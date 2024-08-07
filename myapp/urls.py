from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('post/new/', views.create, name='create'),
    path('post/<int:pk>/edit/', views.edit, name='edit'),
    path('post/<int:pk>/delete/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
