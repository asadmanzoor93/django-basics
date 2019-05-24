from django.urls import path
from django.views.generic.base import TemplateView

from users import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='user_signup'),
    path('login/', views.LoginUser.as_view(), name='user_login'),
    path('logout/', views.LogoutUser.as_view(), name='user_logout'),
    path('update_profile/', views.UpdateProfile.as_view(), name='user_profile'),
    path('', TemplateView.as_view(template_name='signup_form.html'), name='signup_form'),
]
