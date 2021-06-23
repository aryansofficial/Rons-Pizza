from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('accounts/', include('accounts.urls')),
    path('kitchen/', include('kitchen.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

