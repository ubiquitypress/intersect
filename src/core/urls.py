"""core URL Configuration

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
from rest_framework import routers
from api import views

from api.views import IssueSettingOneViewSet, ArticleSettingOneViewSet, IssueOneViewSet, ArticleOneViewSet, UserOneViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'authors', views.AuthorViewSet)

router.register(r'journals', views.JournalViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'issues', views.IssueViewSet)
router.register(r'issue-settings', views.IssueSettingViewSet)
router.register(r'article-settings', views.ArticleSettingViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'get/issue-settings/(?P<issue_id>.+)/', IssueSettingOneViewSet.as_view()),
    url(r'get/issues/(?P<issue_id>.+)/', IssueOneViewSet.as_view()),
    url(r'get/article-settings/(?P<article_id>.+)/', ArticleSettingOneViewSet.as_view()),
    url(r'get/articles/(?P<article_id>.+)/', ArticleOneViewSet.as_view()),
    url(r'get/users/(?P<user_id>.+)/', UserOneViewSet.as_view()),
]
