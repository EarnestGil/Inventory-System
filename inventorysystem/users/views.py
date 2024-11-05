from django.shortcuts import render

# Create your views here.
from os import remove as delete_file

from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    form_class = LoginForm

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)

class MyProfile(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'users/profile.html', context)

    def post(self, request):
        # user's current avatar
        old_avatar_path = request.user.profile.avatar.path
        old_avatar_name = request.user.profile.avatar.name

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            # if avatar is not default
            if old_avatar_name != 'avatar.jpg':
                # if user uploaded a file
                if request.FILES:
                    # remove user's old avatar
                    delete_file(old_avatar_path)

            messages.success(request,'Your profile has been updated successfully')

            return redirect('my_profile')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request,'Error updating your profile')

            return render(request, 'users/profile.html', context)
