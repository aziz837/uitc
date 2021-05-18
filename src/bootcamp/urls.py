from django.urls import path

from . import views
from django.conf.urls import url
app_name = "boot"


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.reg, name='register'),
    path('login/', views.login_view, name='login'),
    path('user/<int:pk>/', views.profile, name='profile'),
    path('logout/<int:pk>/', views.logout_view, name='logout'),
    path('edit/<int:pk>/', views.edit_profile, name='edit-profile'),

]