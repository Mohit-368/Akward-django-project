"""
apps.py
"""

# ============================================================
# IMPORTS
# ============================================================

from django.apps import AppConfig


# ============================================================
# APP CONFIGURATION
# ============================================================

class PostConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'

    def ready(self):
        import post.signals


# ============================================================
# NOTES
# ============================================================

"""
ABOUT THIS FILE
---------------
This module defines the configuration for the 'post' Django app.

Purpose:
    - Register app-level settings
    - Execute startup logic when Django initializes the app
    - Connect signals properly

This file plays a critical role in enabling signal-based automation.


CLASS: PostConfig(AppConfig)
-----------------------------
Django reads this configuration during project startup.


default_auto_field
------------------
Specifies the default type for automatically generated primary keys in models.

BigAutoField:
    - Uses 64-bit integer
    - Safer for large-scale applications


name = 'post'
-------------
Must match the app folder name exactly.


ready()
-------
Runs once when Django starts the app.
We import signals here to ensure they are registered.

Without this import:
    - signals.py exists
    - but signal handlers are never connected
    - and automation silently fails

'import post.signals' registers all signal handlers.
Do NOT remove this line.


IMPORTANT POINTS TO REMEMBER
------------------------------
1. If signals are not working, first check:
       - Is ready() defined?
       - Is signals imported inside ready()?
       - Is this AppConfig referenced in INSTALLED_APPS?

2. In settings.py, you must use:
       'post.apps.PostConfig'
   NOT just:
       'post'

3. ready() runs once per app load.
   Do not put heavy logic here.

4. Avoid database queries inside ready().
   It can cause startup issues.

5. Signals depend on this file.
   If this file is misconfigured, automation breaks.

6. Keep apps.py minimal.
   Its purpose is configuration, not business logic.
"""