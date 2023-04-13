from django.urls import path

from .views import OrderhistoryListView, OrdersDetailView, order_create, OrderhistoryList, OrderList

from rest_framework import routers
from .api import OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register("api/history/", OrderItemViewSet)
router.register("api/create/", OrderViewSet)
urlpatterns = router.urls

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='orders_create'),
    path("api/create/", OrderList.as_view(), name='api_orders_create'),
    path('history/', OrderhistoryListView.as_view(), name='orders_history'),
    path("api/history/", OrderhistoryList.as_view(), name='api_orders_history'),
    path('history/<int:pk>', OrdersDetailView.as_view(), name='orders_detail'),
]