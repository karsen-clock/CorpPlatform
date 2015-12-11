"""CorpPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home','mock.views.getInterfaceList',name='getInterfaceList'),
    url(r'^configPage','mock.views.configPage',name='configPage'),
    url(r'^uploadResponseFile','mock.views.configPage',name='configPage'),
    url(r'^getInterfaceList','mock.views.getInterfaceList',name='getInterfaceList'),
    url(r'^editInterfaceConfig','mock.views.editInterfaceConfig',name='editInterfaceConfig'),
    url(r'^help','mock.views.helpPage',name='helpPage'),
    url(r'^runService','mock.views.runService',name='runservice'),
    url(r'^links','mock.views.links',name='links'),
    url(r'^deleteInterfaceConfig','mock.views.deleteInterfaceConfig',name='deleteInterfaceConfig'),
]
