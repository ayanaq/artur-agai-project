from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/v1/catalog/', include('catalog.urls')),
    path('api/v2/auth/', include('users.urls')),
    path('api/v1/gpt/', include('gpt.urls')),

    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)