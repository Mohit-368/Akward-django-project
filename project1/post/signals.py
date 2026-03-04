"""
signals.py
"""

# ============================================================
# IMPORTS
# ============================================================

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


# ============================================================
# SIGNAL: AUTO CREATE USER PROFILE
# ============================================================

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# ============================================================
# NOTES
# ============================================================

"""
ABOUT THIS FILE
---------------
This module contains signal handlers for the application.

Purpose:
    Automatically create a UserProfile instance
    whenever a new User is created.

Why Signals?
    To decouple profile creation logic from views.
    This ensures profile creation works for:
        - Registration form
        - Admin panel
        - Shell
        - Any script creating users

Signals are event-driven automation inside Django.


IMPORTS
-------
- post_save      : Triggered AFTER a model instance is saved to the database.
- User           : Built-in Django User model. We listen to save events from this model.
- receiver       : Decorator that connects a function to a specific signal.
- UserProfile    : The profile model linked One-to-One with User.


FUNCTION: create_user_profile
------------------------------
Signal handler that runs after a User is saved.

Parameters:
    sender   → The model class sending the signal (User)
    instance → The actual User object being saved
    created  → Boolean (True if new user, False if update)
    **kwargs → Extra metadata passed by Django

Logic:
    If a new user is created, automatically create
    a corresponding UserProfile.

if created:
    This check is CRITICAL.
    Without it, every time a user updates their profile,
    Django would try to create another UserProfile.
    Since UserProfile has a OneToOneField, that would cause IntegrityError.

UserProfile.objects.create(user=instance)
    instance is the newly created User object.
    This creates a UserProfile linked to that specific user.


IMPORTANT POINTS TO REMEMBER
------------------------------
1. This file MUST be imported in apps.py using ready():
       def ready(self):
           import yourapp.signals

   Otherwise, the signal will never register.

2. Signals run silently.
   If debugging, add temporary print statements.

3. Always use 'if created:' for post_save signals
   when creating related objects.

4. Keep signal logic LIGHT.
   Do NOT:
       - Call external APIs
       - Perform heavy computation
       - Write complex business logic

5. Signals are best for:
       - Creating related models
       - Cleaning up files on delete
       - Logging actions

6. Signals are NOT good for:
       - Payment processing
       - Large workflows
       - Complex side effects

7. If project scales:
       Consider moving heavy operations to Celery tasks.

8. Remember:
       Signals improve decoupling,
       but overusing them makes debugging difficult.
"""