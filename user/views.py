from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import CustomUser


class RegisterView(View):
    def post(self, request):
        email = request.POST.get('reg-email')
        username = request.POST.get('reg-username')
        password = request.POST.get('reg-password')
        confirm_password = request.POST.get('reg-confirm-password')

        if password != confirm_password:
            messages.error(request, 'Пароли не совпадают')
            return redirect('index')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Пользователя с таким именем уже существует')
            return redirect('index')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с такой почтой уже существует')
            return redirect('index')

        CustomUser.objects.create_user(username=username, password=password, email=email)
        return redirect('profile')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
            return redirect('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request):
        user = request.user
        return render(request, self.template_name, {'user_profile': user})
