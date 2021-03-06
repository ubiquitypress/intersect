
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username','password','first_name', 'middle_name','last_name', 'email','date_registered', 'date_last_login', 'disabled')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'assoc_type', 'assoc_id','publish_email','seq')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    
    deleted = serializers.ReadOnlyField(source='is_deleted')
    
    class Meta:
        model = Author
        fields = ('id','seq','primary_contact','article', 'first_name', 'middle_name','last_name','country','email','url','user_group','deleted')

class DeletedAuthorSerializer(serializers.HyperlinkedModelSerializer):
 
     class Meta:
        model = DeletedAuthor
        fields = ('id','seq','primary_contact','deleted_article', 'first_name', 'middle_name','last_name','country','email','url','user_group')


class JournalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'path', 'seq','primary_locale','enabled')

class SectionSerializer(serializers.HyperlinkedModelSerializer):

    deleted = serializers.ReadOnlyField(source='is_deleted')

    class Meta:
        model = Section
        fields = ('id', 'journal', 'seq','editor_restricted','meta_indexed','meta_reviewed','abstracts_not_required','hide_title','hide_author','hide_about','disable_comments','abstract_word_count','deleted')

class DeletedSectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'journal', 'seq','editor_restricted','meta_indexed','meta_reviewed','abstracts_not_required','hide_title','hide_author','hide_about','disable_comments','abstract_word_count')

class ArticleAllSettingsSerializer(serializers.Serializer):
    title = serializers.CharField()
    funding = serializers.CharField()
    competing_interests = serializers.CharField()
    doi = serializers.CharField()
    abstract = serializers.CharField()
    article = serializers.IntegerField()

class AuthorAllSettingsSerializer(serializers.Serializer):
    biography = serializers.CharField()
    orcid = serializers.CharField()
    twitter = serializers.CharField()
    department = serializers.CharField()
    affiliation = serializers.CharField()
    author = serializers.IntegerField()

class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    deleted = serializers.ReadOnlyField(source='is_deleted')
    published = serializers.ReadOnlyField(source='is_published')

    class Meta:
        model = Article
        fields = ('id', 'journal', 'section_id','user','date_submitted','pages','locale','language','status','submission_progress','current_round','fast_tracked','hide_author','comments_status','last_modified','deleted','published','published_pk','unpublished_pk')

class DeletedArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DeletedArticle
        fields = ('id', 'journal', 'section_id','user','date_submitted','pages','locale','language','status','submission_progress','current_round','fast_tracked','hide_author','comments_status','last_modified')

class PublishedArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublishedArticle
        fields = ('id', 'article', 'issue','date_published','seq','access_status')

class UnPublishedArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UnPublishedArticle
        fields = ('pk', 'article', 'issue','seq','access_status')

class ArticleSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleSetting
        fields = ('pk','article', 'locale', 'setting_name','setting_value','setting_type')

class IssueSerializer(serializers.HyperlinkedModelSerializer):

    deleted = serializers.ReadOnlyField(source='is_deleted')

    class Meta:
        model = Issue
        read_only = ('deleted',)
        fields = ('id', 'journal', 'volume','number','year','published', 'show_volume','show_number','show_year', 'show_title',"current","access_status","date_published",'last_modified','deleted')

class DeletedIssueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DeletedIssue
        fields = ('id', 'journal', 'volume','number','year','published', 'show_volume','show_number','show_year', 'show_title',"current","access_status","date_published",'last_modified')


class FileSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='pk')
    class Meta:
        model = File
        fields = ('id','owner', 'original_filename','label')

class IssueSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IssueSetting
        fields = ('pk','issue', 'locale', 'setting_name','setting_value','setting_type')

class SectionSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SectionSetting
        fields = ('pk','section', 'locale', 'setting_name','setting_value','setting_type')

class AuthorSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthorSetting
        fields = ('pk','author', 'locale', 'setting_name','setting_value','setting_type')

class JournalSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JournalSetting
        fields = ('pk','journal', 'locale', 'setting_name','setting_value','setting_type')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('intersect_user','user', 'journal')