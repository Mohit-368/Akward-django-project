"""
views.py
"""

# ============================================================
# IMPORTS
# ============================================================

import time
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone

from .utils import generate_otp, hash_otp, send_otp_email
from .models import Post
from .forms import Postfrom, UserRegistrationForm, userprofileform


# ============================================================
# HOME PAGE VIEW
# ============================================================

def index(request):
    return render(request, 'index.html')


# ============================================================
# POST LIST VIEW
# ============================================================

def post_list(request):
    post_list = Post.objects.all().order_by('-id')
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_obj': page_obj})


# ============================================================
# CREATE POST VIEW
# ============================================================

@login_required
def post_create(request):
    if request.method == 'POST':
        form = Postfrom(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')

    else:
        form = Postfrom()

    return render(request, 'post_form.html', {'form': form})


# ============================================================
# EDIT POST VIEW
# ============================================================

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)

    if request.method == 'POST':
        form = Postfrom(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')

    else:
        form = Postfrom(instance=post)

    return render(request, 'post_form.html', {'form': form})


# ============================================================
# DELETE POST VIEW
# ============================================================

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'post_delete_confirm.html', {'post': post})


# ============================================================
# USER REGISTRATION VIEW
# ============================================================

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user_data = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password1'],
            }

            otp = generate_otp()
            hashed_otp = hash_otp(otp)

            request.session['registration_data'] = user_data
            request.session['otp_hash'] = hashed_otp
            request.session['otp_attempts'] = 0
            request.session['otp_created_at'] = time.time()

            send_otp_email(user_data['email'], otp)

            messages.success(request, "OTP sent to your email.")
            return redirect('verify_otp')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


# ============================================================
# OTP VERIFICATION VIEW
# ============================================================

def verify_otp(request):
    if 'registration_data' not in request.session or 'otp_hash' not in request.session:
        messages.error(request, "Session expired or invalid. Please register again.")
        return redirect("register")

    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        stored_hash = request.session.get('otp_hash')
        attempts = request.session.get('otp_attempts', 0)
        created_at = request.session.get('otp_created_at', 0)

        if attempts >= 5:
            request.session.flush()
            messages.error(request, "Too many attempts. Please register again.")
            return redirect("register")

        if time.time() - created_at > 600:
            request.session.flush()
            messages.error(request, "OTP expired. Please register again.")
            return redirect("register")

        if check_password(entered_otp, stored_hash):
            user_data = request.session['registration_data']

            try:
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password']
                )

                del request.session['registration_data']
                del request.session['otp_hash']
                del request.session['otp_attempts']
                del request.session['otp_created_at']

                login(request, user)
                messages.success(request, "Account verified and created successfully!")
                return redirect("post_list")

            except IntegrityError:
                request.session.flush()
                messages.error(request, "Username or email was taken while you were verifying. Please try again.")
                return redirect("register")

        else:
            request.session['otp_attempts'] += 1
            messages.error(request, f"Invalid OTP. You have {5 - request.session['otp_attempts']} attempts left.")

    return render(request, "registration/verify_otp.html")


# ============================================================
# RESEND OTP VIEW
# ============================================================

def resend_otp(request):
    if request.method != "POST":
        return redirect("verify_otp")

    if 'registration_data' not in request.session:
        messages.error(request, "Session expired. Please register again.")
        return redirect("register")

    created_at = request.session.get('otp_created_at', 0)

    if time.time() - created_at < 60:
        messages.error(request, "Please wait a minute before requesting a new OTP.")
        return redirect("verify_otp")

    otp = generate_otp()
    hashed_otp = hash_otp(otp)

    request.session['otp_hash'] = hashed_otp
    request.session['otp_attempts'] = 0
    request.session['otp_created_at'] = time.time()

    user_email = request.session['registration_data']['email']
    send_otp_email(user_email, otp)

    messages.success(request, "New OTP sent successfully.")
    return redirect("verify_otp")


# ============================================================
# PROFILE VIEW
# ============================================================

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.userprofile
    posts = user.posts.all()

    return render(request, "profile.html", {
        "profile_user": user,
        "profile": profile,
        "posts": posts
    })


# ============================================================
# PROFILE EDIT VIEW
# ============================================================

@login_required
def profile_edit(request, username):
    user = get_object_or_404(User, username=username)

    if request.user != user:
        messages.error(request, "You cannot edit someone else's profile.")
        return redirect("profile", username=user.username)

    profile = user.userprofile

    if request.method == "POST":
        form = userprofileform(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile", username=user.username)

    else:
        form = userprofileform(instance=profile)

    return render(request, "profile_edit.html", {"form": form})


# ============================================================
# POST DETAIL VIEW
# ============================================================

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})


# ============================================================
# NOTES
# ============================================================

"""
ABOUT THIS FILE
---------------
This module contains all view functions responsible for handling:
    - Rendering pages
    - Creating, updating, deleting posts
    - User registration with OTP verification
    - Profile viewing and editing

Each view follows Django's request → process → response lifecycle.


IMPORTS
-------
- time                  : Used to track OTP creation time and enforce expiry/cooldown.
- IntegrityError        : Caught when a user already exists during OTP-verified registration.
- Paginator             : Paginates post list queries.
- render                : Renders HTML templates with context data.
- get_object_or_404     : Fetches object from DB or raises 404.
- redirect              : Redirects user to another URL.
- check_password        : Verifies entered OTP against stored hash.
- messages              : Sends one-time success/error notifications to users.
- User                  : Built-in Django User model for profile lookup and auth operations.
- login_required        : Decorator that blocks unauthenticated users from accessing views.
- login                 : Logs in a user programmatically after OTP verification.
- timezone              : Django utility for timezone-aware datetime handling.
- generate_otp,
  hash_otp,
  send_otp_email        : Local OTP utilities for generation, hashing, and email delivery.
- Post                  : Represents user-created content stored in the database.
- Postfrom,
  UserRegistrationForm,
  userprofileform        : Forms for post creation, user registration, and profile editing.


FUNCTION: index(request)
-------------------------
Homepage view. Renders index.html on GET.


FUNCTION: post_list(request)
-----------------------------
Fetches all posts ordered by newest first.
Paginates results at 10 posts per page.


FUNCTION: post_create(request)
-------------------------------
Only accessible to logged-in users.
GET  → Show empty post form.
POST → Validate → Assign current user → Save → Redirect to post list.
commit=False is used to assign user before saving to DB.


FUNCTION: post_edit(request, post_id)
--------------------------------------
Only the owner of the post can edit it (enforced via user=request.user in query).
GET  → Show pre-filled form.
POST → Validate → Update → Redirect.


FUNCTION: post_delete(request, post_id)
----------------------------------------
Only the owner can delete their post.
GET  → Show confirmation page.
POST → Delete → Redirect to post list.


FUNCTION: register(request)
-----------------------------
Handles new user registration with OTP-based email verification.
Does NOT create user immediately.

Flow:
    1. Validate registration form.
    2. Store user data temporarily in session.
    3. Generate and hash OTP.
    4. Send OTP to user's email.
    5. Redirect to OTP verification page.


FUNCTION: verify_otp(request)
-------------------------------
Verifies the OTP entered by the user before creating the account.

Security checks:
    - Session must contain registration data.
    - Max 5 attempts allowed.
    - OTP expires after 10 minutes (600 seconds).

On success:
    - Creates user in database.
    - Clears session data.
    - Logs user in automatically.

On IntegrityError:
    - Username/email conflict detected.
    - Session flushed, user redirected to register.


FUNCTION: resend_otp(request)
------------------------------
Allows user to request a new OTP.

Security:
    - Only accepts POST requests.
    - Enforces 60-second cooldown between resend requests.
    - Requires active registration session.

On success:
    - Generates new OTP, updates session, resends email.


FUNCTION: profile_view(request, username)
------------------------------------------
Displays a user's public profile.
Fetches user, their related UserProfile, and all their posts.
Requires Post model to use related_name='posts'.


FUNCTION: profile_edit(request, username)
------------------------------------------
Allows authenticated users to edit only their own profile.

Security:
    - login_required prevents unauthenticated access.
    - Backend check (request.user != user) prevents editing others' profiles.

GET  → Show pre-filled profile form.
POST → Validate → Save → Redirect to profile page.


FUNCTION: post_detail(request, post_id)
----------------------------------------
Displays the full content of a single post.
Fetches post by ID or raises 404.


IMPORTANT POINTS TO KEEP IN MIND
----------------------------------
1. Always use commit=False when you need to assign
   extra fields (like user) before saving a form.

2. Never create a user before OTP verification.
   Store data in session, create only after confirmed.

3. Always enforce ownership checks server-side.
   Never rely only on frontend to restrict actions.

4. Session data must be cleaned up after successful
   registration to avoid stale data.

5. OTP should always be:
   - Hashed before storing (never raw)
   - Time-limited (10 minutes)
   - Attempt-limited (max 5 tries)

6. login_required should be applied to any view
   that performs create, edit, or delete operations.

7. Use get_object_or_404 instead of .get()
   to handle missing objects gracefully.

8. related_name='posts' on Post model is required
   for user.posts.all() to work in profile_view.
"""