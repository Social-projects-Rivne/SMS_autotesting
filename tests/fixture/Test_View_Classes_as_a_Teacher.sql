-- phpMyAdmin SQL Dump
-- version 4.0.10.12
-- http://www.phpmyadmin.net
--
-- Хост: 127.11.47.2:3306
-- Время создания: Май 09 2016 г., 10:06
-- Версия сервера: 5.5.45
-- Версия PHP: 5.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `sms`
--

DROP DATABASE IF EXISTS sms;
CREATE DATABASE IF NOT EXISTS sms CHARACTER SET utf8;
USE sms;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=52 ;

--
-- Дамп данных таблицы `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add teachers', 6, 'add_teachers'),
(17, 'Can change teachers', 6, 'change_teachers'),
(18, 'Can delete teachers', 6, 'delete_teachers'),
(19, 'Can add roles', 7, 'add_roles'),
(20, 'Can change roles', 7, 'change_roles'),
(21, 'Can delete roles', 7, 'delete_roles'),
(22, 'Can add schools', 8, 'add_schools'),
(23, 'Can change schools', 8, 'change_schools'),
(24, 'Can delete schools', 8, 'delete_schools'),
(25, 'Can add subjects', 9, 'add_subjects'),
(26, 'Can change subjects', 9, 'change_subjects'),
(27, 'Can delete subjects', 9, 'delete_subjects'),
(28, 'Can add groups', 10, 'add_groups'),
(29, 'Can change groups', 10, 'change_groups'),
(30, 'Can delete groups', 10, 'delete_groups'),
(31, 'Can add journal', 11, 'add_journal'),
(32, 'Can change journal', 11, 'change_journal'),
(33, 'Can delete journal', 11, 'delete_journal'),
(34, 'Can add lessons', 12, 'add_lessons'),
(35, 'Can change lessons', 12, 'change_lessons'),
(36, 'Can delete lessons', 12, 'delete_lessons'),
(37, 'Can add lesson types', 13, 'add_lessontypes'),
(38, 'Can change lesson types', 13, 'change_lessontypes'),
(39, 'Can delete lesson types', 13, 'delete_lessontypes'),
(40, 'Can add mark types', 14, 'add_marktypes'),
(41, 'Can change mark types', 14, 'change_marktypes'),
(42, 'Can delete mark types', 14, 'delete_marktypes'),
(43, 'Can add students', 15, 'add_students'),
(44, 'Can change students', 15, 'change_students'),
(45, 'Can delete students', 15, 'delete_students'),
(46, 'Can add teacher subjects', 16, 'add_teachersubjects'),
(47, 'Can change teacher subjects', 16, 'change_teachersubjects'),
(48, 'Can delete teacher subjects', 16, 'delete_teachersubjects'),
(49, 'Can add teacher subject groups', 17, 'add_teachersubjectgroups'),
(50, 'Can change teacher subject groups', 17, 'change_teachersubjectgroups'),
(51, 'Can delete teacher subject groups', 17, 'delete_teachersubjectgroups');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=18 ;

--
-- Дамп данных таблицы `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'auth', 'group'),
(1, 'auth', 'permission'),
(3, 'auth', 'user'),
(4, 'contenttypes', 'contenttype'),
(7, 'mainteacher', 'roles'),
(8, 'mainteacher', 'schools'),
(9, 'mainteacher', 'subjects'),
(6, 'mainteacher', 'teachers'),
(5, 'sessions', 'session'),
(10, 'teacher', 'groups'),
(11, 'teacher', 'journal'),
(12, 'teacher', 'lessons'),
(13, 'teacher', 'lessontypes'),
(14, 'teacher', 'marktypes'),
(15, 'teacher', 'students'),
(17, 'teacher', 'teachersubjectgroups'),
(16, 'teacher', 'teachersubjects');

-- --------------------------------------------------------

--
-- Структура таблицы `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=27 ;

--
-- Дамп данных таблицы `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-06-03 19:58:53'),
(2, 'contenttypes', '0002_remove_content_type_name', '2015-06-03 19:58:54'),
(3, 'auth', '0001_initial', '2015-06-03 19:58:57'),
(4, 'auth', '0002_alter_permission_name_max_length', '2015-06-03 19:58:57'),
(5, 'auth', '0003_alter_user_email_max_length', '2015-06-03 19:58:57'),
(6, 'auth', '0004_alter_user_username_opts', '2015-06-03 19:58:57'),
(7, 'auth', '0005_alter_user_last_login_null', '2015-06-03 19:58:58'),
(8, 'auth', '0006_require_contenttypes_0002', '2015-06-03 19:58:58'),
(9, 'mainteacher', '0001_initial', '2015-06-03 19:58:58'),
(10, 'mainteacher', '0002_auto_20150430_2146', '2015-06-03 19:58:58'),
(11, 'mainteacher', '0003_schools_director', '2015-06-03 19:58:59'),
(12, 'mainteacher', '0004_auto_20150501_1353', '2015-06-03 19:59:00'),
(13, 'mainteacher', '0005_auto_20150501_1355', '2015-06-03 19:59:01'),
(14, 'mainteacher', '0006_auto_20150514_2309', '2015-06-03 19:59:01'),
(15, 'mainteacher', '0007_auto_20150530_1404', '2015-06-03 19:59:01'),
(16, 'mainteacher', '0008_auto_20150530_1405', '2015-06-03 19:59:01'),
(17, 'mainteacher', '0009_auto_20150603_2247', '2015-06-03 19:59:01'),
(18, 'sessions', '0001_initial', '2015-06-03 19:59:01'),
(19, 'teacher', '0001_initial', '2015-06-03 19:59:09'),
(20, 'teacher', '0002_auto_20150517_1019', '2015-06-03 19:59:10'),
(21, 'teacher', '0003_auto_20150517_1029', '2015-06-03 19:59:11'),
(22, 'teacher', '0004_auto_20150520_2200', '2015-06-03 19:59:17'),
(23, 'mainteacher', '0010_auto_20150618_1018', '2015-06-24 17:50:35'),
(24, 'mainteacher', '0011_auto_20150618_1042', '2015-06-24 17:50:36'),
(25, 'mainteacher', '0012_auto_20150623_1054', '2015-06-24 17:50:36'),
(26, 'mainteacher', '0013_auto_20150623_2251', '2015-06-24 17:50:37');

-- --------------------------------------------------------

--
-- Структура таблицы `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1fks7wtgnht1yuz88qagurtaqbwufm34', 'YjAzOGFkMzMxNmU0OTkxZjM4ZGE0NTExZTBkNjNhZjU0Y2QwMmEwMDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJDAoRCEewhVJxBHMu', '2016-05-23 09:10:17'),
('204y17r0p67id2z6e8gkyquatx1nclv9', 'YTI5NTFkODgwODcxMzZkZWQ5OGY0MDc4MDhmYmIzNjc4OWJhMGJlOTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJAwsGCb/0hVJxBHMu', '2016-05-23 00:11:06'),
('47cu3poc9lo9mbaggz0ket9oufwyr28h', 'ZTY5NDM3NDM1MTEyZGQ3NmM3MmM3MDc5NTAxNTI3YTY0OTNiZWQ4NzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJCwsDCzfohVJxBHMu', '2016-05-23 08:11:03'),
('5qanxa6gu7b799twru13vbwyl569h8vl', 'YjhmN2VlMThlNzdmYmE5YjdhNzk5ODQ2MTQ0NjI5NjQ1MDc2NmM1NzqAAn1xAS4=', '2015-06-18 17:08:17'),
('66wdofqqqz8xse8zrbzglcxiole3pwsu', 'MmM2ZGVjNDE0NTkxNzIyZWY3NjhhY2M1MjNhMjllNGU0ZTk1ZjI4MzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIEQoSB5RIhVJxBHMu', '2016-05-22 14:10:18'),
('74zvuu3gpweg6811xp1kgmevwjevefj3', 'MDExZGUxZWMzNmEwOTFmMmRjMTUyNDM4MmFmNWIzZGFiYTIyODQxODqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJAAsXC/4chVJxBHMu', '2016-05-22 21:11:23'),
('8hke0wp9fcybqoy8aik6ndxowylofa44', 'ZTEzMWQ5NWNiMmUyYmU3OWRkOTA1MGUwMGIwM2MxZDA5YzE2ZTlkZDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBQoMDlNthVJxBHMu', '2016-05-23 02:10:12'),
('a7kpxzod8umv87v2k3m65vjzc830ybo0', 'YmNkYjE0YzA1NmQ4ZTIyYjk2ODA2ZmI2Mjk0MDljZmQzODAzNDM0NjqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIEAodBZNghVJxBHMu', '2016-05-22 13:10:29'),
('al5z711tkz2h90aregl2lbtuijrvnx6g', 'Y2YzYzI4YzM1Y2E3YTliZjQwNmY2ODU1YWM1Y2E3MGE5NjhhNTBhMDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIEgoUC+svhVJxBHMu', '2016-05-22 15:10:20'),
('bcys0z5mvwi0zsgxy6vlfopjhbl08ii3', 'Zjc0MDNkZGYzMjU2ZWQ0YjY4YTAyYjRkODljNTgyYzI3MGU0YmVlNTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJDAoRCPavhVJxBHMu', '2016-05-23 09:10:17'),
('c1k0e8mjs4wl973k67k9tyhun38nvkhr', 'NGNjNDU2NTE4NGYyMTI2NThlNDRkYTE5Y2RhYjVkZjM4OTg3YWZhMTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIDwoODm63hVJxBHMu', '2016-05-22 12:10:15'),
('cnesovojiopjjscrmy96rnjp7b0b7de1', 'ZTNiYjYzZmU2YWMwZTI2YTc0NmFjYzVhZTQ2Y2I1NzQyZTM3M2NhNTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIFwsiCxklhVJxBHMu', '2016-05-22 20:11:34'),
('d9d6u0izpwe7c07nlkwhsbro5rcmkq1s', 'Y2Q5YzcyMzhlOTg4MDZlNjA0MWRmYTExOTQ0NGFlMDY4ZTk4OGVhMTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIEQoSBeSNhVJxBHMu', '2016-05-22 14:10:18'),
('dnpxkwpxchp14kasqmgo3xjzx7hbhwpj', 'YjZiMWVlMjM3MTEwZmMzYzdiZWUzYjgwYjNlYTgyYThjNDE4NmI4YjqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJAgodALDihVJxBHMu', '2016-05-22 23:10:29'),
('duaymx7jwedavmm3rw8l3dbein74rqkq', 'ODE0ODBlZmZiZmZmODc3MTlhMjc2YzcxMTU5NWU5YTllYmU0NmNmMDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBgsEAEOqhVJxBHMu', '2016-05-23 03:11:04'),
('e1g3302ckx5kaw5x03krkxzzid788mdy', 'MDZlNjY3Y2RiY2YyNmYwYzRjYjg3ZjcwNGVjODhmNWRkOGE4ODE1ZDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBwocBSAwhVJxBHMu', '2016-05-23 04:10:28'),
('e3cbaiyz8wg8opeats08pnw1nqljfj0r', 'ZjBlMmM0ZWVkN2NkODIwMDk3MjYzMjgyYmFhNWQ4MzdlNDQ3MTI0MzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJAgodAgjZhVJxBHMu', '2016-05-22 23:10:29'),
('erqklgnu90qy5bddiq6nwri0ksse9gko', 'NDlhNzlmYzI0MjY0NDYzYTcwNzRkZmY3MmNiMjM2NGE1ZDg5OTcxMzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIEwoWDmbphVJxBHMu', '2016-05-22 16:10:22'),
('fe7ghruj3rvtqmzvhsknv8319assnfka', 'Mjc0MmIwOGQyYmExMWIyOWRmYWMxZjhjYTI5MDE2MjFkNzQ3Y2JjOTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIFgoMDqhbhVJxBHMu', '2016-05-22 19:10:12'),
('fyxto3o7gqut3igutli8d2pq93eyl844', 'YzgzMGRkZmNjNjRkODY1OTUyZDg1ZWQ2MTkzNjliNjIzN2Y1N2IxMjqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJDQAEAUXghVJxBHMu', '2016-05-23 10:00:04'),
('g5gpqh3i5twqo4zpl3gpto6yepmyve8r', 'MWM5YjM0Yjg5MjBlMGIzZjAyODFiYWRiNmU5NjBmMTQwZDc2N2Y1OTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJCQoRDVgahVJxBHMu', '2016-05-23 06:10:17'),
('gywzz0riv9zuz34qmy2e1o3bjh8hl89j', 'OGFmNGE3ODQ4ZTNkNTkwODhhNzUxOGE3N2Q5OTFjMWYyZTZjNWNiNTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJAQoUCGmLhVJxBHMu', '2016-05-22 22:10:20'),
('hd1ujyxjn7avze73b4llwk50uosi87no', 'MWUyY2JlYjIwNzVmOTVhYmJmYmE3MGI1N2E0NzU1NTg1M2Q5N2ZjYTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJAwsGCNBfhVJxBHMu', '2016-05-23 00:11:06'),
('hq38aktisuhoqgohthl0gdi5ix4gk9em', 'Y2U0ZDZiZjcyYWI2YzExNjgwNjZkNjYyNDczODVhN2MwMDJmMDViNjqAAn1xAShVCnRlYWNoZXJfaWSKAQRVDHRlYWNoZXJfcm9sZVgQAAAA0JLQuNC60LvQsNC00LDRh1UKbGFzdF90b3VjaGNkYXRldGltZQpkYXRldGltZQpxAlUKB98GBAsVAwI9fYVScQN1Lg==', '2015-06-18 08:21:03'),
('hyhktju6lc6gyo7a16fk7k5gh2oz7jej', 'ODQ0NTg5YjE4ZmNjNDNkYzEwNGU0ZGM2NzU4Y2Y2NGNmOWY2ZDg0ODqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBgsEAXO+hVJxBHMu', '2016-05-23 03:11:04'),
('j8zgf9fa3itr6bt5bqu3fw78ewcn0yvl', 'MmQ3OGZlZDM5ODYxNzk1MjIxOWFkYmY5NzcwMjdjYTA4MGIxMDllNjqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIFQsiDtJvhVJxBHMu', '2016-05-22 18:11:34'),
('jx5rdii5dufvava7pb9c5oswsknl01ft', 'YWI3ODdmOWVjNTEzODkxYmQ1ZmJmNTI5NGZkYmJmODg3ZDFhMmFkNjqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJCwsDDRYBhVJxBHMu', '2016-05-23 08:11:03'),
('ln2u78hpewog45115on3et7s3vy3qbwt', 'NWU1MzM0MGZiNzhjYjJhZDJjODQ4NzNkYzY3ZGJkMjgzOWZjMDkyMDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJCgoTAdqrhVJxBHMu', '2016-05-23 07:10:19'),
('mxbgcvq1ckdkjyn5vofuwpt6mpcq4up3', 'NTdmMGFiOTcwMTc3Y2Q0ODEzNTdiMDU0OGUzZmJjZGE3YjgxNzJkOTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIEgoUDReRhVJxBHMu', '2016-05-22 15:10:20'),
('n3ltybhrbdyhun9n93ydlxbbaaxo9hdr', 'MzhhNTA0NWViZDYzYjg2Yjg3ZDFiNjMyMDBmODA0NDkyYWVhZDRkMDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIDi8zCmXxhVJxBHMu', '2016-05-22 11:47:51'),
('oo74zwygowo1cgc5mrc2ky1djyp863dh', 'MjIyNjQ1OWU4YWEwNWZkNTg1Y2Y0NTUwYTUwN2YyOTA3ZDUyNzgyYzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBwocBFPbhVJxBHMu', '2016-05-23 04:10:28'),
('p5mkm0g6uzt76orlf6rhbehs0op9ksdm', 'ZGVlNGZlYzFjMTMyZmI3NzZlOWVlMzMyMWI5ZWYwMzY0OTYyYjNlODqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJAAsXCmovhVJxBHMu', '2016-05-22 21:11:23'),
('p5xy2ozc4s69rwmgdinvd4nq8gletu2j', 'MGIwYTAyOGIyNjQxZTMxNjUyZTZmYTY5MThmZDM0MTk4OTk2NTM2ZDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJCgoTBC2DhVJxBHMu', '2016-05-23 07:10:19'),
('pj1bhqtgnc9sisxn2957hj9c97wwqlxp', 'MjUzOGQ0MjQwMTcwYjFiMTMyNWY0ZTg0YjYwMWY2YTk4M2QyOTU2MDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIEAodAWwThVJxBHMu', '2016-05-22 13:10:29'),
('prodf4no84r3btpb3n474kmm1yltuhep', 'NWVmNWYzOTgxYzYxZTcxMjFhNGM0OTY1N2VhMzE3NmM2YjAzMzA1NzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBQoMD0BwhVJxBHMu', '2016-05-23 02:10:13'),
('q2xq73xzxq68wo6l33d27ugilmrnhzv2', 'YTkxODQ4NzIwOGZkNzVhZjExYWE1YjQ5NzEzYzk2NmE1OGJlOGMwNzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIFQsiDh09hVJxBHMu', '2016-05-22 18:11:34'),
('roy2memzijdakrvih3a7cnaiwg8unudm', 'ZGY0MWJmNGVmNjg5MTk1Y2Q3NGU3ZTZlZWE5ZjI0ZmIwMzAwZmU2YzqAAn1xAVUKbGFzdF90b3VjaGNkYXRldGltZQpkYXRldGltZQpxAlUKB98GBBYULAqGzIVScQNzLg==', '2015-06-18 19:20:44'),
('rr9k6nq7alj4w99g4knxvqts4pzjwl2i', 'MDJiODUxYWNhZDZhNmI5MGYzNmMzNzhkY2JmN2RlOWRlOTg3MzhiMTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBAoMBfq4hVJxBHMu', '2016-05-23 01:10:12'),
('s5vtxqr93z7btpoupnmodxjm4zoh81js', 'ZTVlMzE3OGIyZmQxOTYzYTRkOTUwMmZkODI5MDNiZDAxNDU5ODJhODqAAn1xAShVCnRlYWNoZXJfaWSKAQRVDHRlYWNoZXJfcm9sZVgQAAAA0JLQuNC60LvQsNC00LDRh1UKbGFzdF90b3VjaGNkYXRldGltZQpkYXRldGltZQpxAlUKB98GGBQyNgop6oVScQN1Lg==', '2015-07-08 17:50:54'),
('s9mxeosyqnz9448s29oyvn4s5e97sh2z', 'ODI2NmUwNjY3YTMxOWUxYjY0ZGI0ZGY1ZTYxZjcyNGM0ZjY4NDM2ZDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJCAoQDMPThVJxBHMu', '2016-05-23 05:10:16'),
('seecyo5bvhhfiwfue1linj9v3a70ku0l', 'MmIwZTAxYTRkNDAwYzg3MjBhNjE5ZTFlM2RmZGJiYzYxM2IwYzRjMzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJCAoQDAKehVJxBHMu', '2016-05-23 05:10:16'),
('sv6su3hvtxunkjlhxna50y1itaq0i0au', 'YzAxMGQwMDAwOWNjMzIyNzAzMTY3MDY4OTk2NmEzMDQxNGEzN2RhYzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIDwoPBGoXhVJxBHMu', '2016-05-22 12:10:15'),
('sxig8eep2k4lgaq420pmpuo7a1ink038', 'ZTdmNDU4MzE4YTQ0YzM0ZGNlMzRiNzNhNWZjNTYzNzIzNzVjYjBhMDqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIFAoPDEUxhVJxBHMu', '2016-05-22 17:10:15'),
('toxa21h5u28uaehqgnh4ta819o2kbm7j', 'NjMyYTU2ODg5NDgzZTQzNGFhMjJiNjMyMmI1Y2M3YjkxOGU5MDA0MTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBCQLALw6hVJxBHMu', '2016-05-23 01:36:11'),
('ubpopscercgksoipvqj25rhv3mskhpog', 'ZTJlMDg2OGFjM2I3YmZlNGJiMDEzNzE0N2RjMmU1ZjUxOTE3MjM3ZTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJAQoUBYWuhVJxBHMu', '2016-05-22 22:10:20'),
('v3wfia39p0y8sq49yuoqz0rcuxwfzo8h', 'NWYxNThiYTJiYmYxZWE3YzYwZWZhZjAyODE5MDhlY2RiNmQ1NzAxMTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIFgoMDQpZhVJxBHMu', '2016-05-22 19:10:12'),
('wdeovpgo6ma9f4zz1xra5iwqyg0g4j8f', 'NDdmMGUxODNiNTlkYzU1Y2M0ZGQ1MTNiNDhhNzU4ZTJjNmE0NGRkMTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIFwsiDBBvhVJxBHMu', '2016-05-22 20:11:34'),
('wq3d13q2usocl7au191f9dyeixsqjttf', 'Nzg3YmI3MGFlYjk0NGUwZDJmMjEyMTJlMjVhMzI4MWFkZGY5ZGNiYzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIFAoPC4pThVJxBHMu', '2016-05-22 17:10:15'),
('z2l0ia8397vgnpweob41abvdef7cybve', 'YjZhMzZlMjBjYjMwODNkMzBlYWNmZmYwYTRmYzNjOWFlM2RhNDFkZTqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUIEwoWDbV+hVJxBHMu', '2016-05-22 16:10:22'),
('z6utha0xfdgg48f7n9i2c4x0vs2avzce', 'ZDI4YzkxMTRiMTQwZGVmMjc0MDQwNzM2OWFhYjc0M2ZmODZiZTQ5MzqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJBAoMBFGZhVJxBHMu', '2016-05-23 01:10:12'),
('zhkqf3vjxdkooa9r4c19i594mbv3gd13', 'NDUyNzg4OWRhMTc4M2YwMDBkNTZhOGM5M2UwYWUxMjkyNWNjMjA2ZjqAAn1xAVUKbGFzdF90b3VjaHECY2RhdGV0aW1lCmRhdGV0aW1lCnEDVQoH4AUJCQoRDqqihVJxBHMu', '2016-05-23 06:10:17');

-- --------------------------------------------------------

--
-- Структура таблицы `Groups`
--

CREATE TABLE IF NOT EXISTS `Groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(5) NOT NULL,
  `state` int(11) NOT NULL,
  `school_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Groups_school_id_2f28c60259391856_fk_Schools_id` (`school_id`),
  KEY `Groups_teacher_id_2ab420cd5dca5d9d_fk_Teachers_id` (`teacher_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=17 ;

--
-- Дамп данных таблицы `Groups`
--

INSERT INTO `Groups` (`id`, `name`, `state`, `school_id`, `teacher_id`) VALUES
(1, '9A', 1, 1, NULL),
(2, '10A', 1, 1, NULL),
(3, '11A', 1, 1, NULL),
(4, '8А', 1, 1, NULL),
(5, '8Б', 1, 1, NULL),
(6, '8В', 1, 1, NULL),
(7, '9Б', 1, 1, NULL),
(8, '10Б', 1, 1, NULL),
(9, '11Б', 1, 1, NULL),
(10, '1А', 1, 1, NULL),
(11, '1Б', 1, 1, NULL),
(12, '1В', 1, 1, NULL),
(13, '2А', 1, 1, NULL),
(14, '2Б', 1, 1, NULL),
(15, '3А', 1, 1, NULL),
(16, '3Б', 1, 1, NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `Journal`
--

CREATE TABLE IF NOT EXISTS `Journal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mark` int(11) DEFAULT NULL,
  `comment` varchar(400) DEFAULT NULL,
  `lesson_id` int(11) NOT NULL,
  `marktype_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Journal_55174b7b` (`lesson_id`),
  KEY `Journal_061cf1f9` (`marktype_id`),
  KEY `Journal_30a811f6` (`student_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=97 ;

--
-- Дамп данных таблицы `Journal`
--

INSERT INTO `Journal` (`id`, `mark`, `comment`, `lesson_id`, `marktype_id`, `student_id`) VALUES
(1, NULL, '', 2, 2, 5),
(2, 7, '', 2, 1, 2),
(3, 9, '', 2, 1, 3),
(4, NULL, 'Відпрошення батьків', 2, 2, 1),
(5, 7, '', 3, 2, 5),
(6, 9, '', 3, 2, 1),
(7, 7, '', 4, 1, 69),
(8, 8, '', 4, 1, 64),
(9, 9, '', 4, 1, 67),
(10, 5, '', 4, 1, 68),
(11, 7, '', 4, 1, 65),
(12, 8, '', 4, 1, 71),
(13, 8, '', 4, 1, 72),
(14, NULL, '', 4, 2, 66),
(15, 9, 'доздав', 4, 2, 70),
(16, 5, '', 5, 1, 69),
(17, 8, '', 5, 1, 64),
(18, NULL, '', 5, 2, 68),
(19, NULL, '', 6, 2, 68),
(20, 5, '', 5, 1, 71),
(21, 9, '', 5, 1, 72),
(22, 2, '', 7, 1, 66),
(23, 8, '', 7, 1, 68),
(24, NULL, '', 7, 2, 72),
(25, 7, '', 7, 1, 70),
(26, 8, '', 8, 1, 66),
(27, 8, '', 8, 1, 69),
(28, 9, '', 8, 1, 65),
(29, 4, '', 8, 1, 70),
(30, 7, '', 9, 1, 67),
(31, 6, '', 9, 1, 65),
(32, NULL, '', 9, 2, 64),
(33, 5, '', 9, 1, 70),
(34, 8, '', 3, 1, 2),
(35, 6, '', 3, 1, 4),
(36, 4, '', 3, 1, 3),
(37, 7, '', 1, 1, 4),
(38, 8, '', 1, 1, 1),
(39, NULL, '', 1, 2, 2),
(40, 6, '', 11, 1, 5),
(41, NULL, '', 11, 2, 3),
(42, NULL, '', 12, 2, 4),
(43, 10, '', 12, 1, 5),
(44, 9, '', 12, 1, 1),
(45, 8, '', 13, 1, 2),
(46, 5, '', 13, 1, 3),
(47, 9, '', 14, 1, 4),
(48, NULL, '', 14, 2, 2),
(49, NULL, '', 15, 2, 2),
(50, 8, '', 15, 1, 5),
(51, 7, '', 15, 1, 1),
(52, NULL, '', 16, 2, 5),
(53, 9, '', 16, 1, 3),
(54, 5, '', 16, 1, 4),
(55, 8, '', 18, 1, 2),
(56, 7, '', 18, 2, 4),
(57, NULL, '', 18, 2, 3),
(58, 9, '', 18, 1, 1),
(59, NULL, '', 20, 2, 5),
(60, 7, '', 20, 1, 3),
(61, 9, '', 20, 1, 2),
(62, 8, '', 21, 1, 1),
(63, 10, '', 21, 1, 4),
(64, 4, '', 19, 1, 4),
(65, 7, '', 19, 1, 3),
(66, 7, '', 22, 1, 2),
(67, 8, '', 22, 1, 4),
(68, 5, '', 22, 1, 1),
(69, NULL, '', 23, 2, 2),
(70, 6, '', 23, 1, 5),
(71, 10, '', 23, 1, 3),
(72, NULL, '', 24, 2, 2),
(73, 7, '', 24, 1, 5),
(74, 8, '', 24, 1, 4),
(75, 7, '', 25, 1, 2),
(76, 7, '', 25, 1, 5),
(77, 9, '', 25, 1, 4),
(78, 5, '', 25, 1, 3),
(79, 6, '', 25, 1, 1),
(80, 5, '', 26, 1, 2),
(81, 11, '', 26, 1, 1),
(82, 6, '', 26, 1, 3),
(83, NULL, '', 28, 2, 5),
(84, 7, '', 28, 1, 4),
(85, 8, '', 28, 1, 3),
(86, 9, '', 29, 1, 2),
(87, NULL, '', 29, 2, 5),
(88, 2, '', 29, 1, 1),
(89, NULL, '', 30, 2, 5),
(90, 7, '', 30, 1, 2),
(91, 10, '', 30, 1, 4),
(92, 7, '', 30, 2, 1),
(93, 8, '', 30, 1, 3),
(94, 9, '', 31, 1, 5),
(95, 7, '', 31, 1, 1),
(96, NULL, '', 31, 2, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `Lessons`
--

CREATE TABLE IF NOT EXISTS `Lessons` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `topic` varchar(200) NOT NULL,
  `homework` varchar(200) NOT NULL,
  `teacher_replace_id` int(11) DEFAULT NULL,
  `teacher_subject_group_id` int(11) NOT NULL,
  `lesson_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Lessons_edd57e7e` (`teacher_subject_group_id`),
  KEY `Lessons_teacher_replace_id_463d364cd09d9062_fk_Teachers_id` (`teacher_replace_id`),
  KEY `Lessons_4270872c` (`lesson_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=32 ;

--
-- Дамп данных таблицы `Lessons`
--

INSERT INTO `Lessons` (`id`, `date`, `topic`, `homework`, `teacher_replace_id`, `teacher_subject_group_id`, `lesson_type_id`) VALUES
(1, '2015-05-12', 'Способи вираження підмета.', 'Вправа 32, 33', NULL, 14, 1),
(2, '2015-06-03', 'Морфологічні способи словотворення', 'Вправа 35', NULL, 14, 1),
(3, '2015-06-03', 'Морфологічні способи словотворення', 'Повторити коспект, а також завдання з попереднього уроку', NULL, 14, 3),
(4, '2015-06-01', 'Морфологічні способи словотворення', 'Повторити коспект', NULL, 11, 3),
(5, '2015-06-04', 'Позначення звуків мовлення на письмі.', 'Вправа 27', NULL, 11, 1),
(6, '2015-06-04', 'Позначення звуків мовлення на письмі.', 'Повторити коспект', NULL, 11, 2),
(7, '2015-06-02', 'Лексичне значення слова.', 'Вправа 32, 33', NULL, 11, 1),
(8, '2015-05-26', 'Спрощення в групах приголосних.', 'Вправа 28', NULL, 11, 1),
(9, '2015-05-28', 'Типи обставин за значенням.', 'Повторити коспект', NULL, 11, 1),
(10, '2015-06-05', 'Способи вираження підмета.', 'Вправа 37', NULL, 11, 1),
(11, '2015-05-15', 'Порядок слів у реченні.', 'Вправа 28', NULL, 14, 1),
(12, '2015-05-17', 'Вигук як частина мови.', 'Вправа 30', NULL, 14, 1),
(13, '2015-05-19', 'Розряди прислівників за значенням.', 'Повторити коспект', NULL, 14, 1),
(14, '2015-05-22', 'Творення видових форм.', 'Вправа 29', NULL, 14, 1),
(15, '2015-05-25', 'Безособові дієслова.', 'Вправа 30', NULL, 14, 1),
(16, '2015-05-26', 'Якісні прикметники.', 'Повторити коспект', NULL, 14, 1),
(17, '2015-05-29', 'Відмінки іменників.', 'Тема на самостійне освоєння', NULL, 14, 2),
(18, '2015-05-11', 'Омоніми. Синоніми. Антоніми.', 'Повторити коспект', NULL, 14, 3),
(19, '2015-06-04', 'Спрощення в групах приголосних.', 'Вправа 39', NULL, 14, 1),
(20, '2015-05-05', 'Позначення звуків мовлення на письмі.', 'Вправа 18', NULL, 14, 1),
(21, '2015-05-07', 'Основні випадки чергування у-в, і-й', 'Вправа 20', NULL, 14, 1),
(22, '2015-05-08', 'ТЕМА 4. Українські народні балади', 'Прочитати: "Бондарівна", "Ой летіла стріла"', NULL, 16, 1),
(23, '2015-05-10', 'ТЕМА 5. ДАВНЯ УКРАЇНСЬКА ЛІТЕРАТУРА', 'Читати: Українська середньовічна література ХІ—ХV ст.', NULL, 16, 1),
(24, '2015-05-13', 'Оригінальна література княжої Руси-України', 'Читати про "Повість минулих літ"', NULL, 16, 1),
(25, '2015-05-16', 'Оригінальна література княжої Руси-України', 'Повторити попередні теми', NULL, 16, 3),
(26, '2015-05-18', 'ТЕМА 7. Українська література ренесансу і бароко', 'Читати про перші друковані книги в Україні', NULL, 16, 1),
(27, '2015-05-20', 'ТЕМА 8. Історично-мемуарна проза', 'Тема на самостійне опрацювання', NULL, 16, 2),
(28, '2015-05-25', 'Драматургія', 'Розповідь про відродження вертепної традиції в наш час.', NULL, 16, 1),
(29, '2015-05-28', 'ТЕМА 12. Іван Котляревський. "Енеїда" (скорочено)', 'Читати скорочено', NULL, 16, 1),
(30, '2015-06-01', 'Творчість Івана Котляревського', 'Повторити попередні теми', NULL, 16, 3),
(31, '2015-06-03', 'Григорій Квітка-Основ''яненко. "Конотопська відьма"', 'Прочитати будь-який твір автора на свій розсуд', NULL, 16, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `LessonTypes`
--

CREATE TABLE IF NOT EXISTS `LessonTypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `character` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `LessonTypes`
--

INSERT INTO `LessonTypes` (`id`, `character`) VALUES
(1, 'Звичайний'),
(2, 'Самостійна/Лабораторна робота'),
(3, 'Контрольна робота');

-- --------------------------------------------------------

--
-- Структура таблицы `MarkTypes`
--

CREATE TABLE IF NOT EXISTS `MarkTypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `character` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `MarkTypes`
--

INSERT INTO `MarkTypes` (`id`, `character`) VALUES
(1, 'Оцінка'),
(2, 'Н'),
(3, 'Н/П');

-- --------------------------------------------------------

--
-- Структура таблицы `Roles`
--

CREATE TABLE IF NOT EXISTS `Roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `Roles`
--

INSERT INTO `Roles` (`id`, `role_name`) VALUES
(1, 'Головний вчитель'),
(2, 'Завуч'),
(3, 'Викладач');

-- --------------------------------------------------------

--
-- Структура таблицы `Schools`
--

CREATE TABLE IF NOT EXISTS `Schools` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `address` varchar(256) DEFAULT NULL,
  `director_id` int(11) DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Schools_3f4c842e` (`director_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `Schools`
--

INSERT INTO `Schools` (`id`, `name`, `address`, `director_id`, `state`) VALUES
(1, 'НВК №2', 'вул. Караульна, 17', 6, 1),
(2, 'НВК №7', 'вул. Соборна, 11', 1, 1),
(3, 'НВК-ліцей №19', 'вул. Макарова, 32', 9, 1),
(4, 'НВК №26', 'вул. Степана Бандери, 49', NULL, 1),
(5, 'НВК "Колегіум"', 'вул. Пересопницька, 93', 11, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `Students`
--

CREATE TABLE IF NOT EXISTS `Students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `state` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Students_group_id_71db1dc94b53d3a_fk_Groups_id` (`group_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=125 ;

--
-- Дамп данных таблицы `Students`
--

INSERT INTO `Students` (`id`, `name`, `group_id`, `state`) VALUES
(1, 'Юрковська Надія Юріївна', 1, 1),
(2, 'Галицький Борис Максимович', 1, 1),
(3, 'Пташник Тетяна Миколаївна', 1, 1),
(4, 'Нетребко Юрій Вікторович', 1, 1),
(5, 'Довженко Олександр Миколайович', 1, 1),
(6, 'Бабіак Віктор Святославович', 2, 1),
(7, 'Рижак Марія Миколаївна', 2, 1),
(8, 'Кічатий Дмитро Павлович', 2, 1),
(9, 'Охріменко Олексій Петрович', 2, 1),
(10, 'Галицька Юлія Віталіївна', 2, 1),
(11, 'Тобілевич Марія Миколаївна', 3, 1),
(12, 'Семенченко Наталія Олегівна', 3, 1),
(13, 'Безлюдна Ганна Юріївна', 3, 1),
(14, 'Попіль Оксана Андріївна', 3, 1),
(15, 'Гринюк Олег Ярославович', 3, 1),
(16, 'Пасічник Андрій Васильович', 10, 1),
(17, 'Антонюк Ірина Василівна', 10, 1),
(18, 'Бойко Артем Микитович', 10, 1),
(19, 'Залюзнюк Олег Вікторович', 10, 1),
(20, 'Давидюк Тамара Олексіївна', 10, 1),
(21, 'Ясінчук Ян Володимирович', 10, 1),
(22, 'Наконечний Олександр Андрієвич', 13, 1),
(23, 'Петреченко Вікторія Назарівна', 10, 1),
(24, 'Давидюк Андрій Сергієвич', 11, 1),
(25, 'Омельчук Ігор Микитович', 11, 1),
(26, 'Савчук Олена Петрівна', 11, 1),
(27, 'Крижанівський Олег Віталієвич', 11, 1),
(28, 'Безхатченко Віталій Леонідович', 11, 1),
(29, 'Ясінський Олег Олексієвич', 11, 1),
(30, 'Панасюк Ігор Микитович', 11, 1),
(31, 'Дорошенко Анастасія Ігорівна', 11, 1),
(32, 'Іринчук Олена Григорівна', 12, 1),
(33, 'Коваленко Андрій Миколайович', 12, 1),
(34, 'Павлюченко Сергій Дмитрович', 12, 1),
(35, 'Архипенко Ірина Сергіївна', 12, 1),
(36, 'Конанчук Віктор Віталієвич', 12, 1),
(37, 'Шимчук Олександр Степанович', 12, 1),
(38, 'Бойко Сніжанна Мифодієвна', 12, 1),
(39, 'Степан Сорока Іванович', 12, 1),
(40, 'Засадько Олег Васильович', 13, 1),
(41, 'Антонюк Ірина Степанівна', 13, 1),
(42, 'Семенчук Роман Назарович', 13, 1),
(43, 'Панасюк Ігор Миколайович', 13, 1),
(44, 'Микитюк Софія Юрівна', 13, 1),
(45, 'Коваль Юрій Андрійович', 14, 1),
(46, 'Вербицька Христина Олегівна', 14, 1),
(47, 'Стоколос Ігор Микитович', 14, 1),
(48, 'Петреченко Вікторія Петрівна', 14, 1),
(49, 'Оксинчук Сергій Олегович', 14, 1),
(50, 'Давидюк Андрій Сергієвич', 14, 1),
(51, 'Савчук Сергій Андрієвич', 15, 1),
(52, 'Шимчук Олександра Степанівна', 15, 1),
(53, 'Шиманський Ігор Іванович', 15, 1),
(54, 'Коноплянко Вікторія Андріївна', 15, 1),
(55, 'Ковальчук Христина Романівна', 15, 1),
(56, 'Швець Юрій Артемович', 15, 1),
(57, 'Дорошенко Артем Леонідович', 16, 1),
(58, 'Загірний Леонід Валерієвич', 16, 1),
(59, 'Шиманська Людмила Григорівна', 16, 1),
(60, 'Сорока Степан Іванович', 16, 1),
(61, 'Свистун Архип Іванович', 16, 1),
(62, 'Одарієв Андрій Олександрович', 16, 1),
(63, 'Карамач Володимир Олегович', 16, 1),
(64, 'Обліпиха Володимир Володимирович', 4, 1),
(65, 'Савчук Олена Петрівна', 4, 1),
(66, 'Панасюк Ігор Олександрович', 4, 1),
(67, 'Петрук Тамара Миколаївна', 4, 1),
(68, 'Порох Євген Леонідович', 4, 1),
(69, 'Кулаковський Іван Орестович', 4, 1),
(70, 'Степанюк Володимир Григорович', 4, 1),
(71, 'Сорока Ірина Ігорівна', 4, 1),
(72, 'Щеба Андрій Назарович', 4, 1),
(73, 'Пахальчук Андрій Валерієвич', 5, 1),
(74, 'Остапенко Вікторія Олександрівна', 5, 1),
(75, 'Щербань Мифодій Архипович', 5, 1),
(76, 'Онуфрієнко Андрій Семенович', 5, 1),
(77, 'Вербицький Олександр Олександрович', 5, 1),
(78, 'Скороход Іван Петрович', 5, 1),
(79, 'Нагірний Андрій Вікторвич', 5, 1),
(80, 'Антонюк Софія Степанівна', 5, 1),
(81, 'Стрілець Микола Григорович', 5, 1),
(82, 'Панасюк Ігор Микитович', 6, 1),
(83, 'Коваленко Андрій Мифодієвич', 6, 1),
(84, 'Савчук Олена Петрівна', 6, 1),
(85, 'Свистун Пилип Степанович', 6, 1),
(86, 'Давидюк Андрій Сергієвич', 6, 1),
(87, 'Архипенко Ірина Сергіївна', 6, 1),
(88, 'Дехтяр Інна Семенівна', 6, 1),
(89, 'Засадько Олег Васильович', 6, 1),
(90, 'Дорошенко Анастасія Ігорівна', 6, 1),
(91, 'Нагірний Андрій Вікторвич', 7, 1),
(92, 'Бойко Сніжанна Мифодієвна', 7, 1),
(93, 'Антонюк Ірина Степанівна', 7, 1),
(94, 'Ковальчук Христина Романівна', 7, 1),
(95, 'Погребняк Володимир Володимирович', 7, 1),
(96, 'Григорук Олег Олексієвич', 7, 1),
(97, 'Швець Юрій Артемович', 7, 1),
(98, 'Засадько Олег Васильович', 2, 1),
(99, 'Кулаковський Орест Кирилович', 2, 1),
(100, 'Свистун Пилип Степанович', 2, 1),
(101, 'Панасюк Ігор Микитович', 2, 1),
(102, 'Коваль Юрій Андрійович', 8, 1),
(103, 'Загірний Леонід Валерієвич', 8, 1),
(104, 'Омельчук Андрій Олегович', 8, 1),
(105, 'Іринчук Олена Григорівна', 8, 1),
(106, 'Давидюк Тамара Олексіївна', 8, 1),
(107, 'Степан Сорока Іванович', 8, 1),
(108, 'Андрійчук Ірина Василівна', 8, 1),
(109, 'Балашов Юрій Васильович', 8, 1),
(110, 'Коваль Артем Миколайович', 8, 1),
(111, 'Нагірний Андрій Вікторвич', 3, 1),
(112, 'Дорошенко Анастасія Ігорівна', 3, 1),
(113, 'Дехтяр Інна Семенівна', 3, 1),
(114, 'Ковальчук Христина Романівна', 3, 1),
(115, 'Давидюк Тамара Олексіївна', 3, 1),
(116, 'Дорошенко Анастасія Ігорівна', 9, 1),
(117, 'Панасюк Ігор Микитович', 9, 1),
(118, 'Антонюк Ірина Василівна', 9, 1),
(119, 'Коваленко Андрій Миколайович', 9, 1),
(120, 'Балашов Юрій Васильович', 9, 1),
(121, 'Іринчук Олена Григорівна', 9, 1),
(122, 'Карамач Володимир Олегович', 9, 1),
(123, 'Петреченко Вікторія Петрівна', 9, 1),
(124, 'Свистун Архип Іванович', 9, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `Subjects`
--

CREATE TABLE IF NOT EXISTS `Subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Дамп данных таблицы `Subjects`
--

INSERT INTO `Subjects` (`id`, `name`) VALUES
(1, 'Фізика'),
(2, 'Астрономія'),
(3, 'Математика'),
(4, 'Геометрія'),
(5, 'Інформатика'),
(6, 'Георгафія'),
(7, 'Українська мова'),
(8, 'Українська література'),
(9, 'Зарубіжна література'),
(10, 'Фізична культура'),
(11, 'Трудове навчання'),
(12, 'ДПЮ');

-- --------------------------------------------------------

--
-- Структура таблицы `Teachers`
--

CREATE TABLE IF NOT EXISTS `Teachers` (
  `school_id` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `role_id` int(11) NOT NULL,
  `login` varchar(40) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(180) DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `salt` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `school_id` (`school_id`),
  KEY `role_id` (`role_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=17 ;

--
-- Дамп данных таблицы `Teachers`
--

INSERT INTO `Teachers` (`school_id`, `id`, `name`, `role_id`, `login`, `email`, `password`, `state`, `avatar`, `salt`) VALUES
(2, 1, 'Зощенко Іван Вікторович', 2, 'zoshch', 'zoshch@gmail.com', 'df5sFdf', 1, '', NULL),
(2, 2, 'Галицький Максим Генадійович', 3, 'maximus', 'maximus@gmail.com', 'LKuJf3y', 1, '', NULL),
(1, 3, 'Винниченко Наталя Леонідівна', 3, 'nata', 'nata@gmail.com', 'Hjh43kH', 1, '', NULL),
(1, 4, 'Бондаренко Юлія Олександрівна', 3, 'yulia', 'yulia@gmail.com', 'Lhkj4Gh', 1, '', NULL),
(NULL, 5, 'Семищенко Христофор Онуфрійович', 1, 'semuschenko', 'semuschenko@gmail.com', 'pDk7jf', 1, NULL, NULL),
(1, 6, 'Охріменко Василь Георгійович', 2, 'ohrch', 'ohrimko@gmail.com', 'Bndk7H', 1, '', NULL),
(1, 7, 'Панасюк Ігор Микитович', 3, 'Igor_panasuk', 'example_mail_@ukr.net', '6Ct0XQZd', 1, '', NULL),
(2, 8, 'Балашов Юрій Васильович', 3, 'Uriy_Balash', 'bavcxz__1978@mail.ru', 'S7yUvGN1', 1, '', NULL),
(3, 9, 'Аношко Петро Микитович', 2, 'petr_anoshk', 'petr_anoshk@gmai.com', 'w0bzyN6a', 1, '', NULL),
(3, 10, 'Григорук Олег Степанович', 3, 'oleg_stepanovich', 'oleg_stepanovich@ukr.net', 'e3bwvTrX', 1, '', NULL),
(5, 11, 'Міщенко Олена Петрівна', 2, 'Alena_m', 'olena_m@ukr.net', 'aSeM12KY', 1, '', NULL),
(5, 12, 'Галай Людмила Архипівна', 3, 'Galay_Luda', 'example_mail_2@ukr.net', 'xMLapMg2', 1, '', NULL),
(4, 13, 'Петросян Іван Сергієвич', 3, 'Ivan_Sergievich_P', 'ivan_petrosyan@gmail.com', '7kWysU4i', 1, '', NULL),
(1, 14, 'Свистун Пилип Степанович', 3, 'Svistun_Pilip', 'svistun_1978@mail.ru', 'KhrBUfDx', 1, '', NULL),
(1, 15, 'Дехтяр Інна Семенівна', 3, 'Inna_Semenivna', 'inna_semenivna@gmail.com', 'cOUl0bHM', 1, '', NULL),
(1, 16, 'Левицька Тамара Сергіївна', 3, 'Tamara_Levicka', 'toma_lev@gmail.com', '0TdjMpSY', 1, '', NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `TeacherSubjectGroups`
--

CREATE TABLE IF NOT EXISTS `TeacherSubjectGroups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `teacher_subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TeacherSubjectGroups_c74c0abb` (`teacher_subject_id`),
  KEY `TeacherSubjectGroups_group_id_32800bfb4dd948fc_fk_Groups_id` (`group_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=40 ;

--
-- Дамп данных таблицы `TeacherSubjectGroups`
--

INSERT INTO `TeacherSubjectGroups` (`id`, `group_id`, `teacher_subject_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 3, 2),
(5, 2, 3),
(6, 3, 3),
(7, 1, 4),
(8, 3, 5),
(9, 2, 6),
(10, 3, 6),
(11, 4, 7),
(12, 5, 7),
(13, 6, 7),
(14, 1, 7),
(15, 7, 8),
(16, 1, 8),
(17, 4, 9),
(18, 5, 9),
(19, 6, 15),
(20, 1, 9),
(21, 7, 15),
(22, 10, 11),
(23, 11, 11),
(24, 12, 11),
(25, 13, 11),
(26, 14, 11),
(27, 16, 11),
(28, 15, 11),
(32, 2, 14),
(33, 8, 14),
(34, 3, 14),
(35, 9, 14),
(36, 3, 12),
(37, 9, 12),
(38, 4, 10),
(39, 6, 10);

-- --------------------------------------------------------

--
-- Структура таблицы `TeacherSubjects`
--

CREATE TABLE IF NOT EXISTS `TeacherSubjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TeacherSubjects_teacher_id_e7dcd24858a18cb_fk_Teachers_id` (`teacher_id`),
  KEY `TeacherSubjects_subject_id_211b5309eef33423_fk_Subjects_id` (`subject_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=16 ;

--
-- Дамп данных таблицы `TeacherSubjects`
--

INSERT INTO `TeacherSubjects` (`id`, `subject_id`, `teacher_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 2),
(5, 5, 2),
(6, 6, 3),
(7, 7, 4),
(8, 8, 4),
(9, 1, 15),
(10, 9, 16),
(11, 10, 7),
(12, 12, 7),
(14, 3, 14),
(15, 1, 14);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Ограничения внешнего ключа таблицы `Groups`
--
ALTER TABLE `Groups`
  ADD CONSTRAINT `Groups_school_id_2f28c60259391856_fk_Schools_id` FOREIGN KEY (`school_id`) REFERENCES `Schools` (`id`),
  ADD CONSTRAINT `Groups_teacher_id_2ab420cd5dca5d9d_fk_Teachers_id` FOREIGN KEY (`teacher_id`) REFERENCES `Teachers` (`id`);

--
-- Ограничения внешнего ключа таблицы `Journal`
--
ALTER TABLE `Journal`
  ADD CONSTRAINT `Journal_lesson_id_51f10b0bca2eaad2_fk_Lessons_id` FOREIGN KEY (`lesson_id`) REFERENCES `Lessons` (`id`),
  ADD CONSTRAINT `Journal_marktype_id_2e24d1864c358dad_fk_MarkTypes_id` FOREIGN KEY (`marktype_id`) REFERENCES `MarkTypes` (`id`),
  ADD CONSTRAINT `Journal_student_id_42279cd6f6d19442_fk_Students_id` FOREIGN KEY (`student_id`) REFERENCES `Students` (`id`);

--
-- Ограничения внешнего ключа таблицы `Lessons`
--
ALTER TABLE `Lessons`
  ADD CONSTRAINT `b4fb0c7970e3a541fa14d4aa5408442b` FOREIGN KEY (`teacher_subject_group_id`) REFERENCES `TeacherSubjectGroups` (`id`),
  ADD CONSTRAINT `Lessons_lesson_type_id_11d8c4807dc199ae_fk_LessonTypes_id` FOREIGN KEY (`lesson_type_id`) REFERENCES `LessonTypes` (`id`),
  ADD CONSTRAINT `Lessons_teacher_replace_id_463d364cd09d9062_fk_Teachers_id` FOREIGN KEY (`teacher_replace_id`) REFERENCES `Teachers` (`id`);

--
-- Ограничения внешнего ключа таблицы `Schools`
--
ALTER TABLE `Schools`
  ADD CONSTRAINT `Schools_director_id_5bfb8f0fe7eb13a6_fk_Teachers_id` FOREIGN KEY (`director_id`) REFERENCES `Teachers` (`id`);

--
-- Ограничения внешнего ключа таблицы `Students`
--
ALTER TABLE `Students`
  ADD CONSTRAINT `Students_group_id_71db1dc94b53d3a_fk_Groups_id` FOREIGN KEY (`group_id`) REFERENCES `Groups` (`id`);

--
-- Ограничения внешнего ключа таблицы `Teachers`
--
ALTER TABLE `Teachers`
  ADD CONSTRAINT `Teachers_ibfk_1` FOREIGN KEY (`school_id`) REFERENCES `Schools` (`id`),
  ADD CONSTRAINT `Teachers_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `Roles` (`id`);

--
-- Ограничения внешнего ключа таблицы `TeacherSubjectGroups`
--
ALTER TABLE `TeacherSubjectGroups`
  ADD CONSTRAINT `TeacherSubjectGroups_group_id_32800bfb4dd948fc_fk_Groups_id` FOREIGN KEY (`group_id`) REFERENCES `Groups` (`id`),
  ADD CONSTRAINT `Teache_teacher_subject_id_46b001cdc4de7678_fk_TeacherSubjects_id` FOREIGN KEY (`teacher_subject_id`) REFERENCES `TeacherSubjects` (`id`);

--
-- Ограничения внешнего ключа таблицы `TeacherSubjects`
--
ALTER TABLE `TeacherSubjects`
  ADD CONSTRAINT `TeacherSubjects_subject_id_211b5309eef33423_fk_Subjects_id` FOREIGN KEY (`subject_id`) REFERENCES `Subjects` (`id`),
  ADD CONSTRAINT `TeacherSubjects_teacher_id_e7dcd24858a18cb_fk_Teachers_id` FOREIGN KEY (`teacher_id`) REFERENCES `Teachers` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
