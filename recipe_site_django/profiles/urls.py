from django.urls import path
from recipe_site_django.profiles.views import profile_details

urlpatterns = (
    path('', profile_details, name='profile-details'),
)



