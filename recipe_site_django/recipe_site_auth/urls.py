from django.urls import path
from recipe_site_django.recipe_site_auth import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in', views.SignInView.as_view(), name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    # path('profile/', views.profile_details.as_view(), name='profile details'),
]
