"""
admin.py
"""

# ============================================================
# IMPORTS
# ============================================================

from django.contrib import admin
from .models import Post, UserProfile


# ============================================================
# MODEL REGISTRATION
# ============================================================

admin.site.register(Post)
admin.site.register(UserProfile)


# ============================================================
# NOTES
# ============================================================

"""
ABOUT THIS FILE
---------------
This file registers models with Django Admin panel.

Django Admin provides:
- Automatic database management interface
- CRUD operations for models
- Authentication-protected backend UI

Any model registered here becomes manageable
through the admin dashboard.


IMPORTS
-------
- django.contrib.admin  : Django's built-in admin framework.
                          Provides automatic interface for managing models.

- Post, UserProfile     : Imported so they can be registered
                          inside the Django admin interface.


MODEL REGISTRATION
------------------
After registering Post and UserProfile:
- Objects can be created, edited, deleted, and viewed
- Accessible from: /admin/
- Admin shows basic model fields by default
- Uses __str__() method for display


IMPORTANT POINTS TO KEEP IN MIND
----------------------------------
1. Only registered models appear in Django Admin.

2. __str__ method in model affects how objects
   are displayed inside admin.

3. For better admin experience, you can customize:
   - list_display
   - search_fields
   - list_filter
   - ordering

   Example improvement:

   @admin.register(Post)
   class PostAdmin(admin.ModelAdmin):
       list_display = ('user', 'created_at')
       search_fields = ('text',)
       ordering = ('-created_at',)

4. Admin panel should not replace frontend UI.
   It is meant for internal management.

5. Never expose admin to public without:
   - Strong passwords
   - Proper permissions
   - Production security settings

6. If your project grows:
   Always customize admin for better usability.
"""