from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import FormView, RedirectView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from users.forms import SignUpForm,  ProfileForm
from users.models import CustomUser


class LoginUser(FormView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

            messages.error(request, 'username or password not correct')
        except ObjectDoesNotExist:
            messages.error(request, 'username does not exist !')

        return redirect('user_login')


class LogoutUser(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'logout.html')


class SignUp(FormView):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = CustomUser.objects.create_user(username=username, email=email, password=raw_password)
            auth_user = authenticate(username=user.username, password=raw_password)
            login(request, auth_user)
            return redirect('home')

        return render(request, self.template_name, {'form': form})


class UpdateProfile(FormView):
    template_name = 'profile.html'
    form_class = ProfileForm

    def get(self, request, *args, **kwargs):
        profile_form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': profile_form})

    def post(self, request, *args, **kwargs):
        profile_form = self.form_class(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')

        return render(request, self.template_name, {'form': profile_form})
