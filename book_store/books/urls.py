from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index_page"),
    # path("api/products/", views.products_api, name="procducts_api"),
    path("category/<str:cats>/", views.category, name="catergories"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
]
