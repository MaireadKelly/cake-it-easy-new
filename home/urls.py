from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),  # This points to the home view function
    path('shop/', views.shop, name='shop'),  # This is the pattern for your shop view
]
