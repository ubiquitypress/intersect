# intersect
Intersect is an API for Open Journal Systems, written in Python with Django.
# Table Alterations
- Article Settings : id (auto_increment, primary key)
- Issue Settings : id (auto_increment, primary key)
- Journal Settings : id (auto_increment, primary key)
- Author Settings : id (auto_increment, primary key)
- Section Settings : id (auto_increment, primary key)
- UsageStatsTemporaryRecord : id (auto_increment, primary key)
- user_profiles table : foreignkey ids :intersect_user (auth_users) [PK] + journal (Journals) + user (users)


SQL COMMANDS FOR TABLE ALTERATIONS:


  ALTER TABLE issue_settings add `id` int(11) unsigned NOT NULL AUTO_INCREMENT, ADD CONSTRAINT PRIMARY KEY (`id`);

  ALTER TABLE section_settings add `id` int(11) unsigned NOT NULL AUTO_INCREMENT, ADD CONSTRAINT PRIMARY KEY (`id`);

  ALTER TABLE article_settings add `id` int(11) unsigned NOT NULL AUTO_INCREMENT, ADD CONSTRAINT PRIMARY KEY (`id`);

  ALTER TABLE journal_settings add `id` int(11) unsigned NOT NULL AUTO_INCREMENT, ADD CONSTRAINT PRIMARY KEY (`id`);

  ALTER TABLE author_settings add `id` int(11) unsigned NOT NULL AUTO_INCREMENT, ADD CONSTRAINT PRIMARY KEY (`id`);


  SQL IF TABLES ARE NOT CREATED:

CREATE TABLE `api_deletedarticle` (
  `id` int(11) NOT NULL,
  `locale` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user` bigint(20) NOT NULL,
  `journal` bigint(20) NOT NULL,
  `section_id` bigint(20) DEFAULT NULL,
  `language` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `comments_to_ed` longtext COLLATE utf8_unicode_ci,
  `citations` longtext COLLATE utf8_unicode_ci,
  `date_submitted` datetime(6) DEFAULT NULL,
  `last_modified` datetime(6) DEFAULT NULL,
  `date_status_modified` datetime(6) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `submission_progress` int(11) NOT NULL,
  `current_round` int(11) NOT NULL,
  `submission_file_id` bigint(20) DEFAULT NULL,
  `revised_file_id` bigint(20) DEFAULT NULL,
  `review_file_id` bigint(20) DEFAULT NULL,
  `editor_file_id` bigint(20) DEFAULT NULL,
  `pages` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fast_tracked` int(11) NOT NULL,
  `hide_author` int(11) NOT NULL,
  `comments_status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `api_deletedauthor` (
  `id` int(11) NOT NULL,
  `primary_contact` int(11) NOT NULL,
  `seq` double NOT NULL,
  `first_name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `middle_name` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_name` varchar(90) COLLATE utf8_unicode_ci NOT NULL,
  `country` varchar(90) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(90) COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `suffix` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `deleted_article` bigint(20) DEFAULT NULL,
  `user_group` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `api_deletedissue` (
  `id` int(11) NOT NULL,
  `journal` bigint(20) NOT NULL,
  `volume` smallint(6) DEFAULT NULL,
  `number` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `year` smallint(6) DEFAULT NULL,
  `published` int(11) NOT NULL,
  `current` int(11) NOT NULL,
  `date_published` datetime(6) DEFAULT NULL,
  `date_notified` datetime(6) DEFAULT NULL,
  `access_status` int(11) NOT NULL,
  `open_access_date` datetime(6) DEFAULT NULL,
  `show_volume` int(11) NOT NULL,
  `show_number` int(11) NOT NULL,
  `show_year` int(11) NOT NULL,
  `show_title` int(11) NOT NULL,
  `style_file_name` varchar(90) COLLATE utf8_unicode_ci DEFAULT NULL,
  `original_style_file_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_modified` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `api_deletedsection` (
  `id` int(11) NOT NULL,
  `seq` double NOT NULL,
  `editor_restricted` int(11) NOT NULL,
  `meta_indexed` int(11) NOT NULL,
  `meta_reviewed` int(11) NOT NULL,
  `abstracts_not_required` int(11) NOT NULL,
  `hide_title` int(11) NOT NULL,
  `hide_author` int(11) NOT NULL,
  `hide_about` int(11) NOT NULL,
  `disable_comments` int(11) NOT NULL,
  `abstract_word_count` bigint(20) DEFAULT NULL,
  `journal` bigint(20) NOT NULL,
  `review_form` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `api_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mime_type` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `original_filename` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  `uuid_filename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `label` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` varchar(1000) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date_uploaded` datetime(6) NOT NULL,
  `date_modified` datetime(6) NOT NULL,
  `stage_uploaded` int(11) NOT NULL,
  `kind` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sequence` int(11) NOT NULL,
  `article_file` int(11) NOT NULL,
  `issue_file` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_file_owner_id_6484b6aa2e126aaf_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `api_file_owner_id_6484b6aa2e126aaf_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `api_unpublishedarticle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seq` double NOT NULL,
  `access_status` int(11) NOT NULL,
  `article_id` bigint(20) NOT NULL,
  `issue_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `user_profiles` (
  `intersect_user_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `journal_id` bigint(20) NOT NULL,
  PRIMARY KEY (`intersect_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;