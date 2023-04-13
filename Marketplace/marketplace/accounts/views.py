from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from rest_framework import permissions

from shop.models import Review

from .forms import ProfileForm
from .models import Profile

from rest_framework.generics import GenericAPIView
from .serializers import ProfileSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend


class RegisterView(CreateView):
    """Создаем функцию для регистрации нового пользователя"""
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:main")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)

        return response


def login_view(request: HttpRequest) -> HttpResponse:
    """Функция для входа в аккаунт"""
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('accounts:login')

        return render(request, 'accounts/login.html')

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('accounts:login')

    return render(request, 'accounts/login.html', {'error': "Invalid Login or Password!"})


class MyLogoutView(LogoutView):
    """Функция выхода из аккаунта"""
    next_page = reverse_lazy("accounts:login")


class ProfileListView(LoginRequiredMixin, ListView):
    """Создаем функцию для отображения модели Profile в шаблоне"""
    model = Profile
    template_name = 'accounts/main.html'
    context_object_name = "profiles"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Создаем функцию для редактирования профиля"""
    model = Profile
    form_class = ProfileForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse('accounts:main')


class BalanceUpdateView(LoginRequiredMixin, UpdateView):
    """Создаем функцию для поплнения баланса"""
    model = Profile
    fields = "balance",
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse('accounts:main')


class ReviewhistoryListView(LoginRequiredMixin, ListView):
    """Создаем функцию для отображения модели Review в шаблоне"""
    model = Review
    template_name = 'accounts/my-review.html'
    context_object_name = "reviews"


class UserPermissionsAll(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return False


class ProfileList(ListModelMixin, UpdateModelMixin, GenericAPIView):
    """"Создание generic Api view класса для отображения данных модели Profile и возможности их изменения
    в браузере в формате json"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filterset_fields = ['user', ]
    permission_classes = (UserPermissionsAll,)

    def get(self, request: HttpRequest):
        return self.list(request)

    def put(self, request: HttpRequest):
        return self.update(request)

