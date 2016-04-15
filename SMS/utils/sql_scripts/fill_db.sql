-- switch to ur db
USE SMSDB;

-- LessonTypes
INSERT INTO `LessonTypes` (`id`,`character`) VALUES ('1','Звичайний');
INSERT INTO `LessonTypes` (`id`,`character`) VALUES ('2','Самостійна/Лабораторна робота');
INSERT INTO `LessonTypes` (`id`,`character`) VALUES ('3','Контрольна робота');

-- MarkTypes
INSERT INTO `MarkTypes` (`id`,`character`) VALUES ('1','Оцінка');
INSERT INTO `MarkTypes` (`id`,`character`) VALUES ('2','Н');
INSERT INTO `MarkTypes` (`id`,`character`) VALUES ('3','Н/П');