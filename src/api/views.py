from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from api.serializers import *
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from rest_framework.views import APIView
from api.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_registered')
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-intersect_user')
    serializer_class = ProfileSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all().order_by('-id')
    serializer_class = AuthorSerializer

class JournalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Journal.objects.all().order_by('-id')
    serializer_class = JournalSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer

class PublishedArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PublishedArticle.objects.all().order_by('-id')
    serializer_class = PublishedArticleSerializer

class ArticleSettingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ArticleSetting.objects.all().order_by('-id')
    serializer_class = ArticleSettingSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Issue.objects.all().order_by('-id')
    serializer_class = IssueSerializer

class IssueSettingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IssueSetting.objects.all().order_by('-issue')
    serializer_class = IssueSettingSerializer

class JournalSettingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = JournalSetting.objects.all().order_by('-journal')
    serializer_class = JournalSettingSerializer

class IssueSettingOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = IssueSettingSerializer

    def get_queryset(self):
        queryset = IssueSetting.objects.all().order_by('issue')
        issue = get_object_or_404(Issue, id=int(self.kwargs['issue_id']))
        print self.kwargs
        if 'setting' in self.kwargs:
            setting = self.kwargs['setting']
        else:
            setting = None
        if setting:
            issue_setting = IssueSetting.objects.filter(issue=issue, setting_name = setting)
        else:
            issue_setting = IssueSetting.objects.filter(issue=issue)
        if issue:
            return issue_setting
        else:
            return queryset

class UpdateIssueSettingOneViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = IssueSetting.objects.all()
    serializer_class = IssueSettingSerializer

    def perform_update(self, serializer):
        serializer.save()

class UpdateJournalSettingOneViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = JournalSetting.objects.all()
    serializer_class = JournalSettingSerializer

    def perform_update(self, serializer):
        serializer.save()

class UpdateArticleSettingOneViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = ArticleSetting.objects.all()
    serializer_class = ArticleSettingSerializer

    def perform_update(self, serializer):
        serializer.save()


class ArticleSettingOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ArticleSettingSerializer

    def get_queryset(self):
        queryset = ArticleSetting.objects.all().order_by('article')
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))
        if 'setting' in self.kwargs:
            setting = self.kwargs['setting']
        else:
            setting = None
        if setting:
            article_setting = ArticleSetting.objects.filter(article=article, setting_name = setting)
        else:
            article_setting = ArticleSetting.objects.filter(article=article)
        if article:
            return article_setting
        else:
            return queryset

class LatestArticleOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all().order_by('-id')[:1]
        return queryset

class LatestIssueOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = IssueSerializer

    def get_queryset(self):
        queryset = Issue.objects.all().order_by('-id')[:1]
        return queryset

class LatestJournalOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = JournalSerializer

    def get_queryset(self):
        queryset = Journal.objects.all().order_by('-id')[:1]
        return queryset
class JournalSettingOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = JournalSettingSerializer

    def get_queryset(self):
        queryset = JournalSetting.objects.all().order_by('journal')
        journal = get_object_or_404(Journal, id=int(self.kwargs['journal_id']))
        if journal:
            return JournalSetting.objects.filter(journal=journal)
        else:
            return queryset


class UserOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all().order_by('date_registered')
        user = User.objects.filter(id=int(self.kwargs['user_id']))
        if user:
            return user
        else:
            return queryset

class PublishedArtilesOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PublishedArticleSerializer

    def get(self, request, *args, **kw):
        queryset = PublishedArticle.objects.all().order_by('id')
        issue = get_object_or_404(Issue, id=int(self.kwargs['issue_id']))       
        published_articles = PublishedArticle.objects.filter(issue=issue)
        list_articles = ""
        for id,art in enumerate(published_articles):
            list_articles=list_articles+str(art.article.id)
            if not id == len(published_articles)-1:
               list_articles=list_articles+"," 
            
        print published_articles
        result={'articles':list_articles}

        response = Response(result, status=status.HTTP_200_OK)
        print result
        if issue:
            return response
        else:
            return queryset

class heartbeat(APIView):

    def get(self, request, *args, **kw):
        result={'status':'online'}
        response = Response(result, status=status.HTTP_200_OK)
        return response

class user_id(APIView):

    def get(self, request, *args, **kw):
        result={'id': request.user.pk }
        response = Response(result, status=status.HTTP_200_OK)
        return response