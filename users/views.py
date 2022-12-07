from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, View

from users.forms import CustomUserProfileForm, CustomUserSignUpForm
from users.models import CustomUser


class Signup(View):
    def post(self, request):
        form = CustomUserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            password = form.cleaned_data.get('password1')

            user = authenticate(email=user.email, password=password)
            login(request, user)

            return redirect('homepage:home')

    def get(self, request):
        form = CustomUserSignUpForm()
        return render(request, 'users/signup.html', {'form': form})


class User_list(ListView):
    model = CustomUser
    context_object_name = 'users'
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return CustomUser.objects.active()


class User_detail(View):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        context = {
            'user': user,
        }

        return render(request, 'users/user_detail.html', context)


class Profile(View):
    def post(self, request):
        try:
            form = CustomUserProfileForm(
                request.POST or None,
                instance=request.user)
            form.save()
        except ValueError:
            pass
        return render(request, 'users/profile.html', {'form': form})

    def get(sekf, request):
        form = CustomUserProfileForm(
            request.POST or None,
            instance=request.user)
        return render(request, 'users/profile.html', {'form': form})
