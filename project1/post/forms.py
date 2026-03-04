"""
forms.py
"""

# ============================================================
# IMPORTS
# ============================================================

from django import forms
from .models import Post, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# ============================================================
# POST FORM
# ============================================================

class Postfrom(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["text", "photo", "title"]


# ============================================================
# USER REGISTRATION FORM
# ============================================================

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# ============================================================
# USER PROFILE FORM
# ============================================================

class userprofileform(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_pic", "tagline", 'bio']


# ============================================================
# NOTES
# ============================================================

"""
ABOUT THIS FILE
---------------
This file defines forms for handling user input, validation,
and model-bound data submission.


IMPORTS
-------
- django.forms                          : Django forms module. Handles input validation,
                                          data cleaning, and HTML form generation.

- Post, UserProfile                     : Imported so forms can map user input directly
                                          to their respective database fields.

- UserCreationForm                      : Built-in Django form for creating new users.
                                          Already includes password1, password2,
                                          password validation, and password hashing logic.

- User                                  : Built-in Django User model.
                                          Used for registration form binding.


CLASS: Postfrom(forms.ModelForm)
---------------------------------
ModelForm automatically creates form fields based on the Post model.
Reduces manual field declaration and connects directly to model structure.

fields = ["text", "photo", "title"]
    Only these fields appear in the form.
    We do NOT include: user, created_at, updated_at.
    Those must be controlled by backend logic for security and data integrity.


CLASS: UserRegistrationForm(UserCreationForm)
----------------------------------------------
Extends Django's built-in UserCreationForm.
Adds an email field while keeping username handling,
password validation, and password confirmation logic.

email = forms.EmailField()
    Validates correct email format and cleans input data automatically.

fields = ('username', 'email', 'password1', 'password2')
    Tuple used because Django expects an immutable structure for Meta.fields.
    password1 and password2 are provided by UserCreationForm.


CLASS: userprofileform(forms.ModelForm)
-----------------------------------------
Handles profile picture, tagline, and bio input
mapped directly to the UserProfile model.


IMPORTANT POINTS TO KEEP IN MIND
----------------------------------
1. ModelForm automatically saves data to database
   if form.save() is called.

2. Always use commit=False in views if you need
   to modify object before saving (like assigning user).

3. Never include sensitive fields like 'user'
   inside form fields list.

4. UserCreationForm already handles:
   - Password hashing
   - Password validation
   - Matching passwords

5. Always validate email uniqueness separately
   if required for production systems.

6. Forms handle validation.
   Views handle business logic.
   Keep responsibilities separate.
"""