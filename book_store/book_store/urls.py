from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("books.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('account/', include("account.urls")),
    path('admin/', admin.site.urls),
]
