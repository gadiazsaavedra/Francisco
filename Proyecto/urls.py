"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from AppCoder.views import (hermanos, lista_hermanos, lista_nietos,
                            lista_padres, nietos, padres)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('padres/<nombre>/<edad>/<apellido>', padres),
    path('hermanos/<nombre>/<edad>/<apellido>', hermanos),
    path('nietos/<nombre>/<edad>/<apellido>', nietos),
    path("lista-hermanos", lista_hermanos),
    path("lista-padres", lista_padres),
    path("lista-nietos", lista_nietos),
    ]
