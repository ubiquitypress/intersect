# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from time import strftime
import datetime
from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    mime_type = models.CharField(max_length=256)
    original_filename = models.CharField(max_length=1000)
    uuid_filename = models.CharField(max_length=100)
    label = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    stage_uploaded = models.IntegerField()
    kind = models.CharField(max_length=100)
    sequence = models.IntegerField(default=1)
    owner = models.ForeignKey(User)
    article_file = models.IntegerField(default=-1)
    issue_file = models.IntegerField(default=-1)

    def truncated_filename(self):
        name, extension = os.path.splitext(self.original_filename)
        file_name=''
        if len(name)>14:
            file_name=name[:14]+'...'+' '+extension
        else:
            file_name=name+extension

        return file_name
    def truncated_filename_long(self):
        name, extension = os.path.splitext(self.original_filename)
        file_name=''
        if len(name)>32:
            file_name=name[:32]+'...'+' '+extension
        else:
            file_name=name+extension

        return file_name    

    def truncated_label(self):
        name = str(self.label)
        if len(name)>=22:
            name = name[:22]+'...'
        return name

    def __unicode__(self):
        return u'%s' % self.original_filename

    def __repr__(self):
        return u'%s' % self.original_filename

    class Meta:
        ordering = ('sequence', '-kind')
class AccessKey(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'access_key_id' )
    context = models.CharField(max_length=40)
    key_hash = models.CharField(max_length=40)
    user = models.ForeignKey('User', db_column = 'user_id' )
    assoc_id = models.BigIntegerField(blank=True, null=True)
    expiry_date = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'AccessKeys' 
        app_label='api'
        managed = False
        db_table = 'access_keys'

    def __unicode__(self):
        return u'%s %s - Expiring on : %s' % (self.user.first_name, self.user.last_name, self.expiry_date)

    def __repr__(self):
        return u'%s %s - Expiring on : %s' % (self.user.first_name, self.user.last_name, self.expiry_date)


class AnnouncementSetting(models.Model):
    announcement = models.OneToOneField('Announcement', db_column='announcement_id')
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'AnnouncementSettings' 
        app_label='api'
        managed = False
        db_table = 'announcement_settings'
        unique_together = (('announcement', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'Announcement:%s, Locale: %s, Expiring on %s' % (self.announcement.pk, self.locale, self.announcement.date_expire)

    def __repr__(self):
        return u'Announcement:%s, Locale: %s, Expiring on %s' % (self.announcement.pk, self.locale, self.announcement.date_expire)


class AnnouncementTypeSetting(models.Model):
    type = models.OneToOneField('AnnouncementType', db_column='type_id')
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'AnnouncementTypeSettings' 
        app_label='api'
        managed = False
        db_table = 'announcement_type_settings'
        unique_together = (('type', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'Type:%s, Locale: %s, Name: %s' % (self.type.pk, self.locale, self.setting_name)

    def __repr__(self):
        return u'Type:%s, Locale: %s, Name: %s' % (self.type.pk, self.locale, self.setting_name)


class AnnouncementType(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'type_id' )
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'AnnouncementTypes' 
        app_label='api'
        managed = False
        db_table = 'announcement_types'

    def __unicode__(self):
        return u'Type:%s, Assoc ID: %s' % (self.type.pk, self.assoc_id)

    def __repr__(self):
        return u'Type:%s, Assoc ID: %s' % (self.type.pk, self.assoc_id)


class Announcement(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'announcement_id' )
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()
    type = models.ForeignKey('AnnouncementType', db_column='type_id')
    date_expire = models.DateTimeField(blank=True, null=True)
    date_posted = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Announcements' 
        app_label='api'
        managed = False
        db_table = 'announcements'

    def __unicode__(self):
        return u'%s, Assoc (ID: %s, Type: %s), Expiring on: %s' % (self.id, self.assoc_id, self.assoc_type, self.date_expire)

    def __repr__(self):
        return u'%s, Assoc (ID: %s, Type: %s), Expiring on: %s' % (self.id, self.assoc_id, self.assoc_type, self.date_expire)

class ArticleComment(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'comment_id' )
    comment_type = models.BigIntegerField(blank=True, null=True)
    role = models.ForeignKey('Role', db_column='role_id')
    article = models.ForeignKey('Article', db_column='article_id')
    assoc_id = models.BigIntegerField()
    author = models.ForeignKey('Author', db_column = 'author_id')
    comment_title = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    viewable = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleComments' 
        app_label='api'
        managed = False
        db_table = 'article_comments'

    def __unicode__(self):
        return u'%s - Article: %s' % (self.id, self.article.id)

    def __repr__(self):
        return u'%s - Article: %s' % (self.id, self.article.id)

class ArticleEventLog(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'log_id' )
    article = models.ForeignKey('Article', db_column='article_id')
    user = models.ForeignKey('User', db_column = 'user_id' )
    date_logged = models.DateTimeField()
    ip_address = models.CharField(max_length=15)
    log_level = models.CharField(max_length=1, blank=True, null=True)
    event_type = models.BigIntegerField(blank=True, null=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleEventLogs' 
        app_label='api'
        managed = False
        db_table = 'article_event_log'

    def __unicode__(self):
        return u'%s - Article: %s, Log level: %s. IP: %s' % (self.id, self.article.id,self.log_level,self.ip_address)

    def __repr__(self):
        return u'%s - Article: %s, Log level: %s. IP: %s' % (self.id, self.article.id,self.log_level,self.ip_address)

class ArticleFile(models.Model):
    id = models.AutoField(primary_key = True, db_column = 'file_id' )
    revision = models.BigIntegerField()
    source_file = models.ForeignKey('ArticleFile', blank=True, null=True, db_column='source_file_id')
    source_revision = models.BigIntegerField(blank=True, null=True)
    article = models.ForeignKey('Article', db_column='article_id')
    file_name = models.CharField(max_length=90)
    file_type = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    original_file_name = models.CharField(max_length=127, blank=True, null=True)
    file_stage = models.BigIntegerField()
    viewable = models.IntegerField(blank=True, null=True)
    date_uploaded = models.DateTimeField()
    date_modified = models.DateTimeField()
    round = models.IntegerField()
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleFiles' 
        app_label='api'
        managed = False
        db_table = 'article_files'
        unique_together = (('id', 'revision'),)

    def __unicode__(self):
        return u'%s, Name: %s - Article: %s' % (self.id, self.file_name, self.article.id)

    def __repr__(self):
        return u'%s, Name: %s - Article: %s' % (self.id, self.file_name, self.article.id)

class ArticleGalleySetting(models.Model):
    galley = models.OneToOneField('ArticleGalley', db_column='galley_id')
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ArticleGalleySettings' 
        app_label='api'
        managed = False
        db_table = 'article_galley_settings'
        unique_together = (('galley', 'locale', 'setting_name'),)


class ArticleGalley(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'galley_id' )
    locale = models.CharField(max_length=5, blank=True, null=True)
    article = models.ForeignKey('Article', db_column='article_id')
    file = models.ForeignKey('ArticleFile', db_column='file_id')
    label = models.CharField(max_length=32, blank=True, null=True)
    html_galley = models.IntegerField()
    style_file = models.ForeignKey('ArticleFile', blank=True, null=True, related_name = 'style_file',db_column='style_file_id')
    seq = models.FloatField()
    remote_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleGalleys' 
        app_label='api'
        managed = False
        db_table = 'article_galleys'

    def __unicode__(self):
        return u'%s - Article: %s, Label: %s' % (self.id, self.article.id, self.label)

    def __repr__(self):
        return u'%s - Article: %s, Label: %s' % (self.id, self.article.id, self.label)

class ArticleHtmlGalleyImage(models.Model):
    galley =  models.ForeignKey('ArticleGalley', db_column='galley_id', primary_key = True)
    file = models.ForeignKey('ArticleFile', db_column='file_id', primary_key = True)

    class Meta:
        verbose_name_plural = 'ArticleHtmlGalleyImages' 
        app_label='api'
        managed = False
        db_table = 'article_html_galley_images'
        unique_together = (('galley', 'file'),)

    def __unicode__(self):
        return u'%s - Galley: %s, File: %s' % (self.pk, self.galley.id, self.file.id)

    def __repr__(self):
        return u'%s - Galley: %s, File: %s' % (self.pk, self.galley.id, self.file.id)

class ArticleNote(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'note_id' )
    article = models.ForeignKey('Article', db_column='article_id')
    user = models.ForeignKey('User', db_column = 'user_id' )
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    title = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    file = models.ForeignKey('ArticleFile', db_column='file_id')

    class Meta:
        verbose_name_plural = 'ArticleNotes' 
        app_label='api'
        managed = False
        db_table = 'article_notes'
 
    def __unicode__(self):
        return u'%s - Article: %s, Title: %s' % (self.id, self.article.id, self.title)

    def __repr__(self):
        return u'%s - Article: %s, Title: %s' % (self.id, self.article.id, self.title)

class ArticleSearchKeywordList(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'keyword_id' )
    keyword_text = models.CharField(unique=True, max_length=60)

    class Meta:
        verbose_name_plural = 'ArticleSearchKeywordLists' 
        app_label='api'
        managed = False
        db_table = 'article_search_keyword_list'

    def __unicode__(self):
        return u'%s - Keyword text: %s' % (self.id, self.keyword_text)

    def __repr__(self):
        return u'%s - Keyword text: %s' % (self.id, self.keyword_text)

class ArticleSearchObjectKeyword(models.Model):
    object = models.OneToOneField('ArticleSearchObject', db_column='object_id')
    keyword = models.OneToOneField('ArticleSearchKeywordList', db_column='keyword_id')
    pos = models.IntegerField( primary_key = True)

    class Meta:
        verbose_name_plural = 'ArticleSearchObjectKeywords' 
        app_label='api'
        managed = False
        db_table = 'article_search_object_keywords'
        unique_together = (('object','keyword', 'pos',),)
    def __unicode__(self):
        return u'%s - Pos: %s,  Keyword text: %s' % (self.pk, self.pos, self.keyword.keyword_text)

    def __repr__(self):
        return u'%s - Pos: %s,  Keyword text: %s' % (self.pk, self.pos, self.keyword.keyword_text)

class ArticleSearchObject(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'object_id' )
    article = models.ForeignKey('Article', db_column='article_id')
    type = models.IntegerField()
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleSearchObjects' 
        app_label='api'
        managed = False
        db_table = 'article_search_objects'
    def __unicode__(self):
        return u'%s - Article: %s,  Type: %s' % (self.id, self.article.id, self.type)

    def __repr__(self):
        return u'%s - Article: %s,  Type: %s' % (self.id, self.article.id, self.type)


class ArticleSetting(models.Model):
    article = models.ForeignKey('Article', db_column='article_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ArticleSettings' 
        app_label='api'
        managed = False
        db_table = 'article_settings'
        unique_together = (('article', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'%s - Article: %s,  Setting Name: %s' % (self.pk, self.article.id, self.setting_name)

    def __repr__(self):
        return u'%s - Article: %s,  Setting Name: %s' % (self.pk, self.article.id, self.setting_name)

class ArticleStage(models.Model):
    stage_id = models.IntegerField(blank=True, null=True)
    stage_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleStages' 
        app_label='api'
        managed = False
        db_table = 'article_stages'

    def __unicode__(self):
        return u'%s - %s' % (self.stage_id, self.stage_name)

    def __repr__(self):
        return u'%s - %s' % (self.stage_id, self.stage_name)


class ArticleStatus(models.Model):
    article = models.OneToOneField('Article', db_column = 'article_id', blank=True, null=True)
    status =  models.IntegerField(blank=True, null=True, db_column = 'status_id' )
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleStatuses' 
        app_label='api'
        managed = False
        db_table = 'article_status'
   
    def __unicode__(self):
        return u'%s - Article ID: %s' % (self.id, self.article.id)

    def __repr__(self):
        return u'%s - Article ID: %s' % (self.id, self.article.id)

class ArticleStatusHistory(models.Model):
    article = models.OneToOneField('Article', db_column='article_id', blank=True, null=True)
    status = models.IntegerField(db_column='status_id', blank=True, null=True)
    date_updated = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'ArticleStatusHistories' 
        app_label='api'
        managed = False
        db_table = 'article_status_history'
   
    def __unicode__(self):
        return u' %s - Article ID: %s' % (self.pk, self.article.id)

    def __repr__(self):
        return u' %s - Article ID: %s' % (self.pk, self.article.id)

class ArticleSuppFileSetting(models.Model):
    supp = models.OneToOneField('ArticleSupplementaryFile', db_column = 'supp_id')
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ArticleSuppFileSettings' 
        app_label='api'
        managed = False
        db_table = 'article_supp_file_settings'
        unique_together = (('supp', 'locale', 'setting_name'),)
    
    def __unicode__(self):
        return u' %s - File ID: %s' % (self.pk, self.supp.id)

    def __repr__(self):
        return u' %s - File ID: %s' % (self.pk, self.supp.id)

class ArticleSupplementaryFile(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'supp_id' )
    file = models.ForeignKey('ArticleFile', db_column='file_id')
    article = models.ForeignKey('Article', db_column='article_id')
    type = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    remote_url = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    show_reviewers = models.IntegerField(blank=True, null=True)
    date_submitted = models.DateTimeField()
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'ArticleSupplementaryFiles' 
        app_label='api'
        managed = False
        db_table = 'article_supplementary_files'

    def __unicode__(self):
        return u' %s - Article ID: %s, File: %s' % (self.id, self.article.id, self.file.file_name)

    def __repr__(self):
        return u' %s - Article ID: %s, File: %s' % (self.id, self.article.id, self.file.file_name)


class ArticleXmlGalley(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'xml_galley_id' )
    galley = models.ForeignKey('ArticleGalley', db_column = 'galley_id')
    article = models.ForeignKey('Article', db_column='article_id')
    label = models.CharField(max_length=32)
    galley_type = models.CharField(max_length=255)
    views = models.IntegerField()

    class Meta:
        verbose_name_plural = 'ArticleXmlGalleys' 
        app_label='api'
        managed = False
        db_table = 'article_xml_galleys'
    
    def __unicode__(self):
        return u' %s - Article ID: %s, Galley ID: %s' % (self.id, self.article.id, self.galley.id)

    def __repr__(self):
        return u' %s - Article ID: %s, Galley ID: %s' % (self.id, self.article.id, self.galley.id)
class DeletedArticle(models.Model):
    id = models.IntegerField(primary_key = True)
    locale = models.CharField(max_length=5, blank=True, null=True)
    user =models.BigIntegerField()
    journal = models.BigIntegerField()
    section_id = models.BigIntegerField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    comments_to_ed = models.TextField(blank=True, null=True)
    citations = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_status_modified = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    submission_progress = models.IntegerField()
    current_round = models.IntegerField()
    submission_file_id = models.BigIntegerField(blank=True, null=True)
    revised_file_id = models.BigIntegerField(blank=True, null=True)
    review_file_id = models.BigIntegerField(blank=True, null=True)
    editor_file_id = models.BigIntegerField(blank=True, null=True)
    pages = models.CharField(max_length=255, blank=True, null=True)
    fast_tracked = models.IntegerField()
    hide_author = models.IntegerField()
    comments_status = models.IntegerField()
   
    def __unicode__(self):
        return u' %s - User: %s %s, Section: %s' % (self.id, self.user.first_name, self.user.last_name, self.section_id)

    def __repr__(self):
        return u' %s - User: %s %s, Section: %s' % (self.id, self.user.first_name, self.user.last_name, self.section_id)

class Article(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'article_id' )
    locale = models.CharField(max_length=5, blank=True, null=True)
    user = models.ForeignKey('User', db_column = 'user_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    section_id = models.BigIntegerField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    comments_to_ed = models.TextField(blank=True, null=True)
    citations = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_status_modified = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    submission_progress = models.IntegerField()
    current_round = models.IntegerField()
    submission_file_id = models.BigIntegerField(blank=True, null=True)
    revised_file_id = models.BigIntegerField(blank=True, null=True)
    review_file_id = models.BigIntegerField(blank=True, null=True)
    editor_file_id = models.BigIntegerField(blank=True, null=True)
    pages = models.CharField(max_length=255, blank=True, null=True)
    fast_tracked = models.IntegerField()
    hide_author = models.IntegerField()
    comments_status = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Articles' 
        app_label='api'
        managed = False
        db_table = 'articles'

    def is_deleted(self):
        deleted=False
        delete_article = DeletedArticle.objects.filter(id=self.id)
        if delete_article:
            deleted=True
        return deleted

    def is_published(self):
        published=False
        published_article = PublishedArticle.objects.filter(article__id=self.id)
        if published_article:
            published=True
        return published

    def published_pk(self):
        published_article = PublishedArticle.objects.filter(article__id=self.id)
        if published_article:
            return published_article[0].id
        else:
            return -1

    def unpublished_pk(self):
        unpublished_article = UnPublishedArticle.objects.filter(article__id=self.id)
        if unpublished_article:
            return unpublished_article[0].id
        else:
            return -1

    def __unicode__(self):
        return u' %s - User: %s %s, Section: %s' % (self.id, self.user.first_name, self.user.last_name, self.section_id)

    def __repr__(self):
        return u' %s - User: %s %s, Section: %s' % (self.id, self.user.first_name, self.user.last_name, self.section_id)

class AuthSource(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'auth_id' )
    title = models.CharField(max_length=60)
    plugin = models.CharField(max_length=32)
    auth_default = models.IntegerField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'AuthSources' 
        app_label='api'
        managed = False
        db_table = 'auth_sources'

    def __unicode__(self):
        return u' %s - Title: %s, settings: %s' % (self.id, self.title, self.settings)

    def __repr__(self):
        return u' %s - Title: %s, settings: %s' % (self.id, self.title, self.settings)

class AuthorSetting(models.Model):
    author = models.ForeignKey('Author', db_column = 'author_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'AuthorSettings' 
        app_label='api'
        managed = False
        db_table = 'author_settings'
        unique_together = (('author', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u' %s - Author: %s %s, Setting: %s' % (self.pk, self.author.first_name, self.author.last_name, self.setting_name)

    def __repr__(self):
        return u' %s - Author: %s %s, Setting: %s' % (self.pk, self.author.first_name, self.author.last_name, self.setting_name)

class Author(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'author_id' )
    article = models.ForeignKey('Article', db_column='submission_id')
    primary_contact = models.IntegerField()
    seq = models.FloatField()
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)
    country = models.CharField(max_length=90, blank=True, null=True)
    email = models.CharField(max_length=90)
    url = models.CharField(max_length=255, blank=True, null=True)
    user_group = models.ForeignKey('Group', blank=True, null=True, db_column = 'user_group_id')
    suffix = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Authors' 
        app_label='api'
        managed = False
        db_table = 'authors'

    def is_deleted(self):
        deleted=False
        delete_issue = DeletedAuthor.objects.filter(id=self.id)
        if delete_issue:
            deleted=True
        return deleted   

    def __unicode__(self):
        return u' %s - %s %s' % (self.id, self.first_name, self.last_name)

    def __repr__(self):
        return u' %s - %s %s' % (self.id, self.first_name, self.last_name)

class DeletedAuthor(models.Model):
    id = models.IntegerField(primary_key = True)
    deleted_article = models.ForeignKey('DeletedArticle')
    primary_contact = models.IntegerField()
    seq = models.FloatField()
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)
    country = models.CharField(max_length=90, blank=True, null=True)
    email = models.CharField(max_length=90)
    url = models.CharField(max_length=255, blank=True, null=True)
    user_group = models.ForeignKey('Group', blank=True, null=True)
    suffix = models.CharField(max_length=40, blank=True, null=True)
   
    def __unicode__(self):
        return u' %s - %s %s' % (self.id, self.first_name, self.last_name)

    def __repr__(self):
        return u' %s - %s %s' % (self.id, self.first_name, self.last_name)

class BooksForReview(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'book_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    status = models.SmallIntegerField()
    author_type = models.SmallIntegerField()
    publisher = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    language = models.CharField(max_length=10)
    copy = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    pages = models.SmallIntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateTimeField()
    date_requested = models.DateTimeField(blank=True, null=True)
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_mailed = models.DateTimeField(blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', blank=True, null=True, db_column = 'user_id')
    editor = models.ForeignKey('User', blank=True, null=True, related_name = 'editor' , db_column = 'editor_id')
    article = models.ForeignKey('Article', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'BooksForReviews' 
        app_label='api'
        managed = False
        db_table = 'books_for_review'
   
    def __unicode__(self):
        return u' %s - Journal: %s Article: %s' % (self.id, self.journal.id, self.article.id)

    def __repr__(self):
        return u' %s - Journal: %s Article: %s' % (self.id, self.journal.id, self.article.id)

class BooksForReviewAuthor(models.Model):
    author = models.OneToOneField('Author', db_column = 'author_id', primary_key = True)
    book = models.ForeignKey('BooksForReview', db_column = 'book_id')
    seq = models.FloatField()
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)

    class Meta:
        verbose_name_plural = 'BooksForReviewAuthor' 
        app_label='api'
        managed = False
        db_table = 'books_for_review_authors'
   
    def __unicode__(self):
        return u' %s - %s %s Book: %s' % (self.pk, self.first_name, self.last_name, self.book.id)

    def __repr__(self):
        return u' %s - %s %s Book: %s' % (self.pk, self.first_name, self.last_name, self.book.id)

class BooksForReviewSetting(models.Model):
    book = models.OneToOneField('BooksForReview', db_column = 'book_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'BooksForReviewSettings' 
        app_label='api'
        managed = False
        db_table = 'books_for_review_settings'
        unique_together = (('book', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u' %s - %s Book: %s' % (self.pk, self.setting_name, self.book.id)

    def __repr__(self):
        return u' %s - %s Book: %s' % (self.pk, self.setting_name, self.book.id)

class Captcha(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'captcha_id' )
    session_id = models.CharField(max_length=40)
    value = models.CharField(max_length=20)
    date_created = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Captchas' 
        app_label='api'
        managed = False
        db_table = 'captchas'

    def __unicode__(self):
        return u' %s - Session: %s' % (self.id, self.session_id)

    def __repr__(self):
        return u' %s - Session: %s' % (self.id, self.session_id)


class CitationSetting(models.Model):
    citation = models.OneToOneField('Citation', db_column = 'citation_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'CitationSettings' 
        app_label='api'
        managed = False
        db_table = 'citation_settings'
        unique_together = (('citation', 'locale', 'setting_name'),)
    
    def __unicode__(self):
        return u' %s - Citation: %s' % (self.pk, self.citation.id)

    def __repr__(self):
        return u' %s - Citation: %s' % (self.pk, self.citation.id)

class Citation(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'citation_id' )
    assoc_type = models.BigIntegerField(primary_key = True)
    assoc_id = models.BigIntegerField(primary_key = True)
    citation_state = models.BigIntegerField()
    raw_citation = models.TextField(blank=True, null=True)
    seq = models.BigIntegerField(unique = True)
    lock_id = models.CharField(max_length=23, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Citations' 
        app_label='api'
        managed = False
        db_table = 'citations'
        unique_together = (('assoc_type', 'assoc_id', 'seq'),)
    
    def __unicode__(self):
        return u' %s - Assoc (ID: %s, Type: %s), Seq: %s' % (self.id, self.assoc_id, self.assoc_type, self.seq)

    def __repr__(self):
        return u' %s - Assoc (ID: %s, Type: %s), Seq: %s' % (self.id, self.assoc_id, self.assoc_type, self.seq)

class Collection(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=150)
    abbrev = models.CharField(max_length=150)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField()
    image_filename = models.CharField(max_length=150, blank=True, null=True)
    date_published = models.DateField()
    date_updated = models.DateField(blank=True, null=True)
    tba = models.TextField(blank=True, null=True)  # This field type is a guess.
    disabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    discussions = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Collections' 
        app_label='api'
        managed = False
        db_table = 'collection'
   
    def __unicode__(self):
        return u' %s - %s' % (self.id, self.name)

    def __repr__(self):
        return u' %s - %s' % (self.id, self.name)

class CollectionArticle(models.Model):
    collection = models.OneToOneField('Collection', db_column = 'collection_id', primary_key=True)
    published_article = models.OneToOneField('Article', db_column='published_article_id', primary_key=True)

    class Meta:
        verbose_name_plural = 'CollectionArticles' 
        app_label='api'
        managed = False
        db_table = 'collection_article'
        unique_together = (('collection', 'published_article'),)
    
    def __unicode__(self):
        return u'Published Article: %s' % (self.published_article.id)

    def __repr__(self):
        return u'Published Article: %s' % (self.published_article.id)

class CollectionUser(models.Model):
    collection = models.OneToOneField('Collection', db_column = 'collection_id', unique=True)
    user = models.OneToOneField('User', db_column = 'user_id', primary_key=True )
    role_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'CollectionUsers' 
        app_label='api'
        managed = False
        db_table = 'collection_user'
        unique_together = (('collection', 'user'),)
  
    def __unicode__(self):
        return u' %s - %s %s' % (self.pk, self.user.first_name, self.user.last_name)

    def __repr__(self):
        return u' %s - %s %s' % (self.pk, self.user.first_name, self.user.last_name)


class Comment(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'comment_id' )
    submission_id = models.BigIntegerField()
    parent_comment = models.ForeignKey('Comment', blank=True, null=True, db_column = 'parent_comment_id')
    num_children = models.IntegerField()
    user = models.ForeignKey('User', blank=True, null=True, db_column = 'user_id')
    poster_ip = models.CharField(max_length=15)
    poster_name = models.CharField(max_length=90, blank=True, null=True)
    poster_email = models.CharField(max_length=90, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Comments' 
        app_label='api'
        managed = False
        db_table = 'comments'
  
    def __unicode__(self):
        return u' %s - Submission: %s, Title: %s' % (self.id, self.submission_id, self.title)

    def __repr__(self):
        return u' %s - Submission: %s, Title: %s' % (self.id, self.submission_id, self.title)

class CompletedPayment(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'completed_payment_id' )
    timestamp = models.DateTimeField()
    payment_type = models.BigIntegerField()
    journal = models.ForeignKey('Journal', db_column='journal_id')
    user = models.ForeignKey('User', blank=True, null=True, db_column = 'user_id')
    assoc_id = models.BigIntegerField(blank=True, null=True)
    amount = models.FloatField()
    currency_code_alpha = models.CharField(max_length=3, blank=True, null=True)
    payment_method_plugin_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'CompletedPayments' 
        app_label='api'
        managed = False
        db_table = 'completed_payments'
  
    def __unicode__(self):
        return u' %s - Type: %s, Journal: %s' % (self.id, self.payment_type, self.journal.id)

    def __repr__(self):
        return u' %s - Type: %s, Journal: %s' % (self.id, self.payment_type, self.journal.id)

class ControlledVocabEntry(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'controlled_vocab_entry_id' )
    controlled_vocab = models.ForeignKey('ControlledVocab', db_column = 'controlled_vocab_id')
    seq = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ControlledVocabEntries' 
        app_label='api'
        managed = False
        db_table = 'controlled_vocab_entries'

    def __unicode__(self):
        return u' %s - Vocab: %s, Seq: %s' % (self.id, self.controlled_vocab.id, self.seq)

    def __repr__(self):
        return u' %s - Vocab: %s, Seq: %s' % (self.id, self.controlled_vocab.id, self.seq)

class ControlledVocabEntrySetting(models.Model):
    controlled_vocab_entry = models.OneToOneField('ControlledVocabEntry', db_column = 'controlled_vocab_entry_id',primary_key = True)
    locale = models.CharField(max_length=5, unique = True)
    setting_name = models.CharField(max_length=255, unique = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ControlledVocabEntrySettings' 
        app_label='api'
        managed = False
        db_table = 'controlled_vocab_entry_settings'
        unique_together = (('controlled_vocab_entry', 'locale', 'setting_name'),)
    
    def __unicode__(self):
        return u' %s - Vocab Entry: %s, Setting: %s' % (self.pk, self.controlled_vocab_entry.id, self.setting_name)

    def __repr__(self):
        return u' %s - Vocab Entry: %s, Setting: %s' % (self.pk, self.controlled_vocab_entry.id, self.setting_name)

class ControlledVocab(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'controlled_vocab_id' )
    symbolic = models.CharField(max_length=64)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'ControlledVocabs' 
        app_label='api'
        managed = False
        db_table = 'controlled_vocabs'
        unique_together = (('symbolic', 'assoc_type', 'assoc_id'),)
  
    def __unicode__(self):
        return u' %s - Symbolic: %s, Assoc (ID: %s, Type: %s)' % (self.id, self.symbolic, self.assoc_id, self.assoc_type)

    def __repr__(self):
        return u' %s - Symbolic: %s, Assoc (ID: %s, Type: %s)' % (self.id, self.symbolic, self.assoc_id, self.assoc_type)

class CustomIssueOrder(models.Model):
    issue = models.OneToOneField('Issue', db_column = 'issue_id', primary_key = True)
    journal = models.ForeignKey('Journal', db_column='journal_id')
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'CustomIssueOrders' 
        app_label='api'
        managed = False
        db_table = 'custom_issue_orders'
    
    def __unicode__(self):
        return u' Issue: %s - Journal: %s, Seq: %s' % (self.issue.id, self.journal.id, self.seq)

    def __repr__(self):
        return u' Issue: %s - Journal: %s, Seq: %s' % (self.issue.id, self.journal.id, self.seq)

class CustomSectionOrder(models.Model):
    issue = models.OneToOneField('Issue', db_column = 'issue_id', primary_key = True)
    section = models.OneToOneField('Section', db_column = 'section_id', unique = True)
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'CustomSectionOrders' 
        app_label='api'
        managed = False
        db_table = 'custom_section_orders'
        unique_together = (('issue', 'section'),)
  
    def __unicode__(self):
        return u' Issue: %s - Section: %s, Seq: %s' % (self.issue.id, self.journal.id, self.seq)

    def __repr__(self):
        return u' Issue: %s - Section: %s, Seq: %s' % (self.issue.id, self.journal.id, self.seq)

class DataObjectTombstoneOaiSetObject(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'object_id' )
    tombstone = models.ForeignKey('DataObjectTombstone', db_column = 'tombstone_id')
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'DataObjectTombstoneOaiSetObjects' 
        app_label='api'
        managed = False
        db_table = 'data_object_tombstone_oai_set_objects'

    def __unicode__(self):
        return u' %s - Tombstone: %s, Assoc (ID: %s, Type: %s)' % (self.id, self.tombstone.id, self.assoc_id, self.assoc_type)

    def __repr__(self):
        return u' %s - Tombstone: %s, Assoc (ID: %s, Type: %s)' % (self.id, self.tombstone.id, self.assoc_id, self.assoc_type)

class DataObjectTombstoneSetting(models.Model):
    tombstone = models.ForeignKey('DataObjectTombstone', db_column = 'tombstone_id', primary_key = True)
    locale = models.CharField(max_length=5, unique = True)
    setting_name = models.CharField(max_length=255, unique = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'DataObjectTombstoneSetting' 
        app_label='api'
        managed = False
        db_table = 'data_object_tombstone_settings'
        unique_together = (('tombstone', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u' %s - Tombstone: %s, Setting: %s' % (self.pk, self.tombstone.id, self.setting_name)

    def __repr__(self):
        return u' %s - Tombstone: %s, Setting: %s' % (self.pk, self.tombstone.id, self.setting_name)

class DataObjectTombstone(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'tombstone_id' )
    data_object_id = models.BigIntegerField()
    date_deleted = models.DateTimeField()
    set_spec = models.CharField(max_length=255)
    set_name = models.CharField(max_length=255)
    oai_identifier = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'DataObjectTombstones' 
        app_label='api'
        managed = False
        db_table = 'data_object_tombstones'

    def __unicode__(self):
        return u' %s - Data Object: %s, Set Name: %s' % (self.id, self.data_object_id, self.set_name)

    def __repr__(self):
        return u' %s - Data Object: %s, Set Name: %s' % (self.id, self.data_object_id, self.set_name)

class DataverseFile(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'dvfile_id' )
    supp_id = models.BigIntegerField()
    submission_id = models.BigIntegerField()
    study_id = models.BigIntegerField()
    content_source_uri = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'DataverseFiles' 
        app_label='api'
        managed = False
        db_table = 'dataverse_files'

    def __unicode__(self):
        return u' %s - Supp: %s, Submission: %s' % (self.id, self.supp_id, self.submission_id)

    def __repr__(self):
        return u' %s - Supp: %s, Submission: %s' % (self.id, self.supp_id, self.submission_id)

class DataverseStudy(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'study_id' )
    submission_id = models.BigIntegerField()
    edit_uri = models.CharField(max_length=255)
    edit_media_uri = models.CharField(max_length=255)
    statement_uri = models.CharField(max_length=255)
    persistent_uri = models.CharField(max_length=255)
    data_citation = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'DataverseStudies' 
        app_label='api'
        managed = False
        db_table = 'dataverse_studies'

    def __unicode__(self):
        return u' %s Submission: %s' % (self.id, self.submission_id)

    def __repr__(self):
        return u' %s Submission: %s' % (self.id, self.submission_id)

class DraftDecision(models.Model):
    key_val = models.CharField(max_length=45)
    senior_editor = models.ForeignKey('User',related_name = 'senior_editor', db_column='senior_editor_id')
    junior_editor = models.ForeignKey('User', db_column='junior_editor_id')
    article = models.ForeignKey('Article', db_column = 'article_id')
    decision = models.IntegerField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    attatchment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'DraftDecisions' 
        app_label='api'
        managed = False
        db_table = 'draft_decisions'

    def __unicode__(self):
        return u' %s Key val: %s' % (self.pk, self.key_val)

    def __repr__(self):
        return u' %s Key val: %s' % (self.pk, self.key_val)

class EditAssignment(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'edit_id' )
    article = models.ForeignKey('Article', db_column='article_id')
    editor = models.ForeignKey('User', db_column='editor_id')
    can_edit = models.IntegerField()
    can_review = models.IntegerField()
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    date_underway = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'EditAssignments' 
        app_label='api'
        managed = False
        db_table = 'edit_assignments'

    def __unicode__(self):
        return u' %s Article ID: %s, Editor: %s %s' % (self.id, self.article.id, self.editor.first_name, self.editor.last_name)

    def __repr__(self):
        return u' %s Article ID: %s, Editor: %s %s' % (self.id, self.article.id, self.editor.first_name, self.editor.last_name)

class EditDecision(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'edit_decision_id' )
    article = models.ForeignKey('Article', db_column='article_id')
    round = models.IntegerField()
    editor = models.ForeignKey('User', db_column='editor_id')
    decision = models.IntegerField()
    date_decided = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'EditDecisions' 
        app_label='api'
        managed = False
        db_table = 'edit_decisions'

    def __unicode__(self):
        return u' %s Article ID: %s, Editor: %s %s' % (self.id, self.article.id, self.editor.first_name, self.editor.last_name)

    def __repr__(self):
        return u' %s Article ID: %s, Editor: %s %s' % (self.id, self.article.id, self.editor.first_name, self.editor.last_name)

class EmailLog(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'log_id' )
    sender = models.ForeignKey('User', db_column = 'sender_id')
    date_sent = models.DateTimeField()
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    event_type = models.BigIntegerField(blank=True, null=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    from_address = models.CharField(max_length=255, blank=True, null=True)
    recipients = models.TextField(blank=True, null=True)
    cc_recipients = models.TextField(blank=True, null=True)
    bcc_recipients = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'EmailLogs' 
        app_label='api'
        managed = False
        db_table = 'email_log'

    def __unicode__(self):
        return u' %s Sender: %s %s Subject: %s' % (self.id, self.sender.first_name, self.sender.last_name, self.subject)

    def __repr__(self):
        return u' %s Sender: %s %s Subject: %s' % (self.id, self.sender.first_name, self.sender.last_name, self.subject)

class EmailLogUser(models.Model):
    email_log = models.OneToOneField('EmailLog', db_column = 'email_log_id', primary_key = True)
    user = models.OneToOneField('User', db_column = 'user_id', primary_key = True )

    class Meta:
        verbose_name_plural = 'EmailLogUsers' 
        app_label='api'
        managed = False
        db_table = 'email_log_users'
        unique_together = (('email_log', 'user'),)
  
    def __unicode__(self):
        return u' Log: %s Sender: %s %s' % (self.email_log.id, self.user.first_name, self.user.last_name)

    def __repr__(self):
        return u' Log: %s Sender: %s %s' % (self.email_log.id, self.user.first_name, self.user.last_name)

class EmailTemplate(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'email_id' )
    email_key = models.CharField(max_length=64)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    enabled = models.IntegerField()

    class Meta:
        verbose_name_plural = 'EmailTemplates' 
        app_label='api'
        managed = False
        db_table = 'email_templates'
        unique_together = (('email_key', 'assoc_type', 'assoc_id'),)

    def __unicode__(self):
        return u' %s, Assoc (ID: %s, Type: %s) - %s' % (self.id, self.assoc_id, self.assoc_type, self.email_key)

    def __repr__(self):
        return u' %s, Assoc (ID: %s, Type: %s) - %s' % (self.id, self.assoc_id, self.assoc_type, self.email_key)

class EmailTemplatesData(models.Model):
    email_key = models.CharField(max_length=64, primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    assoc_type = models.BigIntegerField(blank=True, null=True, unique = True)
    assoc_id = models.BigIntegerField(blank=True, null=True, unique = True)
    subject = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'EmailTemplatesDatas' 
        app_label='api'
        managed = False
        db_table = 'email_templates_data'
        unique_together = (('email_key', 'locale', 'assoc_type', 'assoc_id'),)

    def __unicode__(self):
        return u' %s, Assoc (ID: %s, Type: %s) - Subject: %s' % (self.pk, self.assoc_id, self.assoc_type, self.subject)

    def __repr__(self):
        return u' %s, Assoc (ID: %s, Type: %s) - Subject: %s' % (self.pk, self.assoc_id, self.assoc_type, self.subject)

class EmailTemplatesDefault(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'email_id' )
    email_key = models.CharField(max_length=64)
    can_disable = models.IntegerField()
    can_edit = models.IntegerField()
    from_role = models.ForeignKey('Role', blank=True, null=True, related_name = "from_role", db_column = 'from_role_id')
    to_role = models.ForeignKey('Role', blank=True, null=True, related_name = "to_role", db_column = 'to_role_id')

    class Meta:
        verbose_name_plural = 'EmailTemplatesDefaults' 
        app_label='api'
        managed = False
        db_table = 'email_templates_default'

    def __unicode__(self):
        return u' %s, Email Key: %s' % (self.id, self.email_key)

    def __repr__(self):
        return u' %s, Email Key: %s' % (self.id, self.email_key)

class EmailTemplatesDefaultData(models.Model):
    email_key = models.CharField(max_length=64, primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    subject = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'EmailTemplatesDefaultDatas' 
        app_label='api'
        managed = False
        db_table = 'email_templates_default_data'
        unique_together = (('email_key', 'locale'),)

    def __unicode__(self):
        return u'Locale %s, Email Key: %s' % (self.locale, self.email_key)

    def __repr__(self):
        return u'Locale %s, Email Key: %s' % (self.locale, self.email_key)

class EventLog(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'log_id' )
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey('User', db_column = 'user_id' )
    date_logged = models.DateTimeField()
    ip_address = models.CharField(max_length=39)
    event_type = models.BigIntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    is_translated = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'EventLogs' 
        app_label='api'
        managed = False
        db_table = 'event_log'

    def __unicode__(self):
        return u'%s -  Assoc (ID: %s, Type: %s), Date: %s' % (self.id, self.assoc_id, self.assoc_type, self.date_logged)

    def __repr__(self):
        return u'%s -  Assoc (ID: %s, Type: %s), Date: %s' % (self.id, self.assoc_id, self.assoc_type, self.date_logged)

class EventLogSetting(models.Model):
    event_log = models.OneToOneField('EventLog', db_column = 'log_id',primary_key = True )
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'EventLogSettings' 
        app_label='api'
        managed = False
        db_table = 'event_log_settings'
        unique_together = (('event_log', 'setting_name'),)

    def __unicode__(self):
        return u'Setting: %s, Log: %s' % (self.setting_name, self.event_log.id)

    def __repr__(self):
        return u'Setting: %s, Log: %s' % (self.setting_name, self.event_log.id)

class ExternalFeedSetting(models.Model):
    feed = models.OneToOneField('ExternalFeed', db_column='feed_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ExternalFeedSettings' 
        app_label='api'
        managed = False
        db_table = 'external_feed_settings'
        unique_together = (('feed', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'Setting: %s, Feed: %s' % (self.setting_name, self.feed.id)

    def __repr__(self):
        return u'Setting: %s, Feed: %s' % (self.setting_name, self.feed.id)

class ExternalFeed(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'feed_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    url = models.CharField(max_length=255)
    seq = models.FloatField()
    display_homepage = models.IntegerField()
    display_block = models.SmallIntegerField()
    limit_items = models.IntegerField(blank=True, null=True)
    recent_items = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ExternalFeeds' 
        app_label='api'
        managed = False
        db_table = 'external_feeds'

    def __unicode__(self):
        return u'%s - Journal: %s, Seq: %s' % (self.id, self.journal.id, self.seq)

    def __repr__(self):
        return u'%s - Journal: %s, Seq: %s' % (self.id, self.journal.id, self.seq)

class FilterGroup(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'filter_group_id' )
    symbolic = models.CharField(unique=True, max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    input_type = models.CharField(max_length=255, blank=True, null=True)
    output_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'FilterGroups' 
        app_label='api'
        managed = False
        db_table = 'filter_groups'

    def __unicode__(self):
        return u'%s - Name: %s' % (self.id, self.display_name)

    def __repr__(self):
        return u'%s - Name: %s' % (self.id, self.display_name)

class FilterSetting(models.Model):
    filter = models.ForeignKey('Filter', db_column = 'filter_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'FilterSettings' 
        app_label='api'
        managed = False
        db_table = 'filter_settings'
        unique_together = (('filter', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'Filter: %s - Setting: %s' % (self.filter.id, self.setting_name)

    def __repr__(self):
        return u'Filter: %s - Setting: %s' % (self.filter.id, self.setting_name)

class Filter(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'filter_id' )
    context_id = models.BigIntegerField()
    display_name = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    is_template = models.IntegerField()
    parent_filter = models.ForeignKey('Filter', db_column = 'parent_filter_id')
    seq = models.BigIntegerField()
    filter_group = models.ForeignKey('FilterGroup', db_column = 'filter_group_id')

    class Meta:
        verbose_name_plural = 'Filters' 
        app_label='api'
        managed = False
        db_table = 'filters'

    def __unicode__(self):
        return u'%s - Context: %s, Name: %s' % (self.id, self.context_id, self.display_name)

    def __repr__(self):
        return u'%s - Context: %s, Name: %s' % (self.id, self.context_id, self.display_name)

class Gift(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'gift_id' )
    assoc_type = models.SmallIntegerField()
    assoc_id = models.BigIntegerField()
    status = models.IntegerField()
    gift_type = models.SmallIntegerField()
    gift_assoc_id = models.BigIntegerField()
    buyer_first_name = models.CharField(max_length=40)
    buyer_middle_name = models.CharField(max_length=40, blank=True, null=True)
    buyer_last_name = models.CharField(max_length=90)
    buyer_email = models.CharField(max_length=90)
    buyer_user = models.ForeignKey('User', blank=True, null=True, related_name = "buyer", db_column = 'buyer_user_id')
    recipient_first_name = models.CharField(max_length=40)
    recipient_middle_name = models.CharField(max_length=40, blank=True, null=True)
    recipient_last_name = models.CharField(max_length=90)
    recipient_email = models.CharField(max_length=90)
    recipient_user = models.ForeignKey('User', blank=True, null=True, related_name = "recipient", db_column = 'recipient_user_id')
    date_redeemed = models.DateTimeField(blank=True, null=True)
    locale = models.CharField(max_length=5)
    gift_note_title = models.CharField(max_length=90, blank=True, null=True)
    gift_note = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Gifts' 
        app_label='api'
        managed = False
        db_table = 'gifts'
    
    def __unicode__(self):
        return u'%s - Type: %s, From: %s %s, To: %s %s' % (self.id, self.gift_type, self.buyer_first_name, self.buyer_last_name, self.recipient_first_name, self.recipient_last_name)

    def __repr__(self):
        return u'%s - Type: %s, From: %s %s, To: %s %s' % (self.id, self.gift_type, self.buyer_first_name, self.buyer_last_name, self.recipient_first_name, self.recipient_last_name)

class GroupMembership(models.Model):
    user = models.OneToOneField('User', db_column = 'user_id', primary_key = True )
    group = models.OneToOneField('Group', db_column = 'group_id', primary_key = True )
    about_displayed = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'GroupMemberships' 
        app_label='api'
        managed = False
        db_table = 'group_memberships'
        unique_together = (('user', 'group'),)
    
    def __unicode__(self):
        return u'User: %s %s - Group: %s, Seq: %s' % (self.user.first_name, self.user.last_name, self.group.id, self.seq)

    def __repr__(self):
        return u'User: %s %s - Group: %s, Seq: %s' % (self.user.first_name, self.user.last_name, self.group.id, self.seq)


class GroupSetting(models.Model):
    group = models.OneToOneField('Group', db_column = 'group_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'GroupSettings' 
        app_label='api'
        managed = False
        db_table = 'group_settings'
        unique_together = (('group', 'locale', 'setting_name'),)
    
    def __unicode__(self):
        return u'Group: %s - Setting: %s (%s)' % (self.group.id, self.setting_name, self.locale)

    def __repr__(self):
        return u'Group: %s - Setting: %s (%s)' % (self.group.id, self.setting_name, self.locale)

class Group(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'group_id' )
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    publish_email = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    context = models.BigIntegerField(blank=True, null=True)
    about_displayed = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'Groups' 
        app_label='api'
        managed = False
        db_table = 'groups'

    def __unicode__(self):
        return u'%s, Assoc (ID: %s, Type: %s), Seq: %s' % (self.id, self.assoc_id, self.assoc_type, self.seq)

    def __repr__(self):
        return u'%s, Assoc (ID: %s, Type: %s), Seq: %s' % (self.id, self.assoc_id, self.assoc_type, self.seq)


class InstitutionalSubscriptionIP(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'institutional_subscription_ip_id' )
    subscription_id = models.BigIntegerField()
    ip_string = models.CharField(max_length=40)
    ip_start = models.BigIntegerField()
    ip_end = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'InstitutionalSubscriptionIPs' 
        app_label='api'
        managed = False
        db_table = 'institutional_subscription_ip'

    def __unicode__(self):
        return u'%s, Subscription: %s, IP: %s' % (self.id, self.subscription_id, self.ip_string)

    def __repr__(self):
        return u'%s, Subscription: %s, IP: %s' % (self.id, self.subscription_id, self.ip_string)


class InstitutionalSubscription(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'institutional_subscription_id' )
    subscription_id = models.BigIntegerField()
    institution_name = models.CharField(max_length=255)
    mailing_address = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'InstitutionalSubscriptions' 
        app_label='api'
        managed = False
        db_table = 'institutional_subscriptions'

    def __unicode__(self):
        return u'%s, Subscription: %s, Institution: %s' % (self.id, self.subscription_id, self.institution_name)

    def __repr__(self):
        return u'%s, Subscription: %s, Institution: %s' % (self.id, self.subscription_id, self.institution_name)

class IssueFile(models.Model):
    id = models.AutoField(primary_key = True, db_column = 'file_id' )
    issue = models.ForeignKey('Issue', db_column = 'issue_id')
    file_name = models.CharField(max_length=90)
    file_type = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    content_type = models.BigIntegerField()
    original_file_name = models.CharField(max_length=127, blank=True, null=True)
    date_uploaded = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'IssueFiles' 
        app_label='api'
        managed = False
        db_table = 'issue_files'

    def __unicode__(self):
        return u'%s, Issue: %s, Name: %s' % (self.id, self.issue.id, self.original_file_name)

    def __repr__(self):
        return u'%s, Issue: %s, Name: %s' % (self.id, self.issue.id, self.original_file_name)

class IssueGalleySetting(models.Model):
    galley = models.OneToOneField('IssueGalley', db_column = 'galley_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'IssueGalleySettings' 
        app_label='api'
        managed = False
        db_table = 'issue_galley_settings'
        unique_together = (('galley', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'%s, Issue Galley: %s, Setting: %s' % (self.pk, self.galley.id, self.setting_name)

    def __repr__(self):
        return u'%s, Issue Galley: %s, Setting: %s' % (self.pk, self.galley.id, self.setting_name)

class IssueGalley(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'galley_id' )
    locale = models.CharField(max_length=5, blank=True, null=True)
    issue = models.ForeignKey('Issue', db_column = 'issue_id')
    file = models.ForeignKey('IssueFile', db_column = "file_id")
    label = models.CharField(max_length=32, blank=True, null=True)
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'IssueGalleys' 
        app_label='api'
        managed = False
        db_table = 'issue_galleys'

    def __unicode__(self):
        return u'%s, Issue: %s, Seq: %s' % (self.id, self.issue.id, self.seq)

    def __repr__(self):
        return u'%s, Issue: %s, Seq: %s' % (self.id, self.issue.id, self.seq)

class IssueSetting(models.Model):
    issue = models.ForeignKey('Issue', db_column = 'issue_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'IssueSettings' 
        app_label='api'
        managed = False
        db_table = 'issue_settings'
        unique_together = (('issue', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'%s, Issue: %s, Setting: %s' % (self.pk, self.issue.id, self.setting_name)

    def __repr__(self):
        return u'%s, Issue: %s, Setting: %s' % (self.pk, self.issue.id, self.setting_name)
        
class DeletedIssue(models.Model):
    id = models.IntegerField(primary_key = True)
    journal = models.BigIntegerField()
    volume = models.SmallIntegerField(blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    published = models.IntegerField()
    current = models.IntegerField()
    date_published = models.DateTimeField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    access_status = models.IntegerField()
    open_access_date = models.DateTimeField(blank=True, null=True)
    show_volume = models.IntegerField()
    show_number = models.IntegerField()
    show_year = models.IntegerField()
    show_title = models.IntegerField()
    style_file_name = models.CharField(max_length=90, blank=True, null=True)
    original_style_file_name = models.CharField(max_length=255, blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return u'%s, Journal: %s' % (self.id, self.journal.id)

    def __repr__(self):
        return u'%s, Journal: %s' % (self.id, self.journal.id)
class Issue(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'issue_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    volume = models.SmallIntegerField(blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    published = models.IntegerField()
    current = models.IntegerField()
    date_published = models.DateTimeField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    access_status = models.IntegerField()
    open_access_date = models.DateTimeField(blank=True, null=True)
    show_volume = models.IntegerField()
    show_number = models.IntegerField()
    show_year = models.IntegerField()
    show_title = models.IntegerField()
    style_file_name = models.CharField(max_length=90, blank=True, null=True)
    original_style_file_name = models.CharField(max_length=255, blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Issues' 
        app_label='api'
        managed = False
        db_table = 'issues'

    def is_deleted(self):
        deleted=False
        delete_issue = DeletedIssue.objects.filter(id=self.id)
        if delete_issue:
            deleted=True
        return deleted

    def __unicode__(self):
        return u'%s, Journal: %s' % (self.id, self.journal.id)

    def __repr__(self):
        return u'%s, Journal: %s' % (self.id, self.journal.id)

class JournalSetting(models.Model):
    journal = models.ForeignKey('Journal', db_column='journal_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'JournalSettings' 
        app_label='api'
        managed = False
        db_table = 'journal_settings'
        unique_together = (('journal', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'Journal: %s, Setting: %s (%s)' % (self.journal.id, self.setting_name, self.locale)

    def __repr__(self):
        return u'Journal: %s, Setting: %s (%s)' % (self.journal.id, self.setting_name, self.locale)

class Journal(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'journal_id' )
    path = models.CharField(unique=True, max_length=32)
    seq = models.FloatField()
    primary_locale = models.CharField(max_length=5)
    enabled = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Journals' 
        app_label='api'
        managed = False
        db_table = 'journals'

    def __unicode__(self):
        return u'%s - Path: %s, Seq: %s' % (self.id, self.path, self.seq)

    def __repr__(self):
        return u'%s - Path: %s, Seq: %s' % (self.id, self.path, self.seq)

class License(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    pretty_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Licenses' 
        app_label='api'
        managed = False
        db_table = 'licenses'

    def __unicode__(self):
        return u'%s - %s' % (self.pk, self.pretty_name)

    def __repr__(self):
        return u'%s - %s' % (self.pk, self.pretty_name)

class MetadataDescriptionSetting(models.Model):
    metadata_description = models.OneToOneField('MetadataDescription', db_column = 'metadata_description_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'MetadataDescriptionSettings' 
        app_label='api'
        managed = False
        db_table = 'metadata_description_settings'
        unique_together = (('metadata_description', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'%s - %s (%s)' % (self.pk, self.setting_name, self.locale)

    def __repr__(self):
        return u'%s - %s (%s)' % (self.pk, self.setting_name, self.locale)

class MetadataDescription(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'metadata_description_id' )
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    schema_namespace = models.CharField(max_length=255)
    schema_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    seq = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'MetadataDescriptions' 
        app_label='api'
        managed = False
        db_table = 'metadata_descriptions'

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.display_name)

    def __repr__(self):
        return u'%s - %s' % (self.id, self.display_name)

class Metric(models.Model):
    load_id = models.CharField(max_length=255)
    assoc_type = models.BigIntegerField()
    context_id = models.BigIntegerField()
    issue = models.ForeignKey('Issue', blank=True, null=True, db_column = 'issue_id')
    submission_id = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()
    day = models.CharField(max_length=8, blank=True, null=True)
    month = models.CharField(max_length=6, blank=True, null=True)
    file_type = models.IntegerField(blank=True, null=True)
    country_id = models.CharField(max_length=2, blank=True, null=True)
    region = models.SmallIntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    metric_type = models.CharField(max_length=255)
    metric = models.IntegerField(primary_key = True )

    class Meta:
        verbose_name_plural = 'Metrics' 
        app_label='api'
        managed = False
        db_table = 'metrics'

    def __unicode__(self):
        return u'Context: %s, Issue: %s, Submission: %s' % (self.context_id, self.issue.id, self.submission_id)

    def __repr__(self):
        return u'Context: %s, Issue: %s, Submission: %s' % (self.context_id, self.issue.id, self.submission_id)


class Mutex(models.Model):
    i = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name_plural = 'Mutexes' 
        app_label='api'
        managed = False
        db_table = 'mutex'

    def __unicode__(self):
        return u'%s' % (self.i)

    def __repr__(self):
        return u'%s' % (self.i)

class Note(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'note_id' )
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey('User', db_column = 'user_id' )
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    file_id = models.BigIntegerField(blank=True, null=True)
    contents = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Notes' 
        app_label='api'
        managed = False
        db_table = 'notes'

    def __unicode__(self):
        return u'%s - %s , User: %s %s' % (self.id, self.title, self.user.first_name, self.user.last_name)

    def __repr__(self):
        return u'%s - %s , User: %s %s' % (self.id, self.title, self.user.first_name, self.user.last_name)

class NotificationMailList(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'notification_mail_list_id' )
    email = models.CharField(max_length=90, unique = True)
    confirmed = models.IntegerField()
    token = models.CharField(max_length=40)
    context = models.BigIntegerField(unique = True)

    class Meta:
        verbose_name_plural = 'NotificationMailLists' 
        app_label='api'
        managed = False
        db_table = 'notification_mail_list'
        unique_together = (('email', 'context'),)

    def __unicode__(self):
        return u'%s - %s' % (self.id, self.email)

    def __repr__(self):
        return u'%s - %s' % (self.id, self.email)

class NotificationSetting(models.Model):
    notification = models.OneToOneField('Notification', db_column='notification_id',primary_key = True)
    locale = models.CharField(max_length=5,blank=True, null=True, unique=True)
    setting_name = models.CharField(max_length=64, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'NotificationSettings' 
        app_label='api'
        managed = False
        db_table = 'notification_settings'
        unique_together = (('notification', 'locale', 'setting_name'),)

    def __unicode__(self):
        if self.locale:
            return u'Notification: %s - Setting: %s (%s)' % (self.notification.id, self.setting_name, self.locale)
        else:
            return u'Notification: %s - Setting: %s' % (self.notification.id, self.setting_name)

    def __repr__(self):
        if self.locale:
            return u'Notification: %s - Setting: %s (%s)' % (self.notification.id, self.setting_name, self.locale)
        else:
            return u'Notification: %s - Setting: %s' % (self.notification.id, self.setting_name)

class NotificationSubscriptionSetting(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'setting_id' )
    setting_name = models.CharField(max_length=64)
    setting_value = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', db_column = 'user_id' )
    context = models.BigIntegerField()
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'NotificationSubscriptionSettings' 
        app_label='api'
        managed = False
        db_table = 'notification_subscription_settings'
 
    def __unicode__(self):
        return u'%s - Setting: %s, User: %s %s' % (self.id, self.setting_name, self.user.first_name, self.user.last_name)

    def __repr__(self):
        return u'%s - Setting: %s, User: %s %s' % (self.id, self.setting_name, self.user.first_name, self.user.last_name)

class Notification(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'notification_id' )
    context_id = models.BigIntegerField()
    user = models.ForeignKey('User', blank=True, null=True, db_column = 'user_id')
    level = models.BigIntegerField()
    type = models.BigIntegerField()
    date_created = models.DateTimeField()
    date_read = models.DateTimeField(blank=True, null=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Notifications' 
        app_label='api'
        managed = False
        db_table = 'notifications'

    def __unicode__(self):
        return u'%s - Type: %s, User: %s %s' % (self.id, self.type, self.user.first_name, self.user.last_name)

    def __repr__(self):
        return u'%s - Type: %s, User: %s %s' % (self.id, self.type, self.user.first_name, self.user.last_name)

class OaiResumptionToken(models.Model):
    token = models.CharField(primary_key=True, max_length=32)
    expire = models.BigIntegerField()
    record_offset = models.IntegerField()
    params = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'OaiResumptionTokens' 
        app_label='api'
        managed = False
        db_table = 'oai_resumption_tokens'

    def __unicode__(self):
        return u'%s' % (self.token)

    def __repr__(self):
        return u'%s' % (self.token)

class PaypalTransaction(models.Model):
    txn_id = models.CharField(primary_key=True, max_length=17)
    txn_type = models.CharField(max_length=20, blank=True, null=True)
    payer_email = models.CharField(max_length=127, blank=True, null=True)
    receiver_email = models.CharField(max_length=127, blank=True, null=True)
    item_number = models.CharField(max_length=127, blank=True, null=True)
    payment_date = models.CharField(max_length=127, blank=True, null=True)
    payer_id = models.CharField(max_length=13, blank=True, null=True)
    receiver_id = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'PaypalTransactions' 
        app_label='api'
        managed = False
        db_table = 'paypal_transactions'

    def __unicode__(self):
        return u'%s Type: %s Receiver: %s' % (self.txn_id, self.txn_type, self.receiver_email)

    def __repr__(self):
        return u'%s Type: %s Receiver: %s' % (self.txn_id, self.txn_type, self.receiver_email)

class PluginSetting(models.Model):
    plugin_name = models.CharField(max_length=80, primary_key = True)
    locale = models.CharField(max_length=5, unique = True)
    journal = models.ForeignKey('Journal', db_column='journal_id', primary_key = True)
    setting_name = models.CharField(max_length=80, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'PluginSettings' 
        app_label='api'
        managed = False
        db_table = 'plugin_settings'
        unique_together = (('plugin_name', 'locale', 'journal', 'setting_name'),)

    def __unicode__(self):
        if self.locale:
            return u'%s (%s) - Setting: %s' % (self.plugin_name, self.locale, self.setting_name)
        else:
            return u'%s - Setting: %s' % (self.plugin_name, self.setting_name)

    def __repr__(self):
        if self.locale:
            return u'%s (%s) - Setting: %s' % (self.plugin_name, self.locale, self.setting_name)
        else:
            return u'%s - Setting: %s' % (self.plugin_name, self.setting_name)

class Process(models.Model):
    process_id = models.CharField(primary_key=True, max_length=23)
    process_type = models.IntegerField()
    time_started = models.BigIntegerField()
    obliterated = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Processes' 
        app_label='api'
        managed = False
        db_table = 'processes'

    def __unicode__(self):
        return u'%s Type: %s' % (self.process_id, self.process_type)

    def __repr__(self):
        return u'%s Type: %s' % (self.process_id, self.process_type)

class UnPublishedArticle(models.Model):

    id = models.AutoField(primary_key = True)
    article = models.ForeignKey('Article')
    issue = models.ForeignKey('Issue', db_column = 'issue_id')
    seq = models.FloatField()
    access_status = models.IntegerField()

    def __unicode__(self):
        return u'%s Article: %s Issue: %s' % (self.id, self.article.id, self.issue.id)

    def __repr__(self):
        return u'%s Article: %s Issue: %s' % (self.id, self.article.id, self.issue.id)


class PublishedArticle(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'published_article_id' )
    article = models.OneToOneField('Article')
    issue = models.ForeignKey('Issue', db_column = 'issue_id')
    date_published = models.DateTimeField(blank=True, null=True)
    seq = models.FloatField()
    access_status = models.IntegerField()

    class Meta:
        verbose_name_plural = 'PublishedArticles' 
        app_label='api'
        managed = False
        db_table = 'published_articles'

    def __unicode__(self):
        return u'%s Article: %s Issue: %s' % (self.id, self.article.id, self.issue.id)

    def __repr__(self):
        return u'%s Article: %s Issue: %s' % (self.id, self.article.id, self.issue.id)

class QueuedPayment(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'queued_payment_id' )
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    expiry_date = models.DateField(blank=True, null=True)
    payment_data = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'QueuedPayments' 
        app_label='api'
        managed = False
        db_table = 'queued_payments'

    def __unicode__(self):
        return u'%s Created: %s Expiring: %s' % (self.id, self.date_created, self.expiry_date)

    def __repr__(self):
        return u'%s Created: %s Expiring: %s' % (self.id, self.date_created, self.expiry_date)

class ReferralSetting(models.Model):
    referral = models.OneToOneField('Referral', db_column='referral_id', primary_key=True)
    locale = models.CharField(max_length=5, primary_key=True)
    setting_name = models.CharField(max_length=255, primary_key=True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ReferralSettings' 
        app_label='api'
        managed = False
        db_table = 'referral_settings'
        unique_together = (('referral', 'locale', 'setting_name'),)

    def __unicode__(self):
        if self.locale:
            return u'Referral: %s Setting: %s (%s)' % (self.referral.id, self.setting_name, self.locale)
        else:            
            return u'Referral: %s Setting: %s' % (self.referral.id, self.setting_name)

    def __repr__(self):
        if self.locale:
            return u'Referral: %s Setting: %s (%s)' % (self.referral.id, self.setting_name, self.locale)
        else:            
            return u'Referral: %s Setting: %s' % (self.referral.id, self.setting_name)

class Referral(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'referral_id' )
    article = models.OneToOneField('Article', db_column='article_id', unique=True)
    status = models.SmallIntegerField()
    url = models.CharField(max_length=255, unique=True)
    date_added = models.DateTimeField()
    link_count = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'Referrals' 
        app_label='api'
        managed = False
        db_table = 'referrals'
        unique_together = (('article', 'url'),)

    def __unicode__(self):
        return u'%s Article: %s' % (self.id, self.article.id)

    def __repr__(self):
        return u'%s Article: %s' % (self.id, self.article.id)


class ReviewAssignment(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'review_id' )
    submission_id = models.BigIntegerField()
    reviewer = models.ForeignKey('User', db_column = 'reviewer_id')
    competing_interests = models.TextField(blank=True, null=True)
    regret_message = models.TextField(blank=True, null=True)
    recommendation = models.IntegerField(blank=True, null=True)
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    date_confirmed = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    date_acknowledged = models.DateTimeField(blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    date_response_due = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    reminder_was_automatic = models.IntegerField()
    declined = models.IntegerField()
    replaced = models.IntegerField()
    cancelled = models.IntegerField()
    reviewer_file_id = models.BigIntegerField(blank=True, null=True)
    date_rated = models.DateTimeField(blank=True, null=True)
    date_reminded = models.DateTimeField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    review_method = models.IntegerField()
    round = models.IntegerField()
    step = models.IntegerField()
    review_form = models.ForeignKey('ReviewForm',blank=True, null=True, db_column = 'review_form_id')
    review_round = models.ForeignKey('ReviewRound', blank=True, null=True, db_column = 'review_round_id')
    stage_id = models.IntegerField()
    unconsidered = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ReviewAssignments' 
        app_label='api'
        managed = False
        db_table = 'review_assignments'

    def __unicode__(self):
        return u'%s - Submission: %s , Stage: %s' % (self.id, self.submission_id, self.stage_id)

    def __repr__(self):
        return u'%s - Submission: %s , Stage: %s' % (self.id, self.submission_id, self.stage_id)

class ReviewFormElementSetting(models.Model):
    review_form_element = models.ForeignKey('ReviewFormElement', db_column = 'review_form_element_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ReviewFormElementSettings' 
        app_label='api'
        managed = False
        db_table = 'review_form_element_settings'
        unique_together = (('review_form_element', 'locale', 'setting_name'),)

    def __unicode__(self):
        if self.locale:
            return u'Element: %s Setting: %s (%s)' % (self.review_form_element.id, self.setting_name, self.locale)
        else:
            return u'Element: %s Setting: %s' % (self.review_form_element.id, self.setting_name)

    def __repr__(self):
        if self.locale:
            return u'Element: %s Setting: %s (%s)' % (self.review_form_element.id, self.setting_name, self.locale)
        else:
            return u'Element: %s Setting: %s' % (self.review_form_element.id, self.setting_name)

class ReviewFormElement(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'review_form_element_id' )
    review_form = models.ForeignKey('ReviewForm', db_column = 'review_form_id')
    seq = models.FloatField(blank=True, null=True)
    element_type = models.BigIntegerField(blank=True, null=True)
    required = models.IntegerField(blank=True, null=True)
    included = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ReviewFormElements' 
        app_label='api'
        managed = False
        db_table = 'review_form_elements'

    def __unicode__(self):
        return u'%s - Review form: %s' % (self.id, self.review_form.id)

    def __repr__(self):
        return u'%s - Review form: %s' % (self.id, self.review_form.id)

class ReviewFormResponse(models.Model):
    review_form_element = models.ForeignKey('ReviewFormElement', db_column = 'review_form_element_id', primary_key=True)
    review = models.OneToOneField('ReviewAssignment', db_column='review_id', primary_key=True)
    response_type = models.CharField(max_length=6, blank=True, null=True)
    response_value = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ReviewFormResponses' 
        app_label='api'
        managed = False
        db_table = 'review_form_responses'

    def __unicode__(self):
        return u'Assignment:%s - Element: %s' % (self.review.id, self.review_form_element.id)

    def __repr__(self):
        return u'Assignment:%s - Element: %s' % (self.review.id, self.review_form_element.id)

class ReviewFormSetting(models.Model):
    review_form = models.ForeignKey('ReviewForm', db_column = 'review_form_id', primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ReviewFormSettings' 
        app_label='api'
        managed = False
        db_table = 'review_form_settings'
        unique_together = (('review_form', 'locale', 'setting_name'),)

    def __unicode__(self):
        if self.locale:
            return u'Form: %s - Setting: %s (%s)' % (self.review_form.id, self.setting_name, self.locale)
        else:
            return u'Form: %s - Setting: %s' % (self.review_form.id, self.setting_name)

    def __repr__(self):
        if self.locale:
            return u'Form: %s - Setting: %s (%s)' % (self.review_form.id, self.setting_name, self.locale)
        else:
            return u'Form: %s - Setting: %s' % (self.review_form.id, self.setting_name)

class ReviewForm(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'review_form_id' )
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    seq = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ReviewForms' 
        app_label='api'
        managed = False
        db_table = 'review_forms'

    def __unicode__(self):
        return u'%s - Assoc (ID: %s, Type: %s)' % (self.id, self.assoc_id, self.assoc_type)

    def __repr__(self):
        return u'%s - Assoc (ID: %s, Type: %s)' % (self.id, self.assoc_id, self.assoc_type)

class ReviewRound(models.Model):
    submission_id = models.BigIntegerField()
    round = models.IntegerField()
    review_revision = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key = True, db_column = 'review_round_id' )
    stage_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ReviewRounds' 
        app_label='api'
        managed = False
        db_table = 'review_rounds'
   
    def __unicode__(self):
        return u'%s - Submission: %s Round: %s' % (self.id, self.submission_id, self.round)

    def __repr__(self):
        return u'%s - Submission: %s Round: %s' % (self.id, self.submission_id, self.round)


class Role(models.Model):
    journal = models.OneToOneField('Journal', db_column='journal_id')
    user = models.OneToOneField('User', db_column = 'user_id')
    id = models.IntegerField( primary_key = True, db_column = 'role_id' )

    class Meta:
        verbose_name_plural = 'Roles' 
        app_label='api'
        managed = False
        db_table = 'roles'
        unique_together = (('journal', 'user', 'id'),)
   
    def __unicode__(self):
        return u'Journal: %s - User: %s %s - Role: %s' % (self.journal.id, self.user.first_name, self.user.last_name, self.id)

    def __repr__(self):
        return u'Journal: %s - User: %s %s - Role: %s' % (self.journal.id, self.user.first_name, self.user.last_name, self.id)

class RtContext(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'context_id' )
    version = models.ForeignKey('RtVersion', db_column = 'version_id')
    title = models.CharField(max_length=120)
    abbrev = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    cited_by = models.IntegerField()
    author_terms = models.IntegerField()
    define_terms = models.IntegerField()
    geo_terms = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'RtContexts' 
        app_label='api'
        managed = False
        db_table = 'rt_contexts'

    def __unicode__(self):
        return u'%s - Title: %s Version %s' % (self.id, self.title, self.version)

    def __repr__(self):
        return u'%s - Title: %s Version %s' % (self.id, self.title, self.version)


class RtSearch(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'search_id' )
    context = models.ForeignKey('RtContext', db_column = 'context_id')
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    search_url = models.TextField(blank=True, null=True)
    search_post = models.TextField(blank=True, null=True)
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'RtSearches' 
        app_label='api'
        managed = False
        db_table = 'rt_searches'

    def __unicode__(self):
        return u'%s - Title: %s Context: %s' % (self.id, self.title, self.context.title)

    def __repr__(self):
        return u'%s - Title: %s Context: %s' % (self.id, self.title, self.context.title)

class RtVersion(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'version_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    version_key = models.CharField(max_length=40)
    locale = models.CharField(max_length=5, blank=True, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'RtVersions' 
        app_label='api'
        managed = False
        db_table = 'rt_versions'

    def __unicode__(self):
        return u'%s - Journal: %s Title: %s' % (self.id, self.journal.id, self.title)

    def __repr__(self):
        return u'%s - Journal: %s Title: %s' % (self.id, self.journal.id, self.title)

class ScheduledTask(models.Model):
    class_name = models.CharField(unique=True, max_length=255, primary_key = True)
    last_run = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ScheduledTasks' 
        app_label='api'
        managed = False
        db_table = 'scheduled_tasks'

    def __unicode__(self):
        return u'%s' % (self.class_name)

    def __repr__(self):
        return u'%s' % (self.class_name)

class SectionEditor(models.Model):
    journal = models.OneToOneField('Journal', db_column='journal_id', primary_key = True)
    section = models.OneToOneField('Section', db_column = 'section_id', primary_key = True)
    user = models.OneToOneField('User', db_column = 'user_id', primary_key = True)
    can_edit = models.IntegerField()
    can_review = models.IntegerField()

    class Meta:
        verbose_name_plural = 'SectionEditors' 
        app_label='api'
        managed = False
        db_table = 'section_editors'
        unique_together = (('journal', 'section', 'user'),)

    def __unicode__(self):
        return u'Journal: %s Section: %s - User: %s %s' % (self.journal.id, self.section.id, self.user.first_name, self.user.last_name)

    def __repr__(self):
        return u'Journal: %s Section: %s - User: %s %s' % (self.journal.id, self.section.id, self.user.first_name, self.user.last_name)

class SectionSetting(models.Model):
    section = models.ForeignKey('Section', db_column = 'section_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'SectionSettings' 
        app_label='api'
        managed = False
        db_table = 'section_settings'
        unique_together = (('section', 'locale', 'setting_name'),)

    def __unicode__(self):
        if self.locale:
            return u'Section: %s - Setting: %s (%s)' % (self.section.id, self.setting_name, self.locale)
        else:
            return u'Section: %s - Setting: %s' % (self.section.id, self.setting_name)

    def __repr__(self):
        if self.locale:
            return u'Section: %s - Setting: %s (%s)' % (self.section.id, self.setting_name, self.locale)
        else:
            return u'Section: %s - Setting: %s' % (self.section.id, self.setting_name)

class Section(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'section_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    review_form = models.ForeignKey('ReviewForm', blank=True, null=True, db_column = 'review_form_id')
    seq = models.FloatField(default=0.0)
    editor_restricted = models.IntegerField(default=0)
    meta_indexed = models.IntegerField(default=0)
    meta_reviewed = models.IntegerField(default=0)
    abstracts_not_required = models.IntegerField(default=0)
    hide_title = models.IntegerField(default=0)
    hide_author = models.IntegerField(default=0)
    hide_about = models.IntegerField(default=0)
    disable_comments = models.IntegerField(default=0)
    abstract_word_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Sections' 
        app_label='api'
        managed = False
        db_table = 'sections'

    def is_deleted(self):
        deleted=False
        delete_section = DeletedSection.objects.filter(id=self.id)
        if delete_section:
            deleted=True
        return deleted

    def __unicode__(self):
        return u'%s - Journal: %s' % (self.id, self.journal.id)

    def __repr__(self):
        return u'%s - Journal: %s' % (self.id, self.journal.id)

class DeletedSection(models.Model):
    id = models.IntegerField(primary_key = True)
    journal = models.ForeignKey('Journal')
    review_form = models.ForeignKey('ReviewForm', blank=True, null=True)
    seq = models.FloatField(default=0.0)
    editor_restricted = models.IntegerField(default=0)
    meta_indexed = models.IntegerField(default=0)
    meta_reviewed = models.IntegerField(default=0)
    abstracts_not_required = models.IntegerField(default=0)
    hide_title = models.IntegerField(default=0)
    hide_author = models.IntegerField(default=0)
    hide_about = models.IntegerField(default=0)
    disable_comments = models.IntegerField(default=0)
    abstract_word_count = models.BigIntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s - Journal: %s' % (self.id, self.journal.id)

    def __repr__(self):
        return u'%s - Journal: %s' % (self.id, self.journal.id)


class Session(models.Model):
    id = models.CharField(primary_key=True, max_length=40, db_column="session_id")
    user = models.ForeignKey('User', blank=True, null=True, db_column = 'user_id')
    ip_address = models.CharField(max_length=39)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    created = models.BigIntegerField()
    last_used = models.BigIntegerField()
    remember = models.IntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Sessions' 
        app_label='api'
        managed = False
        db_table = 'sessions'

    def __unicode__(self):
        if self.user:
            return u'%s - User: %s %s IP: %s' % (self.id, self.user.first_name, self.user.last_name, self.ip_address)
        else:
            return u'%s - IP: %s' % (self.id, self.ip_address)

    def __repr__(self):
        if self.user:
            return u'%s - User: %s %s IP: %s' % (self.id, self.user.first_name, self.user.last_name, self.ip_address)
        else:
            return u'%s - IP: %s' % (self.id, self.ip_address)

class Signoff(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'signoff_id' )
    symbolic = models.CharField(max_length=32, unique = True)
    assoc_type = models.BigIntegerField(unique = True)
    assoc_id = models.BigIntegerField(unique = True)
    user = models.OneToOneField('User', db_column = 'user_id')
    file = models.OneToOneField('IssueFile', db_column='file_id',unique = True)
    file_revision = models.BigIntegerField(unique = True)
    date_notified = models.DateTimeField(blank=True, null=True)
    date_underway = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    date_acknowledged = models.DateTimeField(blank=True, null=True)
    user_group = models.OneToOneField('Group', db_column = 'user_group_id',unique = True)

    class Meta:
        verbose_name_plural = 'Signoffs' 
        app_label='api'
        managed = False
        db_table = 'signoffs'
        unique_together = (('assoc_type', 'assoc_id', 'symbolic', 'user', 'user_group', 'file', 'file_revision'),)

    def __unicode__(self):
        if self.user:
            return u'%s - User: %s %s' % (self.id, self.user.first_name, self.user.last_name)
        else:
            return u'%s' % (self.id)

    def __repr__(self):
        if self.user:
            return u'%s - User: %s %s' % (self.id, self.user.first_name, self.user.last_name)
        else:
            return u'%s' % (self.id)

class Site(models.Model):
    redirect = models.BigIntegerField(primary_key = True)
    primary_locale = models.CharField(max_length=5, primary_key = True)
    min_password_length = models.IntegerField(primary_key = True)
    installed_locales = models.CharField(max_length=255, primary_key = True)
    supported_locales = models.CharField(max_length=255, blank=True, null=True, unique =True)
    original_style_file_name = models.CharField(max_length=255, blank=True, null=True, unique =True)

    class Meta:
        verbose_name_plural = 'Sites' 
        app_label='api'
        managed = False
        db_table = 'site'
        unique_together = (('redirect', 'primary_locale', 'min_password_length', 'installed_locales', 'supported_locales', 'original_style_file_name'),)

    def __unicode__(self):
        return u'Primary locale: %s - Redirect: %s' % (self.primary_locale, self.redirect)

    def __repr__(self):
        return u'Primary locale: %s - Redirect: %s' % (self.primary_locale, self.redirect)


class SiteSetting(models.Model):
    setting_name = models.CharField(max_length=255, primary_key = True)
    locale = models.CharField(max_length=5, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'SiteSettings' 
        app_label='api'
        managed = False
        db_table = 'site_settings'
        unique_together = (('setting_name', 'locale'),)

    def __unicode__(self):
        if self.locale:
            return u'Setting: %s (%s)' % (self.setting_name, self.locale)
        else:
            return u'Setting: %s' % (self.setting_name)

    def __repr__(self):
        if self.locale:
            return u'Setting: %s (%s)' % (self.setting_name, self.locale)
        else:
            return u'Setting: %s' % (self.setting_name)

class StaticPageSetting(models.Model):
    static_page = models.OneToOneField('StaticPage', db_column = 'static_page_id')
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'StaticPageSettings' 
        app_label='api'
        managed = False
        db_table = 'static_page_settings'
        unique_together = (('static_page', 'locale', 'setting_name'),)

    def __unicode__(self):
        return u'Page: %s Setting: %s (%s)' % (self.static_page.id, self.setting_name, self.locale)

    def __repr__(self):
        return u'Page: %s Setting: %s (%s)' % (self.static_page.id, self.setting_name, self.locale)

class StaticPage(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'static_page_id' )
    path = models.CharField(max_length=255)
    journal = models.ForeignKey('Journal', db_column='journal_id')

    class Meta:
        verbose_name_plural = 'StaticPages' 
        app_label='api'
        managed = False
        db_table = 'static_pages'

    def __unicode__(self):
        return u'%s - Path: %s, Journal: %s' % (self.id, self.path, self.journal.id)

    def __repr__(self):
        return u'%s - Path: %s, Journal: %s' % (self.id, self.path, self.journal.id)

class SubscriptionTypeSetting(models.Model):
    type = models.OneToOneField('SubscriptionType', db_column='type_id')
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'SubscriptionTypeSettings' 
        app_label='api'
        managed = False
        db_table = 'subscription_type_settings'
        unique_together = (('type', 'locale', 'setting_name'),)

    def __unicode__(self):
        if self.locale:
            return u'Type: %s - Setting: %s (%s)' % (self.type.id, self.setting_name, self.locale)
        else:
            return u'Type: %s - Setting: %s' % (self.type.id, self.setting_name)

    def __repr__(self):
        if self.locale:
            return u'Type: %s - Setting: %s (%s)' % (self.type.id, self.setting_name, self.locale)
        else:
            return u'Type: %s - Setting: %s' % (self.type.id, self.setting_name)

class SubscriptionType(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'type_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    cost = models.FloatField()
    currency_code_alpha = models.CharField(max_length=3)
    non_expiring = models.IntegerField()
    duration = models.SmallIntegerField(blank=True, null=True)
    format = models.SmallIntegerField()
    institutional = models.IntegerField()
    membership = models.IntegerField()
    disable_public_display = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'SubscriptionTypes' 
        app_label='api'
        managed = False
        db_table = 'subscription_types'

    def __unicode__(self):
        return u'%s - Cost: %f, Journal: %s' % (self.id, self.cost, self.journal.id)

    def __repr__(self):
        return u'%s - Cost: %f, Journal: %s' % (self.id, self.cost, self.journal.id)

class Subscription(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'subscription_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    user = models.ForeignKey('User', db_column = 'user_id' )
    type = models.ForeignKey('AnnouncementType', db_column='type_id')
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    membership = models.CharField(max_length=40, blank=True, null=True)
    reference_number = models.CharField(max_length=40, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Subscriptions' 
        app_label='api'
        managed = False
        db_table = 'subscriptions'
   
    def __unicode__(self):
        return u'%s - Type: %s, Journal: %s' % (self.id, self.type.id, self.journal.id)

    def __repr__(self):
        return u'%s - Type: %s, Journal: %s' % (self.id, self.type.id, self.journal.id)

class Taxonomy(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    front_end = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Taxonomies' 
        app_label='api'
        managed = False
        db_table = 'taxonomy'

    def __unicode__(self):
        return u'%s - Name: %s' % (self.pk, self.name)

    def __repr__(self):
        return u'%s - Name: %s' % (self.pk, self.name)

class TaxonomyArticle(models.Model):
    taxonomy = models.ForeignKey('Taxonomy', db_column = 'taxonomy_id')
    article = models.ForeignKey('Article', db_column = 'article_id')

    class Meta:
        verbose_name_plural = 'TaxonomyArticles' 
        app_label='api'
        managed = False
        db_table = 'taxonomy_article'
   
    def __unicode__(self):
        return u'%s - Taxonomy: %s, Article: %s' % (self.pk, self.taxonomy.name, self.article.id)

    def __repr__(self):
        return u'%s - Taxonomy: %s, Article: %s' % (self.pk, self.taxonomy.name, self.article.id)

class TaxonomyEditor(models.Model):
    taxonomy = models.ForeignKey('Taxonomy', db_column = 'taxonomy_id')
    user = models.ForeignKey('User', db_column = 'user_id')

    class Meta:
        verbose_name_plural = 'TaxonomyEditors' 
        app_label='api'
        managed = False
        db_table = 'taxonomy_editor'
   
    def __unicode__(self):
        return u'%s - Taxonomy: %s, Editor: %s %s' % (self.pk, self.taxonomy.name, self.user.first_name, self.user.last_name)

    def __repr__(self):
        return u'%s - Taxonomy: %s, Editor: %s %s' % (self.pk, self.taxonomy.name, self.user.first_name, self.user.last_name)

class TemporaryFile(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'file_id' )
    user = models.ForeignKey('User', db_column = 'user_id' )
    file_name = models.CharField(max_length=90)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.BigIntegerField()
    original_file_name = models.CharField(max_length=127, blank=True, null=True)
    date_uploaded = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'TemporaryFiles' 
        app_label='api'
        managed = False
        db_table = 'temporary_files'
    
    def __unicode__(self):
        return u'%s - %s, User: %s %s' % (self.id, self.file_name, self.user.first_name, self.user.last_name)

    def __repr__(self):
        return u'%s - %s, User: %s %s' % (self.id, self.file_name, self.user.first_name, self.user.last_name)

class Thesis(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'thesis_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    status = models.SmallIntegerField()
    degree = models.SmallIntegerField()
    degree_name = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    date_approved = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    student_first_name = models.CharField(max_length=40)
    student_middle_name = models.CharField(max_length=40, blank=True, null=True)
    student_last_name = models.CharField(max_length=90)
    student_email = models.CharField(max_length=90)
    student_email_publish = models.IntegerField(blank=True, null=True)
    student_bio = models.TextField(blank=True, null=True)
    supervisor_first_name = models.CharField(max_length=40)
    supervisor_middle_name = models.CharField(max_length=40, blank=True, null=True)
    supervisor_last_name = models.CharField(max_length=90)
    supervisor_email = models.CharField(max_length=90)
    discipline = models.CharField(max_length=255, blank=True, null=True)
    subject_class = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    coverage_geo = models.CharField(max_length=255, blank=True, null=True)
    coverage_chron = models.CharField(max_length=255, blank=True, null=True)
    coverage_sample = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    date_submitted = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Theses' 
        app_label='api'
        managed = False
        db_table = 'theses'
    
    def __unicode__(self):
        return u'%s - %s, Journal: %s, University: %s, Degree: %s' % (self.id, self.title, self.journal.id, self.university, self.degree)

    def __repr__(self):
        return u'%s - %s, Journal: %s, University: %s, Degree: %s' % (self.id, self.title, self.journal.id, self.university, self.degree)

class UsageStatsTemporaryRecord(models.Model):
    assoc_id = models.BigIntegerField()
    assoc_type = models.BigIntegerField()
    day = models.BigIntegerField()
    metric = models.BigIntegerField()
    country_id = models.CharField(max_length=2, blank=True, null=True)
    region = models.SmallIntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    load_id = models.CharField(max_length=255)
    file_type = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'UsageStatsTemporaryRecords' 
        app_label='api'
        managed = False
        db_table = 'usage_stats_temporary_records'


class UserInterest(models.Model):
    user = models.ForeignKey('User', db_column = 'user_id', primary_key=True)
    controlled_vocab_entry = models.ForeignKey('ControlledVocabEntry', primary_key=True, db_column ='controlled_vocab_entry_id')

    class Meta:
        verbose_name_plural = 'UserInterests' 
        app_label='api'
        managed = False
        db_table = 'user_interests'
        unique_together = (('user', 'controlled_vocab_entry'),)

    def __unicode__(self):
        return u'%s %s - %s' % (self.user.first_name, self.user.last_name, self.controlled_vocab_entry.id)

    def __repr__(self):
        return u'%s %s - %s' % (self.user.first_name, self.user.last_name, self.controlled_vocab_entry.id)

class UserSetting(models.Model):
    user = models.ForeignKey('User', db_column = 'user_id', primary_key = True )
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    assoc_type = models.BigIntegerField(blank=True, null=True, unique = True)
    assoc_id = models.BigIntegerField(blank=True, null=True, unique = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'UserSettings' 
        app_label='api'
        managed = False
        db_table = 'user_settings'
        unique_together = (('user', 'locale', 'setting_name', 'assoc_type', 'assoc_id'),)

    def __unicode__(self):
        return u'%s %s - %s' % (self.user.first_name, self.user.last_name, self.setting_name)

    def __repr__(self):
        return u'%s %s - %s' % (self.user.first_name, self.user.last_name, self.setting_name)

class Profile(models.Model):
    intersect_user = models.BigIntegerField(db_column = 'intersect_user_id', primary_key = True)
    user = models.BigIntegerField(db_column = 'user_id')
    journal = models.BigIntegerField(db_column = 'journal_id')

    class Meta:
        verbose_name_plural = 'Profiles' 
        app_label='api'
        managed = False
        db_table = 'user_profiles'
        unique_together = (('user', 'journal', 'intersect_user'),)

    def __unicode__(self):
        return u'%s - %s %s (%s)' % (self.intersect_user.username, self.user.first_name, self.user.last_name, self.journal.path)

    def __repr__(self):
        return u'%s - %s %s (%s)' % (self.intersect_user.username, self.user.first_name, self.user.last_name, self.journal.path)


class User(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'user_id' )
    username = models.CharField(unique=True, max_length=200, blank=True, null=True)
    password = models.CharField(max_length=40)
    salutation = models.CharField(max_length=40, blank=True, null=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)
    gender = models.CharField(max_length=1, blank=True, null=True)
    initials = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(unique=True, max_length=90)
    url = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    mailing_address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=90, blank=True, null=True)
    locales = models.CharField(max_length=255, blank=True, null=True)
    date_last_email = models.DateTimeField(blank=True, null=True)
    date_registered = models.DateTimeField()
    date_validated = models.DateTimeField(blank=True, null=True)
    date_last_login = models.DateTimeField()
    must_change_password = models.IntegerField(blank=True, null=True)
    auth_id = models.BigIntegerField(blank=True, null=True)
    auth_str = models.CharField(max_length=255, blank=True, null=True)
    disabled = models.IntegerField()
    disabled_reason = models.TextField(blank=True, null=True)
    suffix = models.CharField(max_length=40, blank=True, null=True)
    billing_address = models.CharField(max_length=255, blank=True, null=True)
    inline_help = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Users' 
        app_label='api'
        managed = False
        db_table = 'users'

    def __unicode__(self):
        return u'%s - %s %s' % (self.pk, self.first_name, self.last_name)

    def __repr__(self):
        return u'%s - %s %s' % (self.pk, self.first_name, self.last_name)


class Version(models.Model):
    major = models.IntegerField(primary_key = True)
    minor = models.IntegerField(primary_key = True)
    revision = models.IntegerField(primary_key = True)
    build = models.IntegerField(primary_key = True)
    date_installed = models.DateTimeField()
    current = models.IntegerField()
    product_type = models.CharField(max_length=30, blank=True, null=True, unique = True)
    product = models.CharField(max_length=30, blank=True, null=True, unique = True)
    product_class_name = models.CharField(max_length=80, blank=True, null=True)
    lazy_load = models.IntegerField()
    sitewide = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Versions' 
        app_label='api'
        managed = False
        db_table = 'versions'
        unique_together = (('product_type', 'product', 'major', 'minor', 'revision', 'build'),)

    def __unicode__(self):
        return u'%s - Major: %s, Minor: %s, Build: %s, Revision: %s' % (self.product_type, self.major, self.minor, self.build, self.revision)

    def __repr__(self):
        return u'%s - Major: %s, Minor: %s, Build: %s, Revision: %s' % (self.product_type, self.major, self.minor, self.build, self.revision)
