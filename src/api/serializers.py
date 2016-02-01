
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
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'middle_name','last_name','country','email','user_group')


class JournalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'path', 'seq','primary_locale','enabled')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'journal', 'section_id','user','date_submitted','pages','locale','language','status','submission_progress','current_round','fast_tracked','hide_author','comments_status')

class PublishedArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublishedArticle
        fields = ('id','issue','article','date_published')

class ArticleSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleSetting
        fields = ('pk','article', 'locale', 'setting_name','setting_value','setting_type')

class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'journal', 'volume','number','year','published', 'show_volume','show_number','show_year', 'show_title',"current","access_status","date_published")

class IssueSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IssueSetting
        fields = ('pk','issue', 'locale', 'setting_name','setting_value','setting_type')

class JournalSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JournalSetting
        fields = ('pk','journal', 'locale', 'setting_name','setting_value','setting_type')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('intersect_user','user', 'journal')