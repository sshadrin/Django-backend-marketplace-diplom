from django.urls import path
from rest_framework import routers
from .api import CategoryViewSet, ProductViewSet, ReviewViewSet

from .views import (CategoryDetailView, CategoryListView, PopularListView,
                    ProductListView, ProductsDetailView, PromotionListView,
                    ReviewCreateView, ReviewListView, CategoryList, ProductList, ReviewList)

app_name = 'shop'

router = routers.DefaultRouter()
router.register("api/category/", CategoryViewSet)
router.register("api/products/", ProductViewSet)
router.register("api/reviews/", ReviewViewSet)
urlpatterns = router.urls

urlpatterns = [
    path("", CategoryListView.as_view(), name='category'),
    path("api/category/", CategoryList.as_view(), name='api_category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_details'),
    path('category/<int:pk>/products/', ProductListView.as_view(), name='products'),
    path("api/products/", ProductList.as_view(), name='api_products'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='products_details'),
    path('category/popular/', PopularListView.as_view(), name='populars'),
    path('category/promotion/', PromotionListView.as_view(), name='promotion'),
    path('products/<int:pk>/create/', ReviewCreateView.as_view(), name='products_review'),
    path('category/reviews/', ReviewListView.as_view(), name='reviews'),
    path("api/reviews/", ReviewList.as_view(), name='api_reviews'),
]

urlpatterns += router.urls