from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index_page"),
    # path("api/products/", views.products_api, name="procducts_api"),
    path("category/<str:cats>/", views.category, name="catergories"),
    # path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-dashboard/manage-book", views.manageBook, name="manage_book"),
    path("admin-dashboard/manage-book/<int:pk>/edit", views.edit_book, name="edit_book"),
    path("admin-dashboard/profile", views.profile, name="profile"),
    path("admin-dashboard/manageusers", views.manage_users, name="manage_users"),
    path("admin-dashboard/manageusers/<int:pk>/edit", views.edit_user, name="edit_user"),
    path("admin-dashboard/manageusers/adduser", views.add_user, name="add_user"),
    path("404", views.handler404, name="404_page"),
]

