from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from users.models import CustomUser, BlogPost


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'birth_date', 'location', 'bio')
        widgets = {'birth_date': forms.DateInput(attrs={'class': 'datepicker'})}


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'status')
