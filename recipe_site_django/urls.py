from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('recipe_site_django.common.urls')),
                  path('recipes/', include('recipe_site_django.recipe_app.urls')),
                  path('auth/', include('recipe_site_django.recipe_site_auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
