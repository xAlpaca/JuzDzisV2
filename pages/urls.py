from django.contrib import admin
from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('onas/', views.onas_view, name='onas_view'),
    path('aktualnosci/', views.actual_view, name='actual_view'),
    path('kontakt/', views.kontakt_view, name='kontakt_view'),
    path('zajecia/', views.zajecia_view, name='zajecia_view'),
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
