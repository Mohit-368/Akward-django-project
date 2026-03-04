"""
models.py
"""

# ============================================================
# IMPORTS
# ============================================================

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


# ============================================================
# POST MODEL
# ============================================================

class Post(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=200, default="Untitled")
    text = models.TextField(max_length=400)
    photo = models.ImageField(
        upload_to='photos/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"


# ============================================================
# USER PROFILE MODEL
# ============================================================

class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    profile_pic = models.ImageField(
        upload_to='profile_photos/',
        default='default.jpg'
    )
    tagline = models.CharField(
        max_length=50,
        blank=True
    )
    bio = models.TextField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} profile"


# ============================================================
# NOTES
# ============================================================

"""
ABOUT THIS FILE
---------------
This module defines the database schema for the application.

It contains:
1. Post model        → Stores user-generated posts
2. UserProfile model → Stores additional information for each user

These models represent the data layer of the application.


IMPORTS
-------
- django.db.models              : Core Django ORM module for defining models.
- User                          : Built-in Django User model used for relationships.
- timezone                      : Django utility for timezone-aware datetime handling.
- timedelta                     : Python utility for date arithmetic.


CLASS: Post(models.Model)
--------------------------
Represents a single post created by a user.

Each post:
    - Belongs to one user
    - Contains text content
    - Optionally contains an image
    - Tracks creation and update timestamps

user (ForeignKey)
    Many-to-one relationship: One user → Many posts.
    on_delete=CASCADE: Deleting a user deletes all their posts.
    related_name="posts": Enables reverse access via user.posts.all()

title
    Short title for the post. Defaults to "Untitled".

text (TextField)
    Stores post text. TextField suits variable-length content.
    max_length enforces validation at form level.

photo (ImageField)
    Optional image. Stored in MEDIA_ROOT/photos/
    blank=True → optional in forms.
    null=True  → database can store NULL.

created_at
    Auto-set on creation. Immutable after that.

updated_at
    Auto-updates on every save. Useful for tracking edits.

__str__
    Returns: "username - first10chars"
    Used in admin, debugging, and shell queries.


CLASS: UserProfile(models.Model)
----------------------------------
Extends Django's built-in User model to store additional
user-specific information that doesn't belong in the auth model.

user (OneToOneField)
    One user → One profile.
    on_delete=CASCADE: Deleting a user deletes their profile.

profile_pic (ImageField)
    Stored in MEDIA_ROOT/profile_photos/
    Defaults to 'default.jpg' if no image uploaded.
    Ensure default.jpg exists inside the media folder.

tagline
    Short optional intro line. Max 50 characters.

bio
    Longer optional user description. Max 200 characters.

__str__
    Returns: "username profile"


IMPORTANT POINTS TO REMEMBER
------------------------------
1. Always use OneToOneField for user profile extension.
   Do NOT use ForeignKey for profile model.

2. Always configure MEDIA_ROOT and MEDIA_URL
   when using ImageField.

3. related_name is critical for clean reverse queries:
       user.posts.all()

4. auto_now_add and auto_now:
   Do not manually assign values to these fields.

5. For production:
   - Add database indexes if posts grow large.
   - Consider pagination in views.
   - Consider custom User model if project scales.

6. Never modify User model directly.
   Use profile extension or custom user model from project start.

7. For large scale systems:
   - Add database indexing on created_at
   - Optimize queries using select_related()

8. Keep models clean.
   Business logic should NOT live here.
"""