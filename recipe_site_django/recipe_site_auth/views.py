from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from recipe_site_django.recipe_site_auth.forms import SignInForm, SignUpForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    model = UserModel

    success_url = reverse_lazy('sign-in')


class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('index')


def sign_out(request):
    logout(request)
    return redirect('index')




