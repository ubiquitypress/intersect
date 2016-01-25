from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import *

from rest_framework import generics

from api.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_registered')
    serializer_class = UserSerializer


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

class IssueSettingOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = IssueSettingSerializer

    def get_queryset(self):
        queryset = IssueSetting.objects.all().order_by('-issue')
        issue = Issue.objects.get(id=int(self.kwargs['issue_id']))
        if issue:
            return IssueSetting.objects.filter(issue=issue)
        else:
            return queryset

class IssueOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = IssueSerializer

    def get_queryset(self):
        queryset = Issue.objects.all().order_by('-id')
        issue = Issue.objects.filter(id=int(self.kwargs['issue_id']))
        if issue:
            return issue
        else:
            return queryset

class ArticleOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all().order_by('-id')
        article = Article.objects.filter(id=int(self.kwargs['article_id']))
        if article:
            return article
        else:
            return queryset

class ArticleSettingOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ArticleSettingSerializer

    def get_queryset(self):
        queryset = ArticleSetting.objects.all().order_by('-article')
        article = Article.objects.get(id=int(self.kwargs['article_id']))
        if article:
            return ArticleSetting.objects.filter(article=article)
        else:
            return queryset

class UserOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all().order_by('-date_registered')
        user = User.objects.filter(id=int(self.kwargs['user_id']))
        if user:
            return user
        else:
            return queryset