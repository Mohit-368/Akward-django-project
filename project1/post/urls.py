from . import views
from django.urls import path
urlpatterns = [
    path('',views.index ,name='index'  ),
    path('list/',views.post_list,name='post_list'),
    path('<int:post_id>/edit/',views.post_edit,name='post_edit'),
    path('create/',views.post_create,name='post_create'),
    path('<int:post_id>/delete/',views.post_delete,name='post_delete'),
    path('register/',views.register,name='register'),
    path("profile/<str:username>/", views.profile_view, name="profile"),
    path("profile/<str:username>/edit/", views.profile_edit, name="profile_edit"),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path("resend-otp/", views.resend_otp, name="resend_otp"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),

]
