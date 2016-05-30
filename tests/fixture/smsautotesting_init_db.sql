-- DROP DATABASE IF EXISTS smsautotesting;
-- CREATE DATABASE smsautotesting CHARACTER SET utf8;
USE smsautotesting;
SET foreign_key_checks = 0;

-- -----------------------------------------------------------------------------------------------------------------
-- CREATE
-- -----------------------------------------------------------------------------------------------------------------

DROP TABLE IF EXISTS `Groups`;
CREATE TABLE `Groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(5) NOT NULL,
  `state` int(11) NOT NULL,
  `school_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `Journal`;
CREATE TABLE `Journal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mark` int(11) DEFAULT NULL,
  `comment` varchar(400) DEFAULT NULL,
  `lesson_id` int(11) NOT NULL,
  `marktype_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `LessonTypes`;
CREATE TABLE `LessonTypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `character` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `Lessons`;
CREATE TABLE `Lessons` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `topic` varchar(200) NOT NULL,
  `homework` varchar(200) NOT NULL,
  `teacher_replace_id` int(11) DEFAULT NULL,
  `teacher_subject_group_id` int(11) NOT NULL,
  `lesson_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `MarkTypes`;
CREATE TABLE `MarkTypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `character` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `Roles`;
CREATE TABLE `Roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `Schools`;
CREATE TABLE `Schools` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `address` varchar(256) DEFAULT NULL,
  `director_id` int(11) DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `Students`;
CREATE TABLE `Students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `state` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `Subjects`;
CREATE TABLE `Subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `TeacherSubjectGroups`;
CREATE TABLE `TeacherSubjectGroups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `teacher_subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `TeacherSubjects`;
CREATE TABLE `TeacherSubjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `Teachers`;
CREATE TABLE `Teachers` (
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- -----------------------------------------------------------------------------------------------------------------
-- INSERT
-- -----------------------------------------------------------------------------------------------------------------
INSERT INTO `Groups` VALUES
(1,'9A',1,1,NULL),(2,'10A',1,1,NULL),(3,'11A',1,1,NULL),(4,'8А',1,1,NULL),(5,'8Б',1,1,NULL),(6,'8В',1,1,NULL),(7,'9Б',1,1,NULL),(8,'10Б',1,1,NULL),(9,'11Б',1,1,NULL),(10,'1А',1,1,NULL),(11,'1Б',1,1,NULL),(12,'1В',1,1,NULL),(13,'2А',1,1,NULL),(14,'2Б',1,1,NULL),(15,'3А',1,1,NULL),(16,'3Б',1,1,NULL);

INSERT INTO `Journal` VALUES
 (1,NULL,'',2,2,5),(2,7,'',2,1,2),(3,9,'',2,1,3),(4,NULL,'Відпрошення батьків',2,2,1),(5,7,'',3,2,5),(6,9,'',3,2,1),(7,7,'',4,1,69),(8,8,'',4,1,64),(9,9,'',4,1,67),(10,5,'',4,1,68),(11,7,'',4,1,65),(12,8,'',4,1,71),(13,8,'',4,1,72),(14,NULL,'',4,2,66),(15,9,'доздав',4,2,70),(16,5,'',5,1,69),(17,8,'',5,1,64),(18,NULL,'',5,2,68),(19,NULL,'',6,2,68),(20,5,'',5,1,71),(21,9,'',5,1,72),(22,2,'',7,1,66),(23,8,'',7,1,68),(24,NULL,'',7,2,72),(25,7,'',7,1,70),(26,8,'',8,1,66),(27,8,'',8,1,69),(28,9,'',8,1,65),(29,4,'',8,1,70),(30,7,'',9,1,67),(31,6,'',9,1,65),(32,NULL,'',9,2,64),(33,5,'',9,1,70),(34,8,'',3,1,2),(35,6,'',3,1,4),(36,4,'',3,1,3),(37,7,'',1,1,4),(38,8,'',1,1,1),(39,NULL,'',1,2,2),(40,6,'',11,1,5),(41,NULL,'',11,2,3),(42,NULL,'',12,2,4),(43,10,'',12,1,5),(44,9,'',12,1,1),(45,8,'',13,1,2),(46,5,'',13,1,3),(47,9,'',14,1,4),(48,NULL,'',14,2,2),(49,NULL,'',15,2,2),(50,8,'',15,1,5),(51,7,'',15,1,1),(52,NULL,'',16,2,5),(53,9,'',16,1,3),(54,5,'',16,1,4),(55,8,'',18,1,2),(56,7,'',18,2,4),(57,NULL,'',18,2,3),(58,9,'',18,1,1),(59,NULL,'',20,2,5),(60,7,'',20,1,3),(61,9,'',20,1,2),(62,8,'',21,1,1),(63,10,'',21,1,4),(64,4,'',19,1,4),(65,7,'',19,1,3),(66,7,'',22,1,2),(67,8,'',22,1,4),(68,5,'',22,1,1),(69,NULL,'',23,2,2),(70,6,'',23,1,5),(71,10,'',23,1,3),(72,NULL,'',24,2,2),(73,7,'',24,1,5),(74,8,'',24,1,4),(75,7,'',25,1,2),(76,7,'',25,1,5),(77,9,'',25,1,4),(78,5,'',25,1,3),(79,6,'',25,1,1),(80,5,'',26,1,2),(81,11,'',26,1,1),(82,6,'',26,1,3),(83,NULL,'',28,2,5),(84,7,'',28,1,4),(85,8,'',28,1,3),(86,9,'',29,1,2),(87,NULL,'',29,2,5),(88,2,'',29,1,1),(89,NULL,'',30,2,5),(90,7,'',30,1,2),(91,10,'',30,1,4),(92,7,'',30,2,1),(93,8,'',30,1,3),(94,9,'',31,1,5),(95,7,'',31,1,1),(96,NULL,'',31,2,3);
  
 INSERT INTO `LessonTypes` VALUES
 (1,'Звичайний'),(2,'Самостійна/Лабораторна робота'),(3,'Контрольна робота');
 
INSERT INTO `Lessons` VALUES
 (1,'2015-05-12','Способи вираження підмета.','Вправа 32, 33',NULL,14,1),(2,'2015-06-03','Морфологічні способи словотворення','Вправа 35',NULL,14,1),(3,'2015-06-03','Морфологічні способи словотворення','Повторити коспект, а також завдання з попереднього уроку',NULL,14,3),(4,'2015-06-01','Морфологічні способи словотворення','Повторити коспект',NULL,11,3),(5,'2015-06-04','Позначення звуків мовлення на письмі.','Вправа 27',NULL,11,1),(6,'2015-06-04','Позначення звуків мовлення на письмі.','Повторити коспект',NULL,11,2),(7,'2015-06-02','Лексичне значення слова.','Вправа 32, 33',NULL,11,1),(8,'2015-05-26','Спрощення в групах приголосних.','Вправа 28',NULL,11,1),(9,'2015-05-28','Типи обставин за значенням.','Повторити коспект',NULL,11,1),(10,'2015-06-05','Способи вираження підмета.','Вправа 37',NULL,11,1),(11,'2015-05-15','Порядок слів у реченні.','Вправа 28',NULL,14,1),(12,'2015-05-17','Вигук як частина мови.','Вправа 30',NULL,14,1),(13,'2015-05-19','Розряди прислівників за значенням.','Повторити коспект',NULL,14,1),(14,'2015-05-22','Творення видових форм.','Вправа 29',NULL,14,1),(15,'2015-05-25','Безособові дієслова.','Вправа 30',NULL,14,1),(16,'2015-05-26','Якісні прикметники.','Повторити коспект',NULL,14,1),(17,'2015-05-29','Відмінки іменників.','Тема на самостійне освоєння',NULL,14,2),(18,'2015-05-11','Омоніми. Синоніми. Антоніми.','Повторити коспект',NULL,14,3),(19,'2015-06-04','Спрощення в групах приголосних.','Вправа 39',NULL,14,1),(20,'2015-05-05','Позначення звуків мовлення на письмі.','Вправа 18',NULL,14,1),(21,'2015-05-07','Основні випадки чергування у-в, і-й','Вправа 20',NULL,14,1),(22,'2015-05-08','ТЕМА 4. Українські народні балади','Прочитати: \"Бондарівна\", \"Ой летіла стріла\"',NULL,16,1),(23,'2015-05-10','ТЕМА 5. ДАВНЯ УКРАЇНСЬКА ЛІТЕРАТУРА','Читати: Українська середньовічна література ХІ—ХV ст.',NULL,16,1),(24,'2015-05-13','Оригінальна література княжої Руси-України','Читати про \"Повість минулих літ\"',NULL,16,1),(25,'2015-05-16','Оригінальна література княжої Руси-України','Повторити попередні теми',NULL,16,3),(26,'2015-05-18','ТЕМА 7. Українська література ренесансу і бароко','Читати про перші друковані книги в Україні',NULL,16,1),(27,'2015-05-20','ТЕМА 8. Історично-мемуарна проза','Тема на самостійне опрацювання',NULL,16,2),(28,'2015-05-25','Драматургія','Розповідь про відродження вертепної традиції в наш час.',NULL,16,1),(29,'2015-05-28','ТЕМА 12. Іван Котляревський. \"Енеїда\" (скорочено)','Читати скорочено',NULL,16,1),(30,'2015-06-01','Творчість Івана Котляревського','Повторити попередні теми',NULL,16,3),(31,'2015-06-03','Григорій Квітка-Основ\'яненко. \"Конотопська відьма\"','Прочитати будь-який твір автора на свій розсуд',NULL,16,1);
  
 INSERT INTO `MarkTypes` VALUES
 (1,'Оцінка'),(2,'Н'),(3,'Н/П');
  
 INSERT INTO `Roles` VALUES
 (1,'Головний вчитель'),(2,'Завуч'),(3,'Викладач');
  
 INSERT INTO `Schools` VALUES
 (1,'НВК №2','вул. Караульна, 17',6,1),(2,'НВК №7','вул. Соборна, 11',1,1),(3,'НВК-ліцей №19','вул. Макарова, 32',9,1),(4,'НВК №26','вул. Степана Бандери, 49',NULL,1),(5,'НВК \"Колегіум\"','вул. Пересопницька, 93',11,1);
  
 INSERT INTO `Students` VALUES
 (1,'Юрковська Надія Юріївна',1,1),(2,'Галицький Борис Максимович',1,1),(3,'Пташник Тетяна Миколаївна',1,1),(4,'Нетребко Юрій Вікторович',1,1),(5,'Довженко Олександр Миколайович',1,1),(6,'Бабіак Віктор Святославович',2,1),(7,'Рижак Марія Миколаївна',2,1),(8,'Кічатий Дмитро Павлович',2,1),(9,'Охріменко Олексій Петрович',2,1),(10,'Галицька Юлія Віталіївна',2,1),(11,'Тобілевич Марія Миколаївна',3,1),(12,'Семенченко Наталія Олегівна',3,1),(13,'Безлюдна Ганна Юріївна',3,1),(14,'Попіль Оксана Андріївна',3,1),(15,'Гринюк Олег Ярославович',3,1),(16,'Пасічник Андрій Васильович',10,1),(17,'Антонюк Ірина Василівна',10,1),(18,'Бойко Артем Микитович',10,1),(19,'Залюзнюк Олег Вікторович',10,1),(20,'Давидюк Тамара Олексіївна',10,1),(21,'Ясінчук Ян Володимирович',10,1),(22,'Наконечний Олександр Андрієвич',13,1),(23,'Петреченко Вікторія Назарівна',10,1),(24,'Давидюк Андрій Сергієвич',11,1),(25,'Омельчук Ігор Микитович',11,1),(26,'Савчук Олена Петрівна',11,1),(27,'Крижанівський Олег Віталієвич',11,1),(28,'Безхатченко Віталій Леонідович',11,1),(29,'Ясінський Олег Олексієвич',11,1),(30,'Панасюк Ігор Микитович',11,1),(31,'Дорошенко Анастасія Ігорівна',11,1),(32,'Іринчук Олена Григорівна',12,1),(33,'Коваленко Андрій Миколайович',12,1),(34,'Павлюченко Сергій Дмитрович',12,1),(35,'Архипенко Ірина Сергіївна',12,1),(36,'Конанчук Віктор Віталієвич',12,1),(37,'Шимчук Олександр Степанович',12,1),(38,'Бойко Сніжанна Мифодієвна',12,1),(39,'Степан Сорока Іванович',12,1),(40,'Засадько Олег Васильович',13,1),(41,'Антонюк Ірина Степанівна',13,1),(42,'Семенчук Роман Назарович',13,1),(43,'Панасюк Ігор Миколайович',13,1),(44,'Микитюк Софія Юрівна',13,1),(45,'Коваль Юрій Андрійович',14,1),(46,'Вербицька Христина Олегівна',14,1),(47,'Стоколос Ігор Микитович',14,1),(48,'Петреченко Вікторія Петрівна',14,1),(49,'Оксинчук Сергій Олегович',14,1),(50,'Давидюк Андрій Сергієвич',14,1),(51,'Савчук Сергій Андрієвич',15,1),(52,'Шимчук Олександра Степанівна',15,1),(53,'Шиманський Ігор Іванович',15,1),(54,'Коноплянко Вікторія Андріївна',15,1),(55,'Ковальчук Христина Романівна',15,1),(56,'Швець Юрій Артемович',15,1),(57,'Дорошенко Артем Леонідович',16,1),(58,'Загірний Леонід Валерієвич',16,1),(59,'Шиманська Людмила Григорівна',16,1),(60,'Сорока Степан Іванович',16,1),(61,'Свистун Архип Іванович',16,1),(62,'Одарієв Андрій Олександрович',16,1),(63,'Карамач Володимир Олегович',16,1),(64,'Обліпиха Володимир Володимирович',4,1),(65,'Савчук Олена Петрівна',4,1),(66,'Панасюк Ігор Олександрович',4,1),(67,'Петрук Тамара Миколаївна',4,1),(68,'Порох Євген Леонідович',4,1),(69,'Кулаковський Іван Орестович',4,1),(70,'Степанюк Володимир Григорович',4,1),(71,'Сорока Ірина Ігорівна',4,1),(72,'Щеба Андрій Назарович',4,1),(73,'Пахальчук Андрій Валерієвич',5,1),(74,'Остапенко Вікторія Олександрівна',5,1),(75,'Щербань Мифодій Архипович',5,1),(76,'Онуфрієнко Андрій Семенович',5,1),(77,'Вербицький Олександр Олександрович',5,1),(78,'Скороход Іван Петрович',5,1),(79,'Нагірний Андрій Вікторвич',5,1),(80,'Антонюк Софія Степанівна',5,1),(81,'Стрілець Микола Григорович',5,1),(82,'Панасюк Ігор Микитович',6,1),(83,'Коваленко Андрій Мифодієвич',6,1),(84,'Савчук Олена Петрівна',6,1),(85,'Свистун Пилип Степанович',6,1),(86,'Давидюк Андрій Сергієвич',6,1),(87,'Архипенко Ірина Сергіївна',6,1),(88,'Дехтяр Інна Семенівна',6,1),(89,'Засадько Олег Васильович',6,1),(90,'Дорошенко Анастасія Ігорівна',6,1),(91,'Нагірний Андрій Вікторвич',7,1),(92,'Бойко Сніжанна Мифодієвна',7,1),(93,'Антонюк Ірина Степанівна',7,1),(94,'Ковальчук Христина Романівна',7,1),(95,'Погребняк Володимир Володимирович',7,1),(96,'Григорук Олег Олексієвич',7,1),(97,'Швець Юрій Артемович',7,1),(98,'Засадько Олег Васильович',2,1),(99,'Кулаковський Орест Кирилович',2,1),(100,'Свистун Пилип Степанович',2,1),(101,'Панасюк Ігор Микитович',2,1),(102,'Коваль Юрій Андрійович',8,1),(103,'Загірний Леонід Валерієвич',8,1),(104,'Омельчук Андрій Олегович',8,1),(105,'Іринчук Олена Григорівна',8,1),(106,'Давидюк Тамара Олексіївна',8,1),(107,'Степан Сорока Іванович',8,1),(108,'Андрійчук Ірина Василівна',8,1),(109,'Балашов Юрій Васильович',8,1),(110,'Коваль Артем Миколайович',8,1),(111,'Нагірний Андрій Вікторвич',3,1),(112,'Дорошенко Анастасія Ігорівна',3,1),(113,'Дехтяр Інна Семенівна',3,1),(114,'Ковальчук Христина Романівна',3,1),(115,'Давидюк Тамара Олексіївна',3,1),(116,'Дорошенко Анастасія Ігорівна',9,1),(117,'Панасюк Ігор Микитович',9,1),(118,'Антонюк Ірина Василівна',9,1),(119,'Коваленко Андрій Миколайович',9,1),(120,'Балашов Юрій Васильович',9,1),(121,'Іринчук Олена Григорівна',9,1),(122,'Карамач Володимир Олегович',9,1),(123,'Петреченко Вікторія Петрівна',9,1),(124,'Свистун Архип Іванович',9,1);
 
 INSERT INTO `Subjects` VALUES
 (1,'Фізика'),(2,'Астрономія'),(3,'Математика'),(4,'Геометрія'),(5,'Інформатика'),(6,'Георгафія'),(7,'Українська мова'),(8,'Українська література'),(9,'Зарубіжна література'),(10,'Фізична культура'),(11,'Трудове навчання'),(12,'ДПЮ');
 
 INSERT INTO `TeacherSubjectGroups` VALUES
 (1,1,1),(2,2,1),(3,3,1),(4,3,2),(5,2,3),(6,3,3),(7,1,4),(8,3,5),(9,2,6),(10,3,6),(11,4,7),(12,5,7),(13,6,7),(14,1,7),(15,7,8),(16,1,8),(17,4,9),(18,5,9),(19,6,15),(20,1,9),(21,7,15),(22,10,11),(23,11,11),(24,12,11),(25,13,11),(26,14,11),(27,16,11),(28,15,11),(32,2,14),(33,8,14),(34,3,14),(35,9,14),(36,3,12),(37,9,12),(38,4,10),(39,6,10);
 
 INSERT INTO `TeacherSubjects` VALUES
 (1,1,1),(2,2,1),(3,3,2),(4,4,2),(5,5,2),(6,6,3),(7,7,4),(8,8,4),(9,1,15),(10,9,16),(11,10,7),(12,12,7),(14,3,14),(15,1,14);
 
 INSERT INTO `Teachers` VALUES
 (2,1,'Зощенко Іван Вікторович',2,'zoshch','zoshch@gmail.com','df5sFdf',1,'',NULL),(2,2,'Галицький Максим Генадійович',3,'maximus','maximus@gmail.com','LKuJf3y',1,'',NULL),(1,3,'Винниченко Наталя Леонідівна',3,'nata','nata@gmail.com','Hjh43kH',1,'',NULL),(1,4,'Бондаренко Юлія Олександрівна',3,'yulia','yulia@gmail.com','Lhkj4Gh',1,'',NULL),(NULL,5,'Семищенко Христофор Онуфрійович',1,'semuschenko','semuschenko@gmail.com','pDk7jf',1,NULL,NULL),(1,6,'Охріменко Василь Георгійович',2,'ohrch','ohrimko@gmail.com','Bndk7H',1,'',NULL),(1,7,'Панасюк Ігор Микитович',3,'Igor_panasuk','example_mail_@ukr.net','6Ct0XQZd',1,'',NULL),(2,8,'Балашов Юрій Васильович',3,'Uriy_Balash','bavcxz__1978@mail.ru','S7yUvGN1',1,'',NULL),(3,9,'Аношко Петро Микитович',2,'petr_anoshk','petr_anoshk@gmai.com','w0bzyN6a',1,'',NULL),(3,10,'Григорук Олег Степанович',3,'oleg_stepanovich','oleg_stepanovich@ukr.net','e3bwvTrX',1,'',NULL),(5,11,'Міщенко Олена Петрівна',2,'Alena_m','olena_m@ukr.net','aSeM12KY',1,'',NULL),(5,12,'Галай Людмила Архипівна',3,'Galay_Luda','example_mail_2@ukr.net','xMLapMg2',1,'',NULL),(4,13,'Петросян Іван Сергієвич',3,'Ivan_Sergievich_P','ivan_petrosyan@gmail.com','7kWysU4i',1,'',NULL),(1,14,'Свистун Пилип Степанович',3,'Svistun_Pilip','svistun_1978@mail.ru','KhrBUfDx',1,'',NULL),(1,15,'Дехтяр Інна Семенівна',3,'Inna_Semenivna','inna_semenivna@gmail.com','cOUl0bHM',1,'',NULL),(1,16,'Левицька Тамара Сергіївна',3,'Tamara_Levicka','toma_lev@gmail.com','0TdjMpSY',1,'',NULL);
 
 INSERT INTO `auth_permission` VALUES
 (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add teachers',6,'add_teachers'),(17,'Can change teachers',6,'change_teachers'),(18,'Can delete teachers',6,'delete_teachers'),(19,'Can add roles',7,'add_roles'),(20,'Can change roles',7,'change_roles'),(21,'Can delete roles',7,'delete_roles'),(22,'Can add schools',8,'add_schools'),(23,'Can change schools',8,'change_schools'),(24,'Can delete schools',8,'delete_schools'),(25,'Can add subjects',9,'add_subjects'),(26,'Can change subjects',9,'change_subjects'),(27,'Can delete subjects',9,'delete_subjects'),(28,'Can add groups',10,'add_groups'),(29,'Can change groups',10,'change_groups'),(30,'Can delete groups',10,'delete_groups'),(31,'Can add journal',11,'add_journal'),(32,'Can change journal',11,'change_journal'),(33,'Can delete journal',11,'delete_journal'),(34,'Can add lessons',12,'add_lessons'),(35,'Can change lessons',12,'change_lessons'),(36,'Can delete lessons',12,'delete_lessons'),(37,'Can add lesson types',13,'add_lessontypes'),(38,'Can change lesson types',13,'change_lessontypes'),(39,'Can delete lesson types',13,'delete_lessontypes'),(40,'Can add mark types',14,'add_marktypes'),(41,'Can change mark types',14,'change_marktypes'),(42,'Can delete mark types',14,'delete_marktypes'),(43,'Can add students',15,'add_students'),(44,'Can change students',15,'change_students'),(45,'Can delete students',15,'delete_students'),(46,'Can add teacher subjects',16,'add_teachersubjects'),(47,'Can change teacher subjects',16,'change_teachersubjects'),(48,'Can delete teacher subjects',16,'delete_teachersubjects'),(49,'Can add teacher subject groups',17,'add_teachersubjectgroups'),(50,'Can change teacher subject groups',17,'change_teachersubjectgroups'),(51,'Can delete teacher subject groups',17,'delete_teachersubjectgroups');
 
 INSERT INTO `django_content_type` VALUES
 (2,'auth','group'),(1,'auth','permission'),(3,'auth','user'),(4,'contenttypes','contenttype'),(7,'mainteacher','roles'),(8,'mainteacher','schools'),(9,'mainteacher','subjects'),(6,'mainteacher','teachers'),(5,'sessions','session'),(10,'teacher','groups'),(11,'teacher','journal'),(12,'teacher','lessons'),(13,'teacher','lessontypes'),(14,'teacher','marktypes'),(15,'teacher','students'),(17,'teacher','teachersubjectgroups'),(16,'teacher','teachersubjects');
 
 INSERT INTO `django_migrations` VALUES
 (1,'contenttypes','0001_initial','2015-06-03 19:58:53'),(2,'contenttypes','0002_remove_content_type_name','2015-06-03 19:58:54'),(3,'auth','0001_initial','2015-06-03 19:58:57'),(4,'auth','0002_alter_permission_name_max_length','2015-06-03 19:58:57'),(5,'auth','0003_alter_user_email_max_length','2015-06-03 19:58:57'),(6,'auth','0004_alter_user_username_opts','2015-06-03 19:58:57'),(7,'auth','0005_alter_user_last_login_null','2015-06-03 19:58:58'),(8,'auth','0006_require_contenttypes_0002','2015-06-03 19:58:58'),(9,'mainteacher','0001_initial','2015-06-03 19:58:58'),(10,'mainteacher','0002_auto_20150430_2146','2015-06-03 19:58:58'),(11,'mainteacher','0003_schools_director','2015-06-03 19:58:59'),(12,'mainteacher','0004_auto_20150501_1353','2015-06-03 19:59:00'),(13,'mainteacher','0005_auto_20150501_1355','2015-06-03 19:59:01'),(14,'mainteacher','0006_auto_20150514_2309','2015-06-03 19:59:01'),(15,'mainteacher','0007_auto_20150530_1404','2015-06-03 19:59:01'),(16,'mainteacher','0008_auto_20150530_1405','2015-06-03 19:59:01'),(17,'mainteacher','0009_auto_20150603_2247','2015-06-03 19:59:01'),(18,'sessions','0001_initial','2015-06-03 19:59:01'),(19,'teacher','0001_initial','2015-06-03 19:59:09'),(20,'teacher','0002_auto_20150517_1019','2015-06-03 19:59:10'),(21,'teacher','0003_auto_20150517_1029','2015-06-03 19:59:11'),(22,'teacher','0004_auto_20150520_2200','2015-06-03 19:59:17'),(23,'mainteacher','0010_auto_20150618_1018','2015-06-24 17:50:35'),(24,'mainteacher','0011_auto_20150618_1042','2015-06-24 17:50:36'),(25,'mainteacher','0012_auto_20150623_1054','2015-06-24 17:50:36'),(26,'mainteacher','0013_auto_20150623_2251','2015-06-24 17:50:37');
 
 INSERT INTO `django_session` VALUES
 ('5qanxa6gu7b799twru13vbwyl569h8vl','YjhmN2VlMThlNzdmYmE5YjdhNzk5ODQ2MTQ0NjI5NjQ1MDc2NmM1NzqAAn1xAS4=','2015-06-18 17:08:17'),('hq38aktisuhoqgohthl0gdi5ix4gk9em','Y2U0ZDZiZjcyYWI2YzExNjgwNjZkNjYyNDczODVhN2MwMDJmMDViNjqAAn1xAShVCnRlYWNoZXJfaWSKAQRVDHRlYWNoZXJfcm9sZVgQAAAA0JLQuNC60LvQsNC00LDRh1UKbGFzdF90b3VjaGNkYXRldGltZQpkYXRldGltZQpxAlUKB98GBAsVAwI9fYVScQN1Lg==','2015-06-18 08:21:03'),('roy2memzijdakrvih3a7cnaiwg8unudm','ZGY0MWJmNGVmNjg5MTk1Y2Q3NGU3ZTZlZWE5ZjI0ZmIwMzAwZmU2YzqAAn1xAVUKbGFzdF90b3VjaGNkYXRldGltZQpkYXRldGltZQpxAlUKB98GBBYULAqGzIVScQNzLg==','2015-06-18 19:20:44'),('s5vtxqr93z7btpoupnmodxjm4zoh81js','ZTVlMzE3OGIyZmQxOTYzYTRkOTUwMmZkODI5MDNiZDAxNDU5ODJhODqAAn1xAShVCnRlYWNoZXJfaWSKAQRVDHRlYWNoZXJfcm9sZVgQAAAA0JLQuNC60LvQsNC00LDRh1UKbGFzdF90b3VjaGNkYXRldGltZQpkYXRldGltZQpxAlUKB98GGBQyNgop6oVScQN1Lg==','2015-07-08 17:50:54');
 
 
 -- -----------------------------------------------------------------------------------------------------------------
-- RELATIONS (TABLE CONSTRAINTS)
-- -----------------------------------------------------------------------------------------------------------------

ALTER TABLE `Groups`
ADD CONSTRAINT `Groups_school_id_fk_Schools_id` FOREIGN KEY (`school_id`) REFERENCES `Schools` (`id`),
ADD CONSTRAINT `Groups_teacher_id_fk_Teachers_id` FOREIGN KEY (`teacher_id`) REFERENCES `Teachers` (`id`);

ALTER TABLE `Journal`
ADD CONSTRAINT `Journal_lesson_id_fk_Lessons_id` FOREIGN KEY (`lesson_id`) REFERENCES `Lessons` (`id`),
ADD CONSTRAINT `Journal_marktype_id_fk_MarkTypes_id` FOREIGN KEY (`marktype_id`) REFERENCES `MarkTypes` (`id`),
ADD CONSTRAINT `Journal_student_id_fk_Students_id` FOREIGN KEY (`student_id`) REFERENCES `Students` (`id`);

ALTER TABLE `Lessons`
ADD CONSTRAINT `Lessons_teacher_subject_group_id_fk_TeacherSubjectGroups_id` FOREIGN KEY (`teacher_subject_group_id`) REFERENCES `TeacherSubjectGroups` (`id`),
ADD CONSTRAINT `Lessons_lesson_type_id_fk_LessonTypes_id` FOREIGN KEY (`lesson_type_id`) REFERENCES `LessonTypes` (`id`),
ADD CONSTRAINT `Lessons_teacher_replace_id_fk_Teachers_id` FOREIGN KEY (`teacher_replace_id`) REFERENCES `Teachers` (`id`);

ALTER TABLE `Schools`
ADD CONSTRAINT `Schools_director_id_fk_Teachers_id` FOREIGN KEY (`director_id`) REFERENCES `Teachers` (`id`);

ALTER TABLE `Students`
ADD CONSTRAINT `Students_group_id_fk_Groups_id` FOREIGN KEY (`group_id`) REFERENCES `Groups` (`id`);

ALTER TABLE `TeacherSubjectGroups`
ADD CONSTRAINT `TeacherSubjectGroups_group_id_fk_Groups_id` FOREIGN KEY (`group_id`) REFERENCES `Groups` (`id`),
ADD CONSTRAINT `TeacherSubjectGroups_teacher_subject_id_fk_TeacherSubjects_id` FOREIGN KEY (`teacher_subject_id`) REFERENCES `TeacherSubjects` (`id`);

ALTER TABLE `TeacherSubjects`
ADD CONSTRAINT `TeacherSubjects_subject_id_fk_Subjects_id` FOREIGN KEY (`subject_id`) REFERENCES `Subjects` (`id`),
ADD CONSTRAINT `TeacherSubjects_teacher_id_fk_Teachers_id` FOREIGN KEY (`teacher_id`) REFERENCES `Teachers` (`id`);

ALTER TABLE `Teachers`
ADD CONSTRAINT `Teachers_school_id_fk_Schools_id` FOREIGN KEY (`school_id`) REFERENCES `Schools` (`id`),
ADD CONSTRAINT `Teachers_role_id_fk_Roles_id` FOREIGN KEY (`role_id`) REFERENCES `Roles` (`id`);

ALTER TABLE `auth_group_permissions`
ADD CONSTRAINT `auth_group_permissions_group_id_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `auth_group_permissions_permission_id_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

ALTER TABLE `auth_permission`
ADD CONSTRAINT `auth_permission_content_type_id_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

ALTER TABLE `auth_user_groups`
ADD CONSTRAINT `auth_user_groups_group_id_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `auth_user_groups_user_id_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `auth_user_user_permissions`
ADD CONSTRAINT `auth_user_user_permissions_user_id_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
ADD CONSTRAINT `auth_user_user_permissions_permission_id_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
