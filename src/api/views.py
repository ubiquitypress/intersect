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
from django.forms.models import model_to_dict
import mimetypes
from django.shortcuts import Http404
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_registered')
    serializer_class = UserSerializer

class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Section.objects.all().order_by('-id')
    serializer_class = SectionSerializer

class DeletedSectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DeletedSection.objects.all().order_by('-id')
    serializer_class = DeletedSectionSerializer

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

class DeleteIssueViewSet(DestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Issue.objects.all().order_by('-id')
    serializer_class = IssueSerializer

    def delete(self, request, format=None, *args, **kw):
        issue = get_object_or_404(Issue, id=int(self.kwargs['issue_id']))
        articles = PublishedArticle.objects.filter(issue=issue)
        print "deleting issues"
        print articles
        deleted_issue = DeletedIssue(
            id = issue.id,
            journal = issue.journal.id,
            volume = issue.volume,
            number = issue.number,
            year = issue.year,
            published = issue.published,
            current = issue.current,
            date_published = issue.date_published,
            date_notified = issue.date_notified,
            access_status = issue.access_status,
            open_access_date = issue.open_access_date,
            show_volume = issue.show_volume,
            show_number = issue.show_number,
            show_year = issue.show_year,
            show_title = issue.show_title,
            style_file_name = issue.style_file_name,
            original_style_file_name = issue.original_style_file_name,
            last_modified = issue.last_modified
        )
        deleted_issue.save()
        print deleted_issue
        for published_article in articles:
            print published_article.article
            article = published_article.article
            print article
            deleted_article =  DeletedArticle(
                id = article.id,
                locale = article.locale, 
                user = article.user.id,
                journal = article.journal.id,
                section_id = article.section_id,
                language = article.language,
                comments_to_ed = article.comments_to_ed,
                citations = article.citations,
                date_submitted = article.date_submitted,
                last_modified = article.last_modified,
                date_status_modified = article.date_status_modified,
                status = article.status,
                submission_progress = article.submission_progress,
                current_round = article.current_round,
                submission_file_id = article.submission_file_id,
                revised_file_id = article.revised_file_id,
                review_file_id = article.review_file_id,
                editor_file_id = article.editor_file_id,
                pages = article.pages,
                fast_tracked = article.fast_tracked,
                hide_author = article.hide_author,
                comments_status = article.comments_status
                )
            deleted_article.save()
            authors = Author.objects.filter(article = article)
            for author in authors:
                new_author = DeletedAuthor(
                    id = author.id,
                    deleted_article = deleted_article.id,
                    primary_contact = author.primary_contact,
                    seq = author.seq,
                    first_name = author.first_name,
                    middle_name = author.middle_name,
                    last_name = author.last_name,
                    country = author.country,
                    email = author.email,
                    url = author.url,
                    user_group = author.user_group.id,
                    suffix = author.suffix,
                    )
                new_author.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeleteArticleViewSet(DestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer

    def delete(self, request, format=None, *args, **kw):
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))
        deleted_article =  DeletedArticle(
            id = article.id,
            locale = article.locale, 
            user = article.user.id,
            journal = article.journal.id,
            section_id = article.section_id,
            language = article.language,
            comments_to_ed = article.comments_to_ed,
            citations = article.citations,
            date_submitted = article.date_submitted,
            last_modified = article.last_modified,
            date_status_modified = article.date_status_modified,
            status = article.status,
            submission_progress = article.submission_progress,
            current_round = article.current_round,
            submission_file_id = article.submission_file_id,
            revised_file_id = article.revised_file_id,
            review_file_id = article.review_file_id,
            editor_file_id = article.editor_file_id,
            pages = article.pages,
            fast_tracked = article.fast_tracked,
            hide_author = article.hide_author,
            comments_status = article.comments_status
            )
        deleted_article.save()
        authors = Author.objects.filter(article = article)
        for author in authors:
            new_author = DeletedAuthor(
                id = author.id,
                deleted_article = deleted_article,
                primary_contact = author.primary_contact,
                seq = author.seq,
                first_name = author.first_name,
                middle_name = author.middle_name,
                last_name = author.last_name,
                country = author.country,
                email = author.email,
                url = author.url,
                user_group = author.user_group,
                suffix = author.suffix,
                )
            new_author.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

       
class DeleteSectionViewSet(DestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Section.objects.all().order_by('-id')
    serializer_class = SectionSerializer

    def delete(self, request, format=None, *args, **kw):
        section = get_object_or_404(Section, id=int(self.kwargs['section_id']))
        deleted_section =  DeletedSection(
            id = section.id,
            journal = section.journal.id,
            seq = section.seq,
            editor_restricted = section.editor_restricted,
            meta_indexed = section.meta_indexed,
            meta_reviewed = section.meta_reviewed,
            abstracts_not_required = section.abstracts_not_required,
            hide_title = section.hide_title,
            hide_author = section.hide_author,
            hide_about = section.hide_about,
            disable_comments = section.disable_comments,
            abstract_word_count = section.abstract_word_count,
            )
        deleted_section.save()
        try:
            if section.review_form:
                deleted_section.review_form = section.review_form.id
            deleted_section.save()
        except ReviewForm.DoesNotExist:
            print "review form does not exist"
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class DeletedArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DeletedArticle.objects.all().order_by('-id')
    serializer_class = DeletedArticleSerializer

class DeletedAuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DeletedAuthor.objects.all().order_by('-id')
    serializer_class = DeletedAuthorSerializer

class ArticlePlusViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ArticleAllSettingsSerializer

    def get(self, request, *args, **kw):
        return Response({'detail':"can only update"},status=status.HTTP_200_OK)
    def put(self, request, *args, **kw):

        print self.request.data

        abstract = self.request.data['abstract']
        print abstract
        title = self.request.data['title']
        print title
        competingInterests = request.data['competing_interests']
        print competingInterests

        funding = request.data['funding']
        print funding
        doi = request.data['doi']
        print doi
        article = request.data['article']
        print article
        current_article = None
        if article:
            current_article = get_object_or_404(Article,id = int(article))
        print current_article

        if abstract:
            setting = ArticleSetting.objects.filter(article = current_article, setting_name= "abstract")
            if setting:
                current_abstract = setting[0]
                print current_abstract.id
                current_abstract.setting_value = abstract
                current_abstract.save()
            else:
                current_abstract = ArticleSetting(article = current_article,setting_name= "abstract",setting_value= abstract, locale="en_US",setting_type="string")
                current_abstract.save()
        if title:
            setting = ArticleSetting.objects.filter(article = current_article, setting_name= "title")
            if setting:
                current_title= setting[0]
                print current_title.id
                current_title.setting_value = title
                current_title.save()
            else:
                current_title = ArticleSetting(article = current_article,setting_name= "title",setting_value= title, locale="en_US",setting_type="string")
                current_title.save()
        if competingInterests:
            setting = ArticleSetting.objects.filter(article = current_article, setting_name= "competingInterests")
            if setting:
                current_competingInterests = setting[0]
                print current_competingInterests.id
                current_competingInterests.setting_value = competingInterests
                current_competingInterests.save()
            else:
                current_competingInterests = ArticleSetting(article = current_article,setting_name= "competingInterests",setting_value= competingInterests, locale="en_US",setting_type="string")
                current_competingInterests.save()
        if funding:
            setting = ArticleSetting.objects.filter(article = current_article, setting_name= "funding")
            if setting:
                current_funding= setting[0]
                print current_funding.id
                current_funding.setting_value = funding
                current_funding.save()
            else:
                current_funding = ArticleSetting(article = current_article,setting_name= "funding",setting_value= funding, locale="en_US",setting_type="string")
                current_funding.save()
        if doi:
            setting = ArticleSetting.objects.filter(article = current_article, setting_name= "pub-id::doi")
            if setting:
                current_doi = setting[0]
                print current_doi.id
                current_doi.setting_value = doi
                current_doi.save()
            else:
                current_doi = ArticleSetting(article = current_article,setting_name= "pub-id::doi",setting_value= doi, locale="en_US",setting_type="string")
                current_doi.save()

        return Response({'detail':"can only update"},status=status.HTTP_200_OK)

class AuthorPlusViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorAllSettingsSerializer

    def get(self, request, *args, **kw):
        return Response({'detail':"can only update"},status=status.HTTP_200_OK)
    def put(self, request, *args, **kw):

        print request.data

        affiliation = request.data['affiliation']
        print affiliation
        biography = request.data['biography']
        print biography
        orcid = request.data['orcid']
        print orcid

        twitter = request.data['twitter']
        print twitter
        department = request.data['department']
        print department
        author = request.data['author']
        print author
        current_author = None
        if author:
            current_author = get_object_or_404(Author,id = int(author))
        print current_author

        if affiliation:
            setting = AuthorSetting.objects.filter(author = current_author, setting_name= "affiliation")
            if setting:
                current_affiliation = setting[0]
                print current_affiliation.id
                current_affiliation.setting_value = affiliation
                current_affiliation.save()
            else:
                current_affiliation = AuthorSetting(author = current_author,setting_name= "affiliation",setting_value= affiliation, locale="en_US",setting_type="string")
                current_affiliation.save()
        if biography:
            setting = AuthorSetting.objects.filter(author = current_author, setting_name= "biography")
            if setting:
                current_biography = setting[0]
                print current_biography.id
                current_biography.setting_value = biography
                current_biography.save()
            else:
                current_biography = AuthorSetting(author = current_author,setting_name= "biography",setting_value= biography, locale="en_US",setting_type="string")
                current_biography.save()
        if orcid:
            setting = AuthorSetting.objects.filter(author = current_author, setting_name= "orcid")
            if setting:
                current_orcid = setting[0]
                print current_orcid.id
                current_orcid.setting_value = orcid
                current_orcid.save()
            else:
                current_orcid = AuthorSetting(author = current_author,setting_name= "orcid",setting_value= orcid, locale="en_US",setting_type="string")
                current_orcid.save()
        if twitter:
            setting = AuthorSetting.objects.filter(author = current_author, setting_name= "twitter")
            if setting:
                current_twitter = setting[0]
                print current_twitter.id
                current_twitter.setting_value = twitter
                current_twitter.save()
            else:
                current_twitter = AuthorSetting(author = current_author,setting_name= "twitter",setting_value= twitter, locale="en_US",setting_type="string")
                current_twitter.save()
        if department:
            setting = AuthorSetting.objects.filter(author = current_author, setting_name= "department")
            if setting:
                current_department = setting[0]
                print current_department.id
                current_department.setting_value = department
                current_department.save()
            else:
                current_department = AuthorSetting(author = current_author,setting_name= "department",setting_value= department, locale="en_US",setting_type="string")
                current_department.save()
      

        return Response({'detail':"can only update"},status=status.HTTP_200_OK)



class PublishedArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PublishedArticle.objects.all().order_by('-id')
    serializer_class = PublishedArticleSerializer

class UnPublishedArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UnPublishedArticle.objects.all().order_by('-pk')
    serializer_class = UnPublishedArticleSerializer



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

class DeletedIssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DeletedIssue.objects.all().order_by('-id')
    serializer_class = DeletedIssueSerializer

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

class SectionSettingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SectionSetting.objects.all().order_by('-id')
    serializer_class = SectionSettingSerializer

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
            issue_setting = get_object_or_404(IssueSetting, issue=issue, setting_name = setting)
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
            author_setting = get_object_or_404(AuthorSetting, author=author, setting_name = setting)
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

    def perform_update(self, serializer):

        print serializer.data
        print self.request.data
        if not serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateSectionSettingOneViewSet(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SectionSetting.objects.all()
    serializer_class = SectionSettingSerializer

    def perform_update(self, serializer):

        print serializer.data
        print self.request.data
        if serializer.is_valid():
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
            article_setting = get_object_or_404(ArticleSetting, article=article, setting_name = setting)
            article_setting = ArticleSetting.objects.filter(article=article, setting_name = setting)
        else:
            article_setting = ArticleSetting.objects.filter(article=article)
        if article:
            return article_setting
        else:
            return queryset

class ArticleSettingAppViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ArticleSettingSerializer

    def get(self, request, *args, **kw):
        queryset = ArticleSetting.objects.all().order_by('article')
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))
        article_settings = ArticleSetting.objects.filter(article=article)
        list_settings = []
        list_setting_names = ["title","abstract","pub-id::doi","competingInterests","funding"]
        for name in list_setting_names:
            setting = ArticleSetting.objects.filter(article=article, setting_name = name)
            if setting:
                list_settings.append(model_to_dict(setting[0]))
        article_dict = model_to_dict(article)
        article_dict["date_submitted"] = str(article.date_submitted)
        article_dict["last_modified"] = str(article.last_modified)
        article_dict["date_status_modified"] = str(article.date_status_modified)
        if article:
            published_articles = PublishedArticle.objects.filter(article = article)
            if published_articles:
                published_article = published_articles[0]
                article_dict["date_published"] = str(published_article.date_published)
                article_dict["published_pk"] = published_article.id
            else:
                article_dict["date_published"] = None
                article_dict["published_pk"] =  -1
                article_dict["unpublished_pk"] =  article.unpublished_pk()
        print json.dumps(article_dict)
        result = {'settings':list_settings,'article':article_dict}

        response = Response(result, status=status.HTTP_200_OK)
        if article:
            return response
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
            journal_setting = get_object_or_404(JournalSetting,journal=journal, setting_name = setting)
            journal_setting = JournalSetting.objects.filter(journal=journal, setting_name = setting)
   
        else:
            journal_setting = JournalSetting.objects.filter(journal=journal)
        if journal:
            return journal_setting
        else:
            return Response(serializers.serialize('json',  queryset ), status=status.HTTP_404_NOT_FOUND)

class SectionSpecificSettingViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = SectionSettingSerializer

    def get_queryset(self):
        queryset = SectionSetting.objects.all().order_by('section')
        section = get_object_or_404(Section, id=int(self.kwargs['section_id']))
        if 'setting' in self.kwargs:
            setting = self.kwargs['setting']
        else:
            setting = None
        if setting:
            section_setting = get_object_or_404(SectionSetting,section=section, setting_name = setting)
            section_setting = SectionSetting.objects.filter(section=section, setting_name = setting)
   
        else:
            section_setting = SectionSetting.objects.filter(section=section)
        if section:
            return section_setting
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

class LatestSectionOneViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = SectionSerializer

    def get_queryset(self):
        queryset = Section.objects.all().order_by('-id')[:1]
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

class SectionsOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = SectionSerializer

    def get(self, request, *args, **kw):
        queryset = Section.objects.all().order_by('id')
        journal = get_object_or_404(Journal, id=int(self.kwargs['journal_id']))
        list_sections = []
        sections = Section.objects.filter(journal=journal)
        for section in sections:
            if not section.is_deleted():
                section_dict = model_to_dict(section)
                setting = SectionSetting.objects.filter(section = section, setting_name = "title")
                if setting:
                    section_dict['title'] = setting[0].setting_value
                else:
                    section_dict['title'] = " "

                list_sections.append(section_dict)
            print list_sections

        result = {"sections":list_sections}
        if sections:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_404_NOT_FOUND)   

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
        unpublished_articles = UnPublishedArticle.objects.filter(issue=issue)
        list_articles = ""
        list_unpublished_articles = ""
        for id,art in enumerate(published_articles):
            if not art.article.is_deleted():
                list_articles=list_articles+str(art.article.id)
                if not id == len(published_articles)-1:
                   list_articles=list_articles+"," 
        for id,art in enumerate(unpublished_articles):
            if not art.article.is_deleted():
                list_unpublished_articles=list_unpublished_articles+str(art.article.id)
                if not id == len(unpublished_articles)-1:
                   list_unpublished_articles=list_unpublished_articles+"," 
        print published_articles
        result={'articles':list_articles,'unpublished':list_unpublished_articles}

        response = Response(result, status=status.HTTP_200_OK)
        print result
        if not issue.is_deleted():
            return response
        else:
            result = {'detail':'issue is deleted'}

            response = Response(result, status=status.HTTP_404_NOT_FOUND)
            return response
class UnPublishedArticlesOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PublishedArticleSerializer

    def get(self, request, *args, **kw):
        queryset = Article.objects.all().order_by('id') 
        articles = Article.objects.all()
        list_articles = ""

        published = ""
        for id,art in enumerate(articles):
            if not art.is_published():
                title = ArticleSetting.objects.filter(article=art, setting_name = "title")
                abstract = ArticleSetting.objects.filter(article=art, setting_name = "abstract")
                if title and abstract and art.date_submitted and art.pages:
                    unpub = UnPublishedArticle.objects.filter(article = art)
                    if not unpub:
                        list_articles=list_articles+str(art.id)
                        if not id == len(articles)-1:
                           list_articles=list_articles+"," 
            else:
                title = ArticleSetting.objects.filter(article=art, setting_name = "title")
                abstract = ArticleSetting.objects.filter(article=art, setting_name = "abstract")
                if title and abstract and art.date_submitted and art.pages:
                    published=published+str(art.id)
                    if not id == len(articles)-1:
                       published=published+","

            
        print articles
        result={'unpublished_articles':list_articles,'published_articles':published}

        response = Response(result, status=status.HTTP_200_OK)
        print result

        if articles:
            return response
        else:
            result = {'detail':'no unpublished article found.'}

            response = Response(result, status=status.HTTP_404_NOT_FOUND)
            return response
class ListIssuesViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = IssueSerializer

    def get(self, request, *args, **kw):
        issues = Issue.objects.all().order_by('id')    
        list_issues = ""
        for id,issue in enumerate(issues):
            if not issue.is_deleted():
                list_issues=list_issues+str(issue.id)
                if not id == len(issues)-1:
                   list_issues=list_issues+"," 
            
        print issues
        result={'issues':list_issues}

        response = Response(result, status=status.HTTP_200_OK)
        print result
        if issues:
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
class AllAuthorsArticleOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kw):
        queryset = Author.objects.all().order_by('id')
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))
        list_authors = []
         
        authors = Author.objects.filter(article=article)
        if authors:
            for id,art in enumerate(authors):
                list_authors.append(art.id)
            
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
class AuthorsIssueAppViewSet(APIView):
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
                
                art_dict = model_to_dict(art)
                
                list_settings = {}
                list_setting_names = ["biography","orcid","twitter","department","affiliation"]
                for name in list_setting_names:
                   setting = AuthorSetting.objects.filter(author=art, setting_name = name)
                   if setting:
                      list_settings[setting[0].setting_name]=model_to_dict(setting[0])
                art_dict['settings'] = list_settings
                list_authors.append(art_dict)
                
            print len(authors)
            print list_authors
        result={'authors':list_authors,'articles':list_articles}

        response = Response(result, status=status.HTTP_200_OK)
        print result
        if published_articles and list_authors:
            return response
        else:
            return Response(result, status=status.HTTP_404_NOT_FOUND)     

class OneAuthorsIssueAppViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kw):
        queryset = Author.objects.all().order_by('id')
        author = get_object_or_404(Author, id=int(self.kwargs['author_id']))
        author_dict = model_to_dict(author)   
        list_settings = []
        list_setting_names = ["biography","orcid","twitter","department","affiliation"]
        for name in list_setting_names:
            setting = AuthorSetting.objects.filter(author=author, setting_name = name)
            if setting:
                list_settings.append(model_to_dict(setting[0]))
        author_dict['settings'] = list_settings
                
  
        result=author_dict

        response = Response(result, status=status.HTTP_200_OK)
        print result
        if author:
            return response
        else:
            return Response(result, status=status.HTTP_404_NOT_FOUND)     

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

class UnPublishedArticleOneViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PublishedArticleSerializer

    def get(self, request, *args, **kw):
        queryset = PublishedArticle.objects.all().order_by('article')
        article = get_object_or_404(Article, id=int(self.kwargs['article_id']))
        print article
        article_published = get_object_or_404(UnPublishedArticle, article=article)
        result={
        'id':article_published.pk,
        'article':article_published.article.id,
        'issue':article_published.issue.id,
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
    folder_structure = os.path.join(settings.BASE_DIR, 'files', 'articles', str(article.id),'public')

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

    type_edit = original_filename[original_filename.rfind('.')+1:]
    print type_edit

    new_article_galley = ArticleGalley(
        locale = article.locale,
        article = article,
        file = new_article_file,
        label = type_edit.upper(),
        html_galley = 0,
        seq = 1,
        )
    new_article_galley.save()
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
    file_path = os.path.join(settings.BASE_DIR, 'files', 'articles', str(article.id), 'public', _file.uuid_filename)

    try:
        fsock = open(file_path, 'rb')
        mimetype = mimetypes.guess_type(file_path)
        response = HttpResponse(FileWrapper(fsock), content_type=mimetype)
        response['Content-Disposition'] = "attachment; filename=%s" % (_file.original_filename)
        #log.add_log_entry(book=book, user=request.user, kind='file', message='File %s downloaded.' % _file.original_filename, short_name='Download')
        return response
    except IOError:
        return Response(status=404)