from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from api.serializers import *
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import DestroyAPIView
from django.core import serializers
from rest_framework.views import APIView

from django.http import HttpResponseRedirect, Http404, HttpResponse, StreamingHttpResponse
from rest_framework.parsers import *
from api.models import *
from django.core.servers.basehttp import FileWrapper
from django.utils import timezone
import mimetypes as mime
from uuid import uuid4
import os

import mimetypes
from django.shortcuts import Http404
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_registered')
    serializer_class = UserSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all().order_by('-id')
    serializer_class = AuthorSerializer

class AuthorSettingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AuthorSetting.objects.all().order_by('-author')
    serializer_class = AuthorSettingSerializer


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

class DeleteFileViewSet(DestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = File.objects.all().order_by('-pk')
    serializer_class = FileSerializer

    def delete(self, request, format=None, *args, **kw):
        file = get_object_or_404(File, id=int(self.kwargs['file_id']))
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = File.objects.all().order_by('-pk')
    serializer_class = FileSerializer


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


class AuthorSettingOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorSettingSerializer

    def get_queryset(self):
        queryset = AuthorSetting.objects.all().order_by('author')
        author = get_object_or_404(Author, id=int(self.kwargs['author_id']))
        print self.kwargs
        if 'setting' in self.kwargs:
            setting = self.kwargs['setting']
        else:
            setting = None
        if setting:
            author_setting = AuthorSetting.objects.filter(author=author, setting_name = setting)
        else:
            author_setting = AuthorSetting.objects.filter(author=author)
        if author:
            return author_setting
        else:
            return queryset


class UpdateIssueSettingOneViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = IssueSetting.objects.all()
    serializer_class = IssueSettingSerializer

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateJournalSettingOneViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = JournalSetting.objects.all()
    serializer_class = JournalSettingSerializer

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateArticleSettingOneViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ArticleSetting.objects.all()
    serializer_class = ArticleSettingSerializer

    def perform_update(self,request, serializer):

        print serializer.data
        if not serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetArticleSettingOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = ArticleSettingSerializer

    def get_queryset(self):
        queryset = ArticleSetting.objects.all().order_by('article')
       
        article_setting = ArticleSetting.objects.filter(pk=int(self.kwargs['pk']))

        if article_setting:
            return article_setting
        else:
            return queryset
       
class UpdateAuthorSettingOneViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = AuthorSetting.objects.all()
    serializer_class = AuthorSettingSerializer

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class JournalSpecificSettingViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = JournalSettingSerializer

    def get_queryset(self):
        queryset = JournalSetting.objects.all().order_by('journal')
        journal = get_object_or_404(Journal, id=int(self.kwargs['journal_id']))
        if 'setting' in self.kwargs:
            setting = self.kwargs['setting']
        else:
            setting = None
        if setting:
            journal_setting = JournalSetting.objects.filter(journal=journal, setting_name = setting)
        else:
            journal_setting = JournalSetting.objects.filter(journal=journal)
        if journal:
            return journal_setting
        else:
            return Response(serializers.serialize('json',  queryset ), status=status.HTTP_404_NOT_FOUND)

class LatestArticleOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all().order_by('-id')[:1]
        return queryset

class LatestPublishedArticleOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PublishedArticleSerializer

    def get_queryset(self):
        queryset = PublishedArticle.objects.all().order_by('-id')[:1]
        return queryset

class LatestIssueOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = IssueSerializer

    def get_queryset(self):
        queryset = Issue.objects.all().order_by('-id')[:1]
        return queryset

class LatestFileOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = File.objects.all().order_by('-pk')[:1]
        return queryset

class LatestAuthorOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all().order_by('-id')[:1]
        return queryset

class UniqueAuthorsOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kw):
        emails = Author.objects.all().values_list('email', flat=True).distinct()
  
        list_of_authors=[{} for t in range(0,emails.count()) ]   
        t=0
        for email in emails:
            author = Author.objects.filter(email = str(email))[:1][0]
            list_of_authors[t] = {
            'first_name':author.first_name,
            'middle_name':author.middle_name,
            'last_name':author.last_name,
            'email':author.email,
            'country':author.country
            }
            t=t+1  
        response = Response(list_of_authors, status=status.HTTP_200_OK)
        print list_of_authors
        if list_of_authors:
            return response
        else:
            return queryset
    
        return emails

class TotalViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
  
    def get(self, request, *args, **kw):
        authors = Author.objects.all().count()
        articles = Article.objects.all().count()
        issues = Issue.objects.all().count()
  
      
        total = {
            'articles':articles,
            'authors':authors,
            'issues':issues,
            }
        response = Response(total, status=status.HTTP_200_OK)
        print total
        if total:
            return response
            
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

class AuthorAllSettingOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorSettingSerializer

    def get_queryset(self):
        queryset = AuthorSetting.objects.all().order_by('author')
        author = get_object_or_404(Author, id=int(self.kwargs['author_id']))
        if author:
            return AuthorSetting.objects.filter(author=author)
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

class ArticleFilesOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PublishedArticleSerializer

    def get(self, request, *args, **kw):
        queryset = PublishedArticle.objects.all().order_by('id')
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))       
        article_files = ArticleFile.objects.filter(article=article)
        list_files = ""
        for id,art in enumerate(article_files):
            print art.id
            try:
                file = File.objects.get(article_file=art.id)
                list_files=list_files+str(file.pk)
                if not id == len(article_files)-1:
                   list_files=list_files+"," 
            except File.DoesNotExist:
                pass;
            
        print article_files
        result={'files':list_files}
        response = Response(result, status=status.HTTP_200_OK)
        print result
        if article:
            return response
        else:
            return queryset

class PublishedArticlesOneViewSet(APIView):
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

class AuthorsArticleOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kw):
        queryset = Author.objects.all().order_by('id')
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))       
        authors = Author.objects.filter(article=article)
        list_authors = ""
        for id,art in enumerate(authors):
            list_authors=list_authors+str(art.id)
            if not id == len(authors)-1:
               list_authors=list_authors+"," 
            
        print len(authors)
        print list_authors
        result={'authors':list_authors}

        response = Response(result, status=status.HTTP_200_OK)
        print result
        if article:
            return response
        else:
            return queryset
class AuthorsIssueOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kw):
        queryset = Author.objects.all().order_by('id')
        issue = get_object_or_404(Issue, id=int(self.kwargs['issue_id']))
        published_articles = PublishedArticle.objects.filter(issue=issue)
        list_authors = []
        list_articles = []
        for record in published_articles:   
            authors = Author.objects.filter(article=record.article)
            if authors:
                list_articles.append(record.article.id)
            for id,art in enumerate(authors):
                list_authors.append(art.id)
                
            print len(authors)
            print list_authors
        result={'authors':list_authors,'articles':list_articles}

        response = Response(result, status=status.HTTP_200_OK)
        print result
        if issue:
            return response
        else:
            return queryset         
class PublishedArticleOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PublishedArticleSerializer

    def get(self, request, *args, **kw):
        queryset = PublishedArticle.objects.all().order_by('article')
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))
        print article
        article_published = get_object_or_404(PublishedArticle, article=article)
        result={
        'id':article_published.id,
        'article':article_published.article.id,
        'issue':article_published.issue.id,
        'date_published':str(article_published.date_published)[:10],
        'seq':article_published.seq,
        'access_status':article_published.access_status}
        if article:

            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(serializers.serialize('json',  queryset ), status=status.HTTP_404_NOT_FOUND)

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

def handle_file(file,article,kind, owner, label=None, specific_id=None):

    original_filename = str(file._get_name())
    filename = str(uuid4()) + str(os.path.splitext(original_filename)[1])
    folder_structure = os.path.join(settings.BASE_DIR, 'files', 'article', str(article.id))

    if not os.path.exists(folder_structure):
        os.makedirs(folder_structure)

    path = os.path.join(folder_structure, str(filename))
    fd = open(path, 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()

    file_mime = mime.guess_type(filename)

    try:
        file_mime = file_mime[0]
    except IndexError:
        file_mime = 'unknown'

    if not file_mime:
        file_mime = 'unknown'

    new_article_file = ArticleFile (
        article = article,
        file_name=original_filename,
        file_type = file_mime,
        file_size = os.path.getsize(path),
        revision = 1,
        round = 1,
        file_stage = 1,
        date_uploaded=timezone.now(),
        date_modified=timezone.now(),
        original_file_name=original_filename,

        )

    new_article_file.save()
    if specific_id:
        new_file = File(
            pk = specific_id,
            mime_type=file_mime,
            original_filename=original_filename,
            uuid_filename=filename,
            stage_uploaded=1,
            kind=kind,
            label=label,
            date_uploaded = timezone.now(),
            owner=owner,
        )
    else:
        new_file = File(
            mime_type=file_mime,
            original_filename=original_filename,
            uuid_filename=filename,
            stage_uploaded=1,
            kind=kind,
            label=label,
            date_uploaded = timezone.now(),
            owner=owner,
        )

    new_file.save()
    new_file.article_file = new_article_file.id
    print new_file.article_file
    new_file.save()
    return new_file

class FileUploadView(APIView):
    parser_classes = (FormParser, MultiPartParser,)

    def post(self, request,format=None,*args, **kw):
        file_obj = request.FILES['file']
        print self.kwargs
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))
        file_id=self.kwargs['file_id']
        if file_id:
            id = int(file_id)
        else:
            id = -1
        if id != -1:
            handle_file(file_obj,article,"ArticleFile",request.user,specific_id=id)
        else:
            handle_file(file_obj,article,"ArticleFile",request.user)
        return Response(status=204)

class FileDownloadView(APIView):
    parser_classes = (FormParser, MultiPartParser,)

    def get(self,request,*args, **kw):

        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))

        file = get_object_or_404(File, id=int(self.kwargs['file_id']))
        

        return serve_file(request,article,file.pk)

def serve_file(request, article, file_id):
    _file = get_object_or_404(File, pk=file_id)
    file_path = os.path.join(settings.BASE_DIR, 'files', 'article', str(article.id), _file.uuid_filename)

    try:
        fsock = open(file_path, 'rb')
        mimetype = mimetypes.guess_type(file_path)
        response = HttpResponse(FileWrapper(fsock), content_type=mimetype)
        response['Content-Disposition'] = "attachment; filename=%s" % (_file.original_filename)
        #log.add_log_entry(book=book, user=request.user, kind='file', message='File %s downloaded.' % _file.original_filename, short_name='Download')
        return response
    except IOError:
        return Response(status=404)