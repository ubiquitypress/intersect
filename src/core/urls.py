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
from api.views import *

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'authors', views.AuthorViewSet)

router.register(r'journals', views.JournalViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'author-settings', views.AuthorSettingViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'deleted-articles', views.DeletedArticleViewSet)
router.register(r'deleted-authors', views.DeletedAuthorViewSet)
router.register(r'deleted-issues', views.DeletedIssueViewSet)
router.register(r'deleted-sections', views.DeletedSectionViewSet)
router.register(r'published-articles', views.PublishedArticleViewSet)
router.register(r'issues', views.IssueViewSet)
router.register(r'issue-settings', views.IssueSettingViewSet)
router.register(r'article-settings', views.ArticleSettingViewSet)
router.register(r'journal-settings', views.JournalSettingViewSet)
router.register(r'section-settings', views.SectionSettingViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'files', views.FileViewSet)
router.register(r'sections', views.SectionViewSet)




urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^heartbeat/',heartbeat.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'get/issue-settings/(?P<issue_id>.+)/', IssueSettingOneViewSet.as_view()),
    url(r'get/published-articles/(?P<issue_id>.+)/', PublishedArticlesOneViewSet.as_view()),
    url(r'get/issue-ids/', ListIssuesViewSet.as_view()),
    url(r'get/files/(?P<article_id>.+)/', ArticleFilesOneViewSet.as_view()),
    url(r'get/setting/(?P<setting>[-\w:]+)/issue/(?P<issue_id>.+)/', IssueSettingOneViewSet.as_view()),
    url(r'get/setting/(?P<setting>[-\w:]+)/author/(?P<author_id>.+)/', AuthorSettingOneViewSet.as_view()),
    url(r'get/setting/(?P<setting>[-\w:]+)/article/(?P<article_id>.+)/', ArticleSettingOneViewSet.as_view()),
    url(r'get/setting/(?P<setting>[-\w:]+)/journal/(?P<journal_id>.+)/', JournalSpecificSettingViewSet.as_view()),
    url(r'get/setting/(?P<setting>[-\w:]+)/section/(?P<section_id>.+)/', SectionSpecificSettingViewSet.as_view()),
    
    url(r'update/issue/setting/(?P<pk>.+)/', UpdateIssueSettingOneViewSet.as_view()),
    url(r'update/journal/setting/(?P<pk>.+)/', UpdateJournalSettingOneViewSet.as_view()),
    url(r'update/article/setting/(?P<pk>.+)/', UpdateArticleSettingOneViewSet.as_view()),
    url(r'update/section/setting/(?P<pk>.+)/', UpdateSectionSettingOneViewSet.as_view()),

    url(r'get/article/setting/(?P<pk>.+)/', GetArticleSettingOneViewSet.as_view()),
    url(r'update/author/setting/(?P<pk>.+)/', UpdateAuthorSettingOneViewSet.as_view()),
    url(r'get/article-settings/(?P<article_id>.+)/', ArticleSettingOneViewSet.as_view()),
    url(r'app/article-settings/(?P<article_id>.+)/', ArticleSettingAppViewSet.as_view()),
    url(r'get/article/published/(?P<article_id>.+)/', PublishedArticleOneViewSet.as_view()),
    url(r'get/article/authors/(?P<article_id>.+)/', AuthorsArticleOneViewSet.as_view()),
    url(r'get/issue/authors/(?P<issue_id>.+)/', AuthorsIssueOneViewSet.as_view()),
    url(r'app/issue/authors/(?P<issue_id>.+)/', AuthorsIssueAppViewSet.as_view()),
    url(r'app/authors/(?P<author_id>.+)/', OneAuthorsIssueAppViewSet.as_view()),

    url(r'get/journal-settings/(?P<journal_id>.+)/', JournalSettingOneViewSet.as_view()),

    url(r'get/author-settings/(?P<author_id>.+)/', AuthorAllSettingOneViewSet.as_view()),
    url(r'get/sections/(?P<journal_id>.+)/', SectionsOneViewSet.as_view()),
    url(r'get/latest/journal/', LatestJournalOneViewSet.as_view()),
    url(r'custom/articles/', ArticlePlusViewSet.as_view()),
    url(r'custom/authors/', AuthorPlusViewSet.as_view()),
    url(r'get/latest/issue/', LatestIssueOneViewSet.as_view()),
    url(r'get/latest/file/', LatestFileOneViewSet.as_view()),
    url(r'get/total/count/', TotalViewSet.as_view()),
    url(r'get/latest/author/', LatestAuthorOneViewSet.as_view()),
    url(r'get/latest/section/', LatestSectionOneViewSet.as_view()),
    url(r'get/unique/authors/', UniqueAuthorsOneViewSet.as_view()),
    url(r'get/user_id/', user_id.as_view()),
    url(r'get/latest/article/', LatestArticleOneViewSet.as_view()),
    url(r'get/latest/published-article/', LatestPublishedArticleOneViewSet.as_view()),
    url(r'get/users/(?P<user_id>.+)/', UserOneViewSet.as_view()),
    url(r'upload/file/(?P<article_id>.+)/', FileUploadView.as_view()),
    url(r'upload/specific/file/(?P<article_id>\d+)/(?P<file_id>\d+)/', FileUploadView.as_view()),
    url(r'download/file/(?P<article_id>.+)/(?P<file_id>.+)/', FileDownloadView.as_view()),
    #delete
    url(r'delete/file/(?P<file_id>.+)/', DeleteFileViewSet.as_view()),
    url(r'delete/article/(?P<article_id>.+)/', DeleteArticleViewSet.as_view()),
    url(r'delete/issue/(?P<issue_id>.+)/', DeleteIssueViewSet.as_view()),
    url(r'delete/section/(?P<section_id>.+)/', DeleteIssueViewSet.as_view()),
]
