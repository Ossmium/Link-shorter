from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from accounts.forms import SignUpForm, LoginForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    initial = None
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='accounts/login')
        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super(SignUpView, self).dispatch(request, *args, **kwargs)


class UsersListView(ListView):
    queryset = User.objects.all()
    template_name = 'accounts/users.html'
    context_object_name = 'users'


class UserCreateView(UserPassesTestMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:users')
    template_name = 'accounts/users_create.html'

    def test_func(self):
        return self.request.user.is_superuser


def user_links(request, user_id):
    user = get_object_or_404(User, id=user_id)
    links = user.links.all()
    links_data = [{'short_url': link.short_url} for link in links]
    return JsonResponse({'links': links_data})
