"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dzienniczek import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'klasa', views.KlasaViewSet)
router.register(r'uczen', views.UczenViewSet)
router.register(r'przedmiot', views.PrzedmiotViewSet)
router.register(r'ocena', views.OcenaViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('uczniowie/<int:klasa_id>/', views.uczniowie, name='uczen'),
    path('oceny/<int:uczen_id>/', views.oceny, name='oceny'),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]