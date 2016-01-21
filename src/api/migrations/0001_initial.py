# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKeys',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='access_key_id')),
                ('context', models.CharField(max_length=40)),
                ('key_hash', models.CharField(max_length=40)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('expiry_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'access_keys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='announcement_id')),
                ('assoc_type', models.SmallIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField()),
                ('date_expire', models.DateTimeField(null=True, blank=True)),
                ('date_posted', models.DateTimeField()),
            ],
            options={
                'db_table': 'announcements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncementSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'announcement_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncementTypes',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='type_id')),
                ('assoc_type', models.SmallIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'announcement_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnnouncementTypeSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'announcement_type_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleComments',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='comment_id')),
                ('comment_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField()),
                ('comment_title', models.CharField(max_length=255)),
                ('comments', models.TextField(null=True, blank=True)),
                ('date_posted', models.DateTimeField(null=True, blank=True)),
                ('date_modified', models.DateTimeField(null=True, blank=True)),
                ('viewable', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'article_comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleEventLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='log_id')),
                ('date_logged', models.DateTimeField()),
                ('ip_address', models.CharField(max_length=15)),
                ('log_level', models.CharField(max_length=1, null=True, blank=True)),
                ('event_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'article_event_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleFiles',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='file_id')),
                ('revision', models.BigIntegerField()),
                ('source_revision', models.BigIntegerField(null=True, blank=True)),
                ('file_name', models.CharField(max_length=90)),
                ('file_type', models.CharField(max_length=255)),
                ('file_size', models.BigIntegerField()),
                ('original_file_name', models.CharField(max_length=127, null=True, blank=True)),
                ('file_stage', models.BigIntegerField()),
                ('viewable', models.IntegerField(null=True, blank=True)),
                ('date_uploaded', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('round', models.IntegerField()),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'article_files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleGalleys',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='galley_id')),
                ('locale', models.CharField(max_length=5, null=True, blank=True)),
                ('label', models.CharField(max_length=32, null=True, blank=True)),
                ('html_galley', models.IntegerField()),
                ('seq', models.FloatField()),
                ('remote_url', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'article_galleys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleGalleySettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'article_galley_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleHtmlGalleyImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'article_html_galley_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleNotes',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='note_id')),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'article_notes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='article_id')),
                ('locale', models.CharField(max_length=5, null=True, blank=True)),
                ('section_id', models.BigIntegerField(null=True, blank=True)),
                ('language', models.CharField(max_length=10, null=True, blank=True)),
                ('comments_to_ed', models.TextField(null=True, blank=True)),
                ('citations', models.TextField(null=True, blank=True)),
                ('date_submitted', models.DateTimeField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(null=True, blank=True)),
                ('date_status_modified', models.DateTimeField(null=True, blank=True)),
                ('status', models.IntegerField()),
                ('submission_progress', models.IntegerField()),
                ('current_round', models.IntegerField()),
                ('submission_file_id', models.BigIntegerField(null=True, blank=True)),
                ('revised_file_id', models.BigIntegerField(null=True, blank=True)),
                ('review_file_id', models.BigIntegerField(null=True, blank=True)),
                ('editor_file_id', models.BigIntegerField(null=True, blank=True)),
                ('pages', models.CharField(max_length=255, null=True, blank=True)),
                ('fast_tracked', models.IntegerField()),
                ('hide_author', models.IntegerField()),
                ('comments_status', models.IntegerField()),
            ],
            options={
                'db_table': 'articles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleSearchKeywordList',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='keyword_id')),
                ('keyword_text', models.CharField(unique=True, max_length=60)),
            ],
            options={
                'db_table': 'article_search_keyword_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleSearchObjectKeywords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword_id', models.BigIntegerField()),
                ('pos', models.IntegerField()),
            ],
            options={
                'db_table': 'article_search_object_keywords',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleSearchObjects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='object_id')),
                ('type', models.IntegerField()),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'article_search_objects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'article_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleStages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stage_id', models.IntegerField(null=True, blank=True)),
                ('stage_name', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'article_stages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleStatus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column='status_id')),
                ('date_updated', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'article_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleStatusHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'article_status_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleSuppFileSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'article_supp_file_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleSupplementaryFiles',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='supp_id')),
                ('type', models.CharField(max_length=255, null=True, blank=True)),
                ('language', models.CharField(max_length=10, null=True, blank=True)),
                ('remote_url', models.CharField(max_length=255, null=True, blank=True)),
                ('date_created', models.DateField(null=True, blank=True)),
                ('show_reviewers', models.IntegerField(null=True, blank=True)),
                ('date_submitted', models.DateTimeField()),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'article_supplementary_files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleXmlGalleys',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='xml_galley_id')),
                ('label', models.CharField(max_length=32)),
                ('galley_type', models.CharField(max_length=255)),
                ('views', models.IntegerField()),
            ],
            options={
                'db_table': 'article_xml_galleys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='author_id')),
                ('submission_id', models.BigIntegerField()),
                ('primary_contact', models.IntegerField()),
                ('seq', models.FloatField()),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40, null=True, blank=True)),
                ('last_name', models.CharField(max_length=90)),
                ('country', models.CharField(max_length=90, null=True, blank=True)),
                ('email', models.CharField(max_length=90)),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('suffix', models.CharField(max_length=40, null=True, blank=True)),
            ],
            options={
                'db_table': 'authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthorSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'author_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthSources',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='auth_id')),
                ('title', models.CharField(max_length=60)),
                ('plugin', models.CharField(max_length=32)),
                ('auth_default', models.IntegerField()),
                ('settings', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'auth_sources',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksForReview',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='book_id')),
                ('status', models.SmallIntegerField()),
                ('author_type', models.SmallIntegerField()),
                ('publisher', models.CharField(max_length=255)),
                ('year', models.SmallIntegerField()),
                ('language', models.CharField(max_length=10)),
                ('copy', models.IntegerField()),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('edition', models.IntegerField(null=True, blank=True)),
                ('pages', models.SmallIntegerField(null=True, blank=True)),
                ('isbn', models.CharField(max_length=30, null=True, blank=True)),
                ('date_created', models.DateTimeField()),
                ('date_requested', models.DateTimeField(null=True, blank=True)),
                ('date_assigned', models.DateTimeField(null=True, blank=True)),
                ('date_mailed', models.DateTimeField(null=True, blank=True)),
                ('date_due', models.DateTimeField(null=True, blank=True)),
                ('date_submitted', models.DateTimeField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'books_for_review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksForReviewAuthors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.FloatField()),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40, null=True, blank=True)),
                ('last_name', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'books_for_review_authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BooksForReviewSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'books_for_review_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Captchas',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='captcha_id')),
                ('session_id', models.CharField(max_length=40)),
                ('value', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField()),
            ],
            options={
                'db_table': 'captchas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Citations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='citation_id')),
                ('assoc_type', models.BigIntegerField()),
                ('assoc_id', models.BigIntegerField()),
                ('citation_state', models.BigIntegerField()),
                ('raw_citation', models.TextField(null=True, blank=True)),
                ('seq', models.BigIntegerField()),
                ('lock_id', models.CharField(max_length=23, null=True, blank=True)),
            ],
            options={
                'db_table': 'citations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CitationSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'citation_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='collection_id')),
                ('name', models.CharField(max_length=150)),
                ('abbrev', models.CharField(max_length=150)),
                ('short_description', models.TextField(null=True, blank=True)),
                ('description', models.TextField()),
                ('image_filename', models.CharField(max_length=150, null=True, blank=True)),
                ('date_published', models.DateField()),
                ('date_updated', models.DateField(null=True, blank=True)),
                ('tba', models.TextField(null=True, blank=True)),
                ('disabled', models.TextField(null=True, blank=True)),
                ('discussions', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'collection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CollectionArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'collection_article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CollectionUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'collection_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='comment_id')),
                ('submission_id', models.BigIntegerField()),
                ('num_children', models.IntegerField()),
                ('poster_ip', models.CharField(max_length=15)),
                ('poster_name', models.CharField(max_length=90, null=True, blank=True)),
                ('poster_email', models.CharField(max_length=90, null=True, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(null=True, blank=True)),
                ('date_posted', models.DateTimeField(null=True, blank=True)),
                ('date_modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompletedPayments',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='completed_payment_id')),
                ('timestamp', models.DateTimeField()),
                ('payment_type', models.BigIntegerField()),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('amount', models.FloatField()),
                ('currency_code_alpha', models.CharField(max_length=3, null=True, blank=True)),
                ('payment_method_plugin_name', models.CharField(max_length=80, null=True, blank=True)),
            ],
            options={
                'db_table': 'completed_payments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ControlledVocabEntries',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='controlled_vocab_entry_id')),
                ('seq', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'controlled_vocab_entries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ControlledVocabEntrySettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'controlled_vocab_entry_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ControlledVocabs',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='controlled_vocab_id')),
                ('symbolic', models.CharField(max_length=64)),
                ('assoc_type', models.BigIntegerField()),
                ('assoc_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'controlled_vocabs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomIssueOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'custom_issue_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomSectionOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_id', models.BigIntegerField()),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'custom_section_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataObjectTombstoneOaiSetObjects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='object_id')),
                ('assoc_type', models.BigIntegerField()),
                ('assoc_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'data_object_tombstone_oai_set_objects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataObjectTombstones',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='tombstone_id')),
                ('data_object_id', models.BigIntegerField()),
                ('date_deleted', models.DateTimeField()),
                ('set_spec', models.CharField(max_length=255)),
                ('set_name', models.CharField(max_length=255)),
                ('oai_identifier', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'data_object_tombstones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataObjectTombstoneSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'data_object_tombstone_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataverseFiles',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='dvfile_id')),
                ('supp_id', models.BigIntegerField()),
                ('submission_id', models.BigIntegerField()),
                ('study_id', models.BigIntegerField()),
                ('content_source_uri', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'dataverse_files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataverseStudies',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='study_id')),
                ('submission_id', models.BigIntegerField()),
                ('edit_uri', models.CharField(max_length=255)),
                ('edit_media_uri', models.CharField(max_length=255)),
                ('statement_uri', models.CharField(max_length=255)),
                ('persistent_uri', models.CharField(max_length=255)),
                ('data_citation', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'dataverse_studies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DraftDecisions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key_val', models.CharField(max_length=45)),
                ('decision', models.IntegerField()),
                ('subject', models.CharField(max_length=200, null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('attatchment', models.TextField(null=True, blank=True)),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'draft_decisions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EditAssignments',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='edit_id')),
                ('can_edit', models.IntegerField()),
                ('can_review', models.IntegerField()),
                ('date_assigned', models.DateTimeField(null=True, blank=True)),
                ('date_notified', models.DateTimeField(null=True, blank=True)),
                ('date_underway', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'edit_assignments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EditDecisions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='edit_decision_id')),
                ('round', models.IntegerField()),
                ('decision', models.IntegerField()),
                ('date_decided', models.DateTimeField()),
            ],
            options={
                'db_table': 'edit_decisions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='log_id')),
                ('date_sent', models.DateTimeField()),
                ('ip_address', models.CharField(max_length=39, null=True, blank=True)),
                ('event_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('from_address', models.CharField(max_length=255, null=True, blank=True)),
                ('recipients', models.TextField(null=True, blank=True)),
                ('cc_recipients', models.TextField(null=True, blank=True)),
                ('bcc_recipients', models.TextField(null=True, blank=True)),
                ('subject', models.CharField(max_length=255, null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'email_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailLogUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'email_log_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailTemplates',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='email_id')),
                ('email_key', models.CharField(max_length=64)),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('enabled', models.IntegerField()),
            ],
            options={
                'db_table': 'email_templates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailTemplatesData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_key', models.CharField(max_length=64)),
                ('locale', models.CharField(max_length=5)),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('subject', models.CharField(max_length=120)),
                ('body', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'email_templates_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailTemplatesDefault',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='email_id')),
                ('email_key', models.CharField(max_length=64)),
                ('can_disable', models.IntegerField()),
                ('can_edit', models.IntegerField()),
            ],
            options={
                'db_table': 'email_templates_default',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailTemplatesDefaultData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_key', models.CharField(max_length=64)),
                ('locale', models.CharField(max_length=5)),
                ('subject', models.CharField(max_length=120)),
                ('body', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'email_templates_default_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='log_id')),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('date_logged', models.DateTimeField()),
                ('ip_address', models.CharField(max_length=39)),
                ('event_type', models.BigIntegerField(null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('is_translated', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'event_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventLogSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'event_log_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExternalFeeds',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='feed_id')),
                ('url', models.CharField(max_length=255)),
                ('seq', models.FloatField()),
                ('display_homepage', models.IntegerField()),
                ('display_block', models.SmallIntegerField()),
                ('limit_items', models.IntegerField(null=True, blank=True)),
                ('recent_items', models.SmallIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'external_feeds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExternalFeedSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'external_feed_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilterGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='filter_group_id')),
                ('symbolic', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('display_name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('input_type', models.CharField(max_length=255, null=True, blank=True)),
                ('output_type', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'filter_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Filters',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='filter_id')),
                ('context_id', models.BigIntegerField()),
                ('display_name', models.CharField(max_length=255, null=True, blank=True)),
                ('class_name', models.CharField(max_length=255, null=True, blank=True)),
                ('is_template', models.IntegerField()),
                ('seq', models.BigIntegerField()),
            ],
            options={
                'db_table': 'filters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilterSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'filter_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='gift_id')),
                ('assoc_type', models.SmallIntegerField()),
                ('assoc_id', models.BigIntegerField()),
                ('status', models.IntegerField()),
                ('gift_type', models.SmallIntegerField()),
                ('gift_assoc_id', models.BigIntegerField()),
                ('buyer_first_name', models.CharField(max_length=40)),
                ('buyer_middle_name', models.CharField(max_length=40, null=True, blank=True)),
                ('buyer_last_name', models.CharField(max_length=90)),
                ('buyer_email', models.CharField(max_length=90)),
                ('recipient_first_name', models.CharField(max_length=40)),
                ('recipient_middle_name', models.CharField(max_length=40, null=True, blank=True)),
                ('recipient_last_name', models.CharField(max_length=90)),
                ('recipient_email', models.CharField(max_length=90)),
                ('date_redeemed', models.DateTimeField(null=True, blank=True)),
                ('locale', models.CharField(max_length=5)),
                ('gift_note_title', models.CharField(max_length=90, null=True, blank=True)),
                ('gift_note', models.TextField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'gifts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupMemberships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about_displayed', models.IntegerField()),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'group_memberships',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='group_id')),
                ('assoc_type', models.SmallIntegerField(null=True, blank=True)),
                ('publish_email', models.SmallIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('context', models.BigIntegerField(null=True, blank=True)),
                ('about_displayed', models.IntegerField()),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'group_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InstitutionalSubscriptionIp',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='institutional_subscription_ip_id')),
                ('subscription_id', models.BigIntegerField()),
                ('ip_string', models.CharField(max_length=40)),
                ('ip_start', models.BigIntegerField()),
                ('ip_end', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'institutional_subscription_ip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InstitutionalSubscriptions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='institutional_subscription_id')),
                ('subscription_id', models.BigIntegerField()),
                ('institution_name', models.CharField(max_length=255)),
                ('mailing_address', models.CharField(max_length=255, null=True, blank=True)),
                ('domain', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'institutional_subscriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IssueFiles',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='file_id')),
                ('file_name', models.CharField(max_length=90)),
                ('file_type', models.CharField(max_length=255)),
                ('file_size', models.BigIntegerField()),
                ('content_type', models.BigIntegerField()),
                ('original_file_name', models.CharField(max_length=127, null=True, blank=True)),
                ('date_uploaded', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
            ],
            options={
                'db_table': 'issue_files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IssueGalleys',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='galley_id')),
                ('locale', models.CharField(max_length=5, null=True, blank=True)),
                ('label', models.CharField(max_length=32, null=True, blank=True)),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'issue_galleys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IssueGalleySettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'issue_galley_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='issue_id')),
                ('volume', models.SmallIntegerField(null=True, blank=True)),
                ('number', models.CharField(max_length=10, null=True, blank=True)),
                ('year', models.SmallIntegerField(null=True, blank=True)),
                ('published', models.IntegerField()),
                ('current', models.IntegerField()),
                ('date_published', models.DateTimeField(null=True, blank=True)),
                ('date_notified', models.DateTimeField(null=True, blank=True)),
                ('access_status', models.IntegerField()),
                ('open_access_date', models.DateTimeField(null=True, blank=True)),
                ('show_volume', models.IntegerField()),
                ('show_number', models.IntegerField()),
                ('show_year', models.IntegerField()),
                ('show_title', models.IntegerField()),
                ('style_file_name', models.CharField(max_length=90, null=True, blank=True)),
                ('original_style_file_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'issues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IssueSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'issue_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Journals',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='journal_id')),
                ('path', models.CharField(unique=True, max_length=32)),
                ('seq', models.FloatField()),
                ('primary_locale', models.CharField(max_length=5)),
                ('enabled', models.IntegerField()),
            ],
            options={
                'db_table': 'journals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JournalSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'journal_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('pretty_name', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('enabled', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'licenses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetadataDescriptions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='metadata_description_id')),
                ('assoc_type', models.BigIntegerField()),
                ('assoc_id', models.BigIntegerField()),
                ('schema_namespace', models.CharField(max_length=255)),
                ('schema_name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255, null=True, blank=True)),
                ('seq', models.BigIntegerField()),
            ],
            options={
                'db_table': 'metadata_descriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetadataDescriptionSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'metadata_description_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('load_id', models.CharField(max_length=255)),
                ('assoc_type', models.BigIntegerField()),
                ('context_id', models.BigIntegerField()),
                ('submission_id', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField()),
                ('day', models.CharField(max_length=8, null=True, blank=True)),
                ('month', models.CharField(max_length=6, null=True, blank=True)),
                ('file_type', models.IntegerField(null=True, blank=True)),
                ('country_id', models.CharField(max_length=2, null=True, blank=True)),
                ('region', models.SmallIntegerField(null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('metric_type', models.CharField(max_length=255)),
                ('metric', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'metrics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mutex',
            fields=[
                ('i', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'mutex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='note_id')),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField(null=True, blank=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('file_id', models.BigIntegerField(null=True, blank=True)),
                ('contents', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'notes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationMailList',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='notification_mail_list_id')),
                ('email', models.CharField(max_length=90)),
                ('confirmed', models.IntegerField()),
                ('token', models.CharField(max_length=40)),
                ('context', models.BigIntegerField()),
            ],
            options={
                'db_table': 'notification_mail_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='notification_id')),
                ('context_id', models.BigIntegerField()),
                ('level', models.BigIntegerField()),
                ('type', models.BigIntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_read', models.DateTimeField(null=True, blank=True)),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'notifications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5, null=True, blank=True)),
                ('setting_name', models.CharField(max_length=64)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'notification_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationSubscriptionSettings',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='setting_id')),
                ('setting_name', models.CharField(max_length=64)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('context', models.BigIntegerField()),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'notification_subscription_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OaiResumptionTokens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(unique=True, max_length=32)),
                ('expire', models.BigIntegerField()),
                ('record_offset', models.IntegerField()),
                ('params', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'oai_resumption_tokens',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaypalTransactions',
            fields=[
                ('txn_id', models.CharField(max_length=17, serialize=False, primary_key=True)),
                ('txn_type', models.CharField(max_length=20, null=True, blank=True)),
                ('payer_email', models.CharField(max_length=127, null=True, blank=True)),
                ('receiver_email', models.CharField(max_length=127, null=True, blank=True)),
                ('item_number', models.CharField(max_length=127, null=True, blank=True)),
                ('payment_date', models.CharField(max_length=127, null=True, blank=True)),
                ('payer_id', models.CharField(max_length=13, null=True, blank=True)),
                ('receiver_id', models.CharField(max_length=13, null=True, blank=True)),
            ],
            options={
                'db_table': 'paypal_transactions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PluginSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plugin_name', models.CharField(max_length=80)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=80)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'plugin_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Processes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('process_id', models.CharField(unique=True, max_length=23)),
                ('process_type', models.IntegerField()),
                ('time_started', models.BigIntegerField()),
                ('obliterated', models.IntegerField()),
            ],
            options={
                'db_table': 'processes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PublishedArticles',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='published_article_id')),
                ('date_published', models.DateTimeField(null=True, blank=True)),
                ('seq', models.FloatField()),
                ('access_status', models.IntegerField()),
            ],
            options={
                'db_table': 'published_articles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QueuedPayments',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='queued_payment_id')),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('expiry_date', models.DateField(null=True, blank=True)),
                ('payment_data', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'queued_payments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Referrals',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='referral_id')),
                ('status', models.SmallIntegerField()),
                ('url', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField()),
                ('link_count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'referrals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReferralSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'referral_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewAssignments',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='review_id')),
                ('submission_id', models.BigIntegerField()),
                ('competing_interests', models.TextField(null=True, blank=True)),
                ('regret_message', models.TextField(null=True, blank=True)),
                ('recommendation', models.IntegerField(null=True, blank=True)),
                ('date_assigned', models.DateTimeField(null=True, blank=True)),
                ('date_notified', models.DateTimeField(null=True, blank=True)),
                ('date_confirmed', models.DateTimeField(null=True, blank=True)),
                ('date_completed', models.DateTimeField(null=True, blank=True)),
                ('date_acknowledged', models.DateTimeField(null=True, blank=True)),
                ('date_due', models.DateTimeField(null=True, blank=True)),
                ('date_response_due', models.DateTimeField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(null=True, blank=True)),
                ('reminder_was_automatic', models.IntegerField()),
                ('declined', models.IntegerField()),
                ('replaced', models.IntegerField()),
                ('cancelled', models.IntegerField()),
                ('reviewer_file_id', models.BigIntegerField(null=True, blank=True)),
                ('date_rated', models.DateTimeField(null=True, blank=True)),
                ('date_reminded', models.DateTimeField(null=True, blank=True)),
                ('quality', models.IntegerField(null=True, blank=True)),
                ('review_method', models.IntegerField()),
                ('round', models.IntegerField()),
                ('step', models.IntegerField()),
                ('stage_id', models.IntegerField()),
                ('unconsidered', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'review_assignments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewFormElements',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='review_form_element_id')),
                ('seq', models.FloatField(null=True, blank=True)),
                ('element_type', models.BigIntegerField(null=True, blank=True)),
                ('required', models.IntegerField(null=True, blank=True)),
                ('included', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'review_form_elements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewFormElementSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'review_form_element_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewFormResponses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response_type', models.CharField(max_length=6, null=True, blank=True)),
                ('response_value', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'review_form_responses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewForms',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='review_form_id')),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('seq', models.FloatField(null=True, blank=True)),
                ('is_active', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'review_forms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewFormSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'review_form_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewRounds',
            fields=[
                ('submission_id', models.BigIntegerField()),
                ('round', models.IntegerField()),
                ('review_revision', models.BigIntegerField(null=True, blank=True)),
                ('status', models.BigIntegerField(null=True, blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='review_round_id')),
                ('stage_id', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'review_rounds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='role_id')),
            ],
            options={
                'db_table': 'roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RtContexts',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='context_id')),
                ('title', models.CharField(max_length=120)),
                ('abbrev', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
                ('cited_by', models.IntegerField()),
                ('author_terms', models.IntegerField()),
                ('define_terms', models.IntegerField()),
                ('geo_terms', models.IntegerField()),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'rt_contexts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RtSearches',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='search_id')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
                ('url', models.TextField(null=True, blank=True)),
                ('search_url', models.TextField(null=True, blank=True)),
                ('search_post', models.TextField(null=True, blank=True)),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'rt_searches',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RtVersions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='version_id')),
                ('version_key', models.CharField(max_length=40)),
                ('locale', models.CharField(max_length=5, null=True, blank=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'rt_versions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ScheduledTasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(unique=True, max_length=255)),
                ('last_run', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'scheduled_tasks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SectionEditors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('can_edit', models.IntegerField()),
                ('can_review', models.IntegerField()),
            ],
            options={
                'db_table': 'section_editors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='section_id')),
                ('seq', models.FloatField()),
                ('editor_restricted', models.IntegerField()),
                ('meta_indexed', models.IntegerField()),
                ('meta_reviewed', models.IntegerField()),
                ('abstracts_not_required', models.IntegerField()),
                ('hide_title', models.IntegerField()),
                ('hide_author', models.IntegerField()),
                ('hide_about', models.IntegerField()),
                ('disable_comments', models.IntegerField()),
                ('abstract_word_count', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sections',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SectionSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'section_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.CharField(max_length=40, serialize=False, primary_key=True, db_column='session_id')),
                ('ip_address', models.CharField(max_length=39)),
                ('user_agent', models.CharField(max_length=255, null=True, blank=True)),
                ('created', models.BigIntegerField()),
                ('last_used', models.BigIntegerField()),
                ('remember', models.IntegerField()),
                ('data', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sessions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Signoffs',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='signoff_id')),
                ('symbolic', models.CharField(max_length=32)),
                ('assoc_type', models.BigIntegerField()),
                ('assoc_id', models.BigIntegerField()),
                ('file_revision', models.BigIntegerField(null=True, blank=True)),
                ('date_notified', models.DateTimeField(null=True, blank=True)),
                ('date_underway', models.DateTimeField(null=True, blank=True)),
                ('date_completed', models.DateTimeField(null=True, blank=True)),
                ('date_acknowledged', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'signoffs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('redirect', models.BigIntegerField()),
                ('primary_locale', models.CharField(max_length=5)),
                ('min_password_length', models.IntegerField()),
                ('installed_locales', models.CharField(max_length=255)),
                ('supported_locales', models.CharField(max_length=255, null=True, blank=True)),
                ('original_style_file_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('setting_name', models.CharField(max_length=255)),
                ('locale', models.CharField(max_length=5)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'site_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StaticPages',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='static_page_id')),
                ('path', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'static_pages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StaticPageSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'static_page_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='subscription_id')),
                ('date_start', models.DateField(null=True, blank=True)),
                ('date_end', models.DateTimeField(null=True, blank=True)),
                ('status', models.IntegerField()),
                ('membership', models.CharField(max_length=40, null=True, blank=True)),
                ('reference_number', models.CharField(max_length=40, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'subscriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionTypes',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='type_id')),
                ('cost', models.FloatField()),
                ('currency_code_alpha', models.CharField(max_length=3)),
                ('non_expiring', models.IntegerField()),
                ('duration', models.SmallIntegerField(null=True, blank=True)),
                ('format', models.SmallIntegerField()),
                ('institutional', models.IntegerField()),
                ('membership', models.IntegerField()),
                ('disable_public_display', models.IntegerField()),
                ('seq', models.FloatField()),
            ],
            options={
                'db_table': 'subscription_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionTypeSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'subscription_type_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('note', models.TextField(null=True, blank=True)),
                ('front_end', models.IntegerField()),
            ],
            options={
                'db_table': 'taxonomy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxonomyArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'taxonomy_article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxonomyEditor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'taxonomy_editor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TemporaryFiles',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='file_id')),
                ('file_name', models.CharField(max_length=90)),
                ('file_type', models.CharField(max_length=255, null=True, blank=True)),
                ('file_size', models.BigIntegerField()),
                ('original_file_name', models.CharField(max_length=127, null=True, blank=True)),
                ('date_uploaded', models.DateTimeField()),
            ],
            options={
                'db_table': 'temporary_files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Theses',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='thesis_id')),
                ('status', models.SmallIntegerField()),
                ('degree', models.SmallIntegerField()),
                ('degree_name', models.CharField(max_length=255, null=True, blank=True)),
                ('department', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('date_approved', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('url', models.TextField(null=True, blank=True)),
                ('abstract', models.TextField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('student_first_name', models.CharField(max_length=40)),
                ('student_middle_name', models.CharField(max_length=40, null=True, blank=True)),
                ('student_last_name', models.CharField(max_length=90)),
                ('student_email', models.CharField(max_length=90)),
                ('student_email_publish', models.IntegerField(null=True, blank=True)),
                ('student_bio', models.TextField(null=True, blank=True)),
                ('supervisor_first_name', models.CharField(max_length=40)),
                ('supervisor_middle_name', models.CharField(max_length=40, null=True, blank=True)),
                ('supervisor_last_name', models.CharField(max_length=90)),
                ('supervisor_email', models.CharField(max_length=90)),
                ('discipline', models.CharField(max_length=255, null=True, blank=True)),
                ('subject_class', models.CharField(max_length=255, null=True, blank=True)),
                ('subject', models.CharField(max_length=255, null=True, blank=True)),
                ('coverage_geo', models.CharField(max_length=255, null=True, blank=True)),
                ('coverage_chron', models.CharField(max_length=255, null=True, blank=True)),
                ('coverage_sample', models.CharField(max_length=255, null=True, blank=True)),
                ('method', models.CharField(max_length=255, null=True, blank=True)),
                ('language', models.CharField(max_length=10, null=True, blank=True)),
                ('date_submitted', models.DateTimeField()),
            ],
            options={
                'db_table': 'theses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsageStatsTemporaryRecords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assoc_id', models.BigIntegerField()),
                ('assoc_type', models.BigIntegerField()),
                ('day', models.BigIntegerField()),
                ('metric', models.BigIntegerField()),
                ('country_id', models.CharField(max_length=2, null=True, blank=True)),
                ('region', models.SmallIntegerField(null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('load_id', models.CharField(max_length=255)),
                ('file_type', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'usage_stats_temporary_records',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInterests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('controlled_vocab_entry_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'user_interests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column='user_id')),
                ('username', models.CharField(max_length=200, unique=True, null=True, blank=True)),
                ('password', models.CharField(max_length=40)),
                ('salutation', models.CharField(max_length=40, null=True, blank=True)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40, null=True, blank=True)),
                ('last_name', models.CharField(max_length=90)),
                ('gender', models.CharField(max_length=1, null=True, blank=True)),
                ('initials', models.CharField(max_length=5, null=True, blank=True)),
                ('email', models.CharField(unique=True, max_length=90)),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=24, null=True, blank=True)),
                ('fax', models.CharField(max_length=24, null=True, blank=True)),
                ('mailing_address', models.CharField(max_length=255, null=True, blank=True)),
                ('country', models.CharField(max_length=90, null=True, blank=True)),
                ('locales', models.CharField(max_length=255, null=True, blank=True)),
                ('date_last_email', models.DateTimeField(null=True, blank=True)),
                ('date_registered', models.DateTimeField()),
                ('date_validated', models.DateTimeField(null=True, blank=True)),
                ('date_last_login', models.DateTimeField()),
                ('must_change_password', models.IntegerField(null=True, blank=True)),
                ('auth_id', models.BigIntegerField(null=True, blank=True)),
                ('auth_str', models.CharField(max_length=255, null=True, blank=True)),
                ('disabled', models.IntegerField()),
                ('disabled_reason', models.TextField(null=True, blank=True)),
                ('suffix', models.CharField(max_length=40, null=True, blank=True)),
                ('billing_address', models.CharField(max_length=255, null=True, blank=True)),
                ('inline_help', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(max_length=5)),
                ('setting_name', models.CharField(max_length=255)),
                ('assoc_type', models.BigIntegerField(null=True, blank=True)),
                ('assoc_id', models.BigIntegerField(null=True, blank=True)),
                ('setting_value', models.TextField(null=True, blank=True)),
                ('setting_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'user_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Versions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('major', models.IntegerField()),
                ('minor', models.IntegerField()),
                ('revision', models.IntegerField()),
                ('build', models.IntegerField()),
                ('date_installed', models.DateTimeField()),
                ('current', models.IntegerField()),
                ('product_type', models.CharField(max_length=30, null=True, blank=True)),
                ('product', models.CharField(max_length=30, null=True, blank=True)),
                ('product_class_name', models.CharField(max_length=80, null=True, blank=True)),
                ('lazy_load', models.IntegerField()),
                ('sitewide', models.IntegerField()),
            ],
            options={
                'db_table': 'versions',
                'managed': False,
            },
        ),
    ]
