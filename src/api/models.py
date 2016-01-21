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

from django.db import models


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


class AnnouncementSetting(models.Model):
    announcement = models.ForeignKey('Announcement', db_column='announcement_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'AnnouncementSettings' 
        app_label='api'
        managed = False
        db_table = 'announcement_settings'
        unique_together = (('announcement', 'locale', 'setting_name'),)


class AnnouncementTypeSetting(models.Model):
    type = models.OneToOneField('AnnouncementType', db_column='type_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'AnnouncementTypeSettings' 
        app_label='api'
        managed = False
        db_table = 'announcement_type_settings'
        unique_together = (('type', 'locale', 'setting_name'),)


class AnnouncementType(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'type_id' )
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'AnnouncementTypes' 
        app_label='api'
        managed = False
        db_table = 'announcement_types'


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


class ArticleFile(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'file_id' )
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


class ArticleGalleySetting(models.Model):
    galley = models.ForeignKey('ArticleGalley', db_column='galley_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
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


class ArticleHtmlGalleyImage(models.Model):
    galley =  models.ForeignKey('ArticleGalley', db_column='galley_id')
    file = models.ForeignKey('ArticleFile', db_column='file_id')

    class Meta:
        verbose_name_plural = 'ArticleHtmlGalleyImages' 
        app_label='api'
        managed = False
        db_table = 'article_html_galley_images'
        unique_together = (('galley', 'file'),)


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


class ArticleSearchKeywordList(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'keyword_id' )
    keyword_text = models.CharField(unique=True, max_length=60)

    class Meta:
        verbose_name_plural = 'ArticleSearchKeywordLists' 
        app_label='api'
        managed = False
        db_table = 'article_search_keyword_list'


class ArticleSearchObjectKeyword(models.Model):
    object = models.ForeignKey('ArticleSearchObject', db_column='object_id')
    keyword_id = models.BigIntegerField()
    pos = models.IntegerField()

    class Meta:
        verbose_name_plural = 'ArticleSearchObjectKeywords' 
        app_label='api'
        managed = False
        db_table = 'article_search_object_keywords'
        unique_together = (('object', 'pos'),)


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


class ArticleStage(models.Model):
    stage_id = models.IntegerField(blank=True, null=True)
    stage_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleStages' 
        app_label='api'
        managed = False
        db_table = 'article_stages'


class ArticleStatus(models.Model):
    article = models.OneToOneField('Article', db_column = 'article_id')
    id =  models.AutoField(primary_key = True, db_column = 'status_id' )
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ArticleStatuses' 
        app_label='api'
        managed = False
        db_table = 'article_status'


class ArticleStatusHistory(models.Model):
    article = models.ForeignKey('Article', db_column='article_id')
    status = models.ForeignKey('ArticleStatus', db_column='status_id')
    date_updated = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'ArticleStatusHistories' 
        app_label='api'
        managed = False
        db_table = 'article_status_history'


class ArticleSuppFileSetting(models.Model):
    supp = models.ForeignKey('ArticleSupplementaryFile', db_column = 'supp_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ArticleSuppFileSettings' 
        app_label='api'
        managed = False
        db_table = 'article_supp_file_settings'
        unique_together = (('supp', 'locale', 'setting_name'),)


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


class Author(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'author_id' )
    submission_id = models.BigIntegerField()
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


class BooksForReviewAuthor(models.Model):
    author = models.OneToOneField('Author', db_column = 'author_id' )
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


class BooksForReviewSetting(models.Model):
    book = models.ForeignKey('BooksForReview', db_column = 'book_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'BooksForReviewSettings' 
        app_label='api'
        managed = False
        db_table = 'books_for_review_settings'
        unique_together = (('book', 'locale', 'setting_name'),)


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


class CitationSetting(models.Model):
    citation = models.ForeignKey('Citation', db_column = 'citation_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'CitationSettings' 
        app_label='api'
        managed = False
        db_table = 'citation_settings'
        unique_together = (('citation', 'locale', 'setting_name'),)


class Citation(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'citation_id' )
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    citation_state = models.BigIntegerField()
    raw_citation = models.TextField(blank=True, null=True)
    seq = models.BigIntegerField()
    lock_id = models.CharField(max_length=23, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Citations' 
        app_label='api'
        managed = False
        db_table = 'citations'
        unique_together = (('assoc_type', 'assoc_id', 'seq'),)


class Collection(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'collection_id' )
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


class CollectionArticle(models.Model):
    collection = models.ForeignKey('Collection', db_column = 'collection_id')
    published_article = models.ForeignKey('Article', db_column='article_id')

    class Meta:
        verbose_name_plural = 'CollectionArticles' 
        app_label='api'
        managed = False
        db_table = 'collection_article'
        unique_together = (('collection', 'published_article'),)


class CollectionUser(models.Model):
    collection = models.ForeignKey('Collection', db_column = 'collection_id')
    user = models.ForeignKey('User', db_column = 'user_id' )
    role_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'CollectionUsers' 
        app_label='api'
        managed = False
        db_table = 'collection_user'
        unique_together = (('collection', 'user'),)


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


class ControlledVocabEntry(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'controlled_vocab_entry_id' )
    controlled_vocab = models.ForeignKey('ControlledVocab', db_column = 'controlled_vocab_id')
    seq = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ControlledVocabEntries' 
        app_label='api'
        managed = False
        db_table = 'controlled_vocab_entries'


class ControlledVocabEntrySetting(models.Model):
    controlled_vocab_entry = models.ForeignKey('ControlledVocabEntry', db_column = 'controlled_vocab_entry_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ControlledVocabEntrySettings' 
        app_label='api'
        managed = False
        db_table = 'controlled_vocab_entry_settings'
        unique_together = (('controlled_vocab_entry', 'locale', 'setting_name'),)


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


class CustomIssueOrder(models.Model):
    issue = models.OneToOneField('Issue', db_column = 'issue_id')
    journal = models.ForeignKey('Journal', db_column='journal_id')
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'CustomIssueOrders' 
        app_label='api'
        managed = False
        db_table = 'custom_issue_orders'


class CustomSectionOrder(models.Model):
    issue = models.ForeignKey('Issue', db_column = 'issue_id')
    section_id = models.BigIntegerField()
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'CustomSectionOrders' 
        app_label='api'
        managed = False
        db_table = 'custom_section_orders'
        unique_together = (('issue', 'section_id'),)


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


class DataObjectTombstoneSetting(models.Model):
    tombstone = models.ForeignKey('DataObjectTombstone', db_column = 'tombstone_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'DataObjectTombstoneSetting' 
        app_label='api'
        managed = False
        db_table = 'data_object_tombstone_settings'
        unique_together = (('tombstone', 'locale', 'setting_name'),)


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


class EmailLogUser(models.Model):
    email_log = models.ForeignKey('EmailLog', db_column = 'email_log_id')
    user = models.ForeignKey('User', db_column = 'user_id' )

    class Meta:
        verbose_name_plural = 'EmailLogUsers' 
        app_label='api'
        managed = False
        db_table = 'email_log_users'
        unique_together = (('email_log', 'user'),)


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


class EmailTemplatesData(models.Model):
    email_key = models.CharField(max_length=64)
    locale = models.CharField(max_length=5)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'EmailTemplatesDatas' 
        app_label='api'
        managed = False
        db_table = 'email_templates_data'
        unique_together = (('email_key', 'locale', 'assoc_type', 'assoc_id'),)


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


class EmailTemplatesDefaultData(models.Model):
    email_key = models.CharField(max_length=64)
    locale = models.CharField(max_length=5)
    subject = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'EmailTemplatesDefaultDatas' 
        app_label='api'
        managed = False
        db_table = 'email_templates_default_data'
        unique_together = (('email_key', 'locale'),)


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


class EventLogSetting(models.Model):
    event_log = models.ForeignKey('EventLog', db_column = 'log_id' )
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'EventLogSettings' 
        app_label='api'
        managed = False
        db_table = 'event_log_settings'
        unique_together = (('event_log', 'setting_name'),)


class ExternalFeedSetting(models.Model):
    feed = models.ForeignKey('ExternalFeed', db_column='feed_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ExternalFeedSettings' 
        app_label='api'
        managed = False
        db_table = 'external_feed_settings'
        unique_together = (('feed', 'locale', 'setting_name'),)


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


class FilterSetting(models.Model):
    filter = models.ForeignKey('Filter', db_column = 'filter_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'FilterSettings' 
        app_label='api'
        managed = False
        db_table = 'filter_settings'
        unique_together = (('filter', 'locale', 'setting_name'),)


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


class GroupMembership(models.Model):
    user = models.ForeignKey('User', db_column = 'user_id' )
    group = models.ForeignKey('Group', db_column = 'group_id')
    about_displayed = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        verbose_name_plural = 'GroupMemberships' 
        app_label='api'
        managed = False
        db_table = 'group_memberships'
        unique_together = (('user', 'group'),)


class GroupSetting(models.Model):
    group = models.ForeignKey('Group', db_column = 'group_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'GroupSettings' 
        app_label='api'
        managed = False
        db_table = 'group_settings'
        unique_together = (('group', 'locale', 'setting_name'),)


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


class IssueFile(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'file_id' )
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


class IssueGalleySetting(models.Model):
    galley = models.ForeignKey('IssueGalley', db_column = 'galley_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'IssueGalleySettings' 
        app_label='api'
        managed = False
        db_table = 'issue_galley_settings'
        unique_together = (('galley', 'locale', 'setting_name'),)


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


class MetadataDescriptionSetting(models.Model):
    metadata_description = models.ForeignKey('MetadataDescription', db_column = 'metadata_description_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'MetadataDescriptionSettings' 
        app_label='api'
        managed = False
        db_table = 'metadata_description_settings'
        unique_together = (('metadata_description', 'locale', 'setting_name'),)


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
    metric = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Metrics' 
        app_label='api'
        managed = False
        db_table = 'metrics'


class Mutex(models.Model):
    i = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name_plural = 'Mutexes' 
        app_label='api'
        managed = False
        db_table = 'mutex'


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


class NotificationMailList(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'notification_mail_list_id' )
    email = models.CharField(max_length=90)
    confirmed = models.IntegerField()
    token = models.CharField(max_length=40)
    context = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'NotificationMailLists' 
        app_label='api'
        managed = False
        db_table = 'notification_mail_list'
        unique_together = (('email', 'context'),)


class NotificationSetting(models.Model):
    notification = models.ForeignKey('Notification', db_column='notification_id')
    locale = models.CharField(max_length=5, blank=True, null=True)
    setting_name = models.CharField(max_length=64)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'NotificationSettings' 
        app_label='api'
        managed = False
        db_table = 'notification_settings'
        unique_together = (('notification', 'locale', 'setting_name'),)


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


class OaiResumptionToken(models.Model):
    token = models.CharField(unique=True, max_length=32)
    expire = models.BigIntegerField()
    record_offset = models.IntegerField()
    params = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'OaiResumptionTokens' 
        app_label='api'
        managed = False
        db_table = 'oai_resumption_tokens'


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


class PluginSetting(models.Model):
    plugin_name = models.CharField(max_length=80)
    locale = models.CharField(max_length=5)
    journal = models.ForeignKey('Journal', db_column='journal_id')
    setting_name = models.CharField(max_length=80)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'PluginSettings' 
        app_label='api'
        managed = False
        db_table = 'plugin_settings'
        unique_together = (('plugin_name', 'locale', 'journal', 'setting_name'),)


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


class ReferralSetting(models.Model):
    referral = models.ForeignKey('Referral', db_column='referral_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ReferralSettings' 
        app_label='api'
        managed = False
        db_table = 'referral_settings'
        unique_together = (('referral', 'locale', 'setting_name'),)


class Referral(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'referral_id' )
    article = models.ForeignKey('Article', db_column='article_id')
    status = models.SmallIntegerField()
    url = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    link_count = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'Referrals' 
        app_label='api'
        managed = False
        db_table = 'referrals'
        unique_together = (('article', 'url'),)


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


class ReviewFormElementSetting(models.Model):
    review_form_element = models.ForeignKey('ReviewFormElement', db_column = 'review_form_element_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ReviewFormElementSettings' 
        app_label='api'
        managed = False
        db_table = 'review_form_element_settings'
        unique_together = (('review_form_element', 'locale', 'setting_name'),)


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


class ReviewFormResponse(models.Model):
    review_form_element = models.ForeignKey('ReviewFormElement', db_column = 'review_form_element_id')
    review = models.ForeignKey('ReviewAssignment', db_column='review_id')
    response_type = models.CharField(max_length=6, blank=True, null=True)
    response_value = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ReviewFormResponses' 
        app_label='api'
        managed = False
        db_table = 'review_form_responses'


class ReviewFormSetting(models.Model):
    review_form = models.ForeignKey('ReviewForm', db_column = 'review_form_id')
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'ReviewFormSettings' 
        app_label='api'
        managed = False
        db_table = 'review_form_settings'
        unique_together = (('review_form', 'locale', 'setting_name'),)


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
        unique_together = (('submission_id', 'stage_id', 'round'),)


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


class ScheduledTask(models.Model):
    class_name = models.CharField(unique=True, max_length=255)
    last_run = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ScheduledTasks' 
        app_label='api'
        managed = False
        db_table = 'scheduled_tasks'


class SectionEditor(models.Model):
    journal = models.OneToOneField('Journal', db_column='journal_id')
    section = models.OneToOneField('Section', db_column = 'section_id')
    user = models.OneToOneField('User', db_column = 'user_id')
    can_edit = models.IntegerField()
    can_review = models.IntegerField()

    class Meta:
        verbose_name_plural = 'SectionEditors' 
        app_label='api'
        managed = False
        db_table = 'section_editors'
        unique_together = (('journal', 'section', 'user'),)


class SectionSetting(models.Model):
    section = models.OneToOneField('Section', db_column = 'section_id')
    locale = models.CharField(max_length=5, primary_key = True)
    setting_name = models.CharField(max_length=255, primary_key = True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'SectionSettings' 
        app_label='api'
        managed = False
        db_table = 'section_settings'
        unique_together = (('section', 'locale', 'setting_name'),)


class Section(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'section_id' )
    journal = models.ForeignKey('Journal', db_column='journal_id')
    review_form = models.ForeignKey('ReviewForm', blank=True, null=True, db_column = 'review_form_id')
    seq = models.FloatField()
    editor_restricted = models.IntegerField()
    meta_indexed = models.IntegerField()
    meta_reviewed = models.IntegerField()
    abstracts_not_required = models.IntegerField()
    hide_title = models.IntegerField()
    hide_author = models.IntegerField()
    hide_about = models.IntegerField()
    disable_comments = models.IntegerField()
    abstract_word_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Sections' 
        app_label='api'
        managed = False
        db_table = 'sections'


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


class Signoff(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'signoff_id' )
    symbolic = models.CharField(max_length=32, primary_key = True)
    assoc_type = models.BigIntegerField(primary_key = True)
    assoc_id = models.BigIntegerField(primary_key = True)
    user = models.OneToOneField('User', db_column = 'user_id')
    file = models.OneToOneField('IssueFile', db_column='file_id')
    file_revision = models.BigIntegerField(primary_key = True)
    date_notified = models.DateTimeField(blank=True, null=True)
    date_underway = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    date_acknowledged = models.DateTimeField(blank=True, null=True)
    user_group = models.OneToOneField('Group', db_column = 'user_group_id')

    class Meta:
        verbose_name_plural = 'Signoffs' 
        app_label='api'
        managed = False
        db_table = 'signoffs'
        unique_together = (('assoc_type', 'assoc_id', 'symbolic', 'user', 'user_group', 'file', 'file_revision'),)


class Site(models.Model):
    redirect = models.BigIntegerField()
    primary_locale = models.CharField(max_length=5)
    min_password_length = models.IntegerField()
    installed_locales = models.CharField(max_length=255)
    supported_locales = models.CharField(max_length=255, blank=True, null=True)
    original_style_file_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Sites' 
        app_label='api'
        managed = False
        db_table = 'site'


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


class StaticPage(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'static_page_id' )
    path = models.CharField(max_length=255)
    journal = models.ForeignKey('Journal', db_column='journal_id')

    class Meta:
        verbose_name_plural = 'StaticPages' 
        app_label='api'
        managed = False
        db_table = 'static_pages'


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


class Taxonomy(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    front_end = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Taxonomies' 
        app_label='api'
        managed = False
        db_table = 'taxonomy'


class TaxonomyArticle(models.Model):
    taxonomy = models.ForeignKey('Taxonomy', db_column = 'taxonomy_id')
    article = models.ForeignKey('Article', db_column = 'article_id')

    class Meta:
        verbose_name_plural = 'TaxonomyArticles' 
        app_label='api'
        managed = False
        db_table = 'taxonomy_article'


class TaxonomyEditor(models.Model):
    taxonomy = models.ForeignKey('Taxonomy', db_column = 'taxonomy_id')
    user = models.ForeignKey('User', db_column = 'user_id')

    class Meta:
        verbose_name_plural = 'TaxonomyEditors' 
        app_label='api'
        managed = False
        db_table = 'taxonomy_editor'


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
    user = models.ForeignKey('User', db_column = 'user_id' )
    controlled_vocab_entry_id = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'UserInterests' 
        app_label='api'
        managed = False
        db_table = 'user_interests'
        unique_together = (('user', 'controlled_vocab_entry_id'),)


class UserSetting(models.Model):
    user = models.ForeignKey('User', db_column = 'user_id' )
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'UserSettings' 
        app_label='api'
        managed = False
        db_table = 'user_settings'
        unique_together = (('user', 'locale', 'setting_name', 'assoc_type', 'assoc_id'),)


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


class Version(models.Model):
    major = models.IntegerField()
    minor = models.IntegerField()
    revision = models.IntegerField()
    build = models.IntegerField()
    date_installed = models.DateTimeField()
    current = models.IntegerField()
    product_type = models.CharField(max_length=30, blank=True, null=True)
    product = models.CharField(max_length=30, blank=True, null=True)
    product_class_name = models.CharField(max_length=80, blank=True, null=True)
    lazy_load = models.IntegerField()
    sitewide = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Versions' 
        app_label='api'
        managed = False
        db_table = 'versions'
        unique_together = (('product_type', 'product', 'major', 'minor', 'revision', 'build'),)
