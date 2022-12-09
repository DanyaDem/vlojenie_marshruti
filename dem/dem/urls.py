"""dem URL Configuration

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
from django.urls import path, include
from app import views


posts_patterns = [
    path('', views.test),
    path('top', views.top),
    path('last', views.last),
    path('<int:id>', views.likes)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include(posts_patterns)),
    path('', views.user),
    path('about', views.about),
    path('contacts' , views.contacts),
    path('ERROR' ,views.error),
    path('acces', views.acces),
    path('response', views.response),
    path('cookies', views.cookies),
    path('get', views.get)
]
