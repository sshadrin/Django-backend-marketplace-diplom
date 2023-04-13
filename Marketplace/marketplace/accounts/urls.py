from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (BalanceUpdateView, MyLogoutView, ProfileListView,
                    ProfileUpdateView, RegisterView, ReviewhistoryListView, ProfileList)

from rest_framework import routers
from .api import ProfileViewSet

router = routers.DefaultRouter()
router.register("api/main/", ProfileViewSet)
urlpatterns = router.urls

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(
        template_name="accounts/login.html",redirect_authenticated_user=True,), name='login',),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path("", ProfileListView.as_view(), name='main'),
    path("api/main/", ProfileList.as_view(), name='api_main'),
    path('main/<int:pk>/update/', ProfileUpdateView.as_view(), name='update_profile'),
    path('main/<int:pk>/update/balance/', BalanceUpdateView.as_view(), name='update_balance'),
    path('main/review/', ReviewhistoryListView.as_view(), name='my_reviews'),
]