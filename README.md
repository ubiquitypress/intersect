# intersect
Intersect is an API for Open Journal Systems, written in Python with Django.
# Table Alterations
- Article Settings : id (auto_increment, primary key)
- Issue Settings : id (auto_increment, primary key)
- Journal Settings : id (auto_increment, primary key)
- Author Settings : id (auto_increment, primary key)
- UsageStatsTemporaryRecord : id (auto_increment, primary key)
- user_profiles table : foreignkey ids :intersect_user (auth_users) [PK] + journal (Journals) + user (users)