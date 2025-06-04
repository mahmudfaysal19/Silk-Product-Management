from django.conf import settings
from django.conf.urls.static import static

urlpatterns = []

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)