"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


from .views import *

urlpatterns = [
    url(r'^create/$', post_create, name="create"),
    url(r'^update/(?P<id>\d+)$', post_update, name="update"),
    url(r'^delete/(?P<id>\d+)$', post_delete, name="delete"),
    url(r'^detail/(?P<id>\d+)$', post_detail, name="detail"),
    url(r'^login$', auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout$', auth_views.logout_then_login, name='logout'),
    url(r'^$', home, name="home"),
    url(r'^register$', register, name="register"),
]
