"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curiosidade/', views.add_curiosity, name='add_curiosity'),
    path('top/', views.add_top_scorer, name='add_top_scorer'),
    path('edit_curiosity/<int:pk>/', views.edit_curiosity, name='edit_curiosity'),
    path('delete_curiosity/<int:pk>/', views.delete_curiosity, name='delete_curiosity'),
    path('edit_top_scorer/<int:pk>/', views.edit_top_scorer, name='edit_top_scorer'),
    path('delete_top_scorer/<int:pk>/', views.delete_top_scorer, name='delete_top_scorer'),
]


