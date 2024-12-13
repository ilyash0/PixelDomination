from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import CustomUser


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, self.template_name, {'error': 'Passwords do not match'})

        if CustomUser.objects.filter(username=username).exists():
            return render(request, self.template_name, {'error': 'Username already exists'})

        CustomUser.objects.create_user(username=username, password=password)
        return redirect('login')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, self.template_name, {'error': 'Invalid credentials'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request):
        user = request.user
        return render(request, self.template_name, {'user_profile': user})

