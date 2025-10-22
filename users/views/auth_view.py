from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View
from users.forms import UserRegistrationForm
from users.models import CustomUser



class UserLoginView(LoginView):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, message="You are now logged in.")
            return redirect('login')
        messages.error(request, message="Invalid username or password.")
        return render(request, self.template_name, context={'form': form})


def auth_logout(request):
    pass


class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        messages.success(request, message="You are now logged out.")
        return redirect('login')

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')



