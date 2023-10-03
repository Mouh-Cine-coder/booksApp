from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from books import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("books.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path('account/', include("account.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)


handler404 = views.handler404