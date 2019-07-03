"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chart, name='chart'),
    path('get_models_for_make/', views.get_models_for_make, name='get_models_for_make'),
    path('model/', views.get_models_for_make, name='get_models_for_make'),
    path('trim/', views.get_trim_for_model, name='get_trim_for_model'),
    path('year/', views.get_year_for_trim, name='get_year_for_trim'),
    path('chart/', views.get_graph, name='get_graph'),
]

