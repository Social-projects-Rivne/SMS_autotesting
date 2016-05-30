SET foreign_key_checks = 0;

DROP TABLE IF EXISTS `Teachers`;
DROP TABLE IF EXISTS `Schools`;


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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

CREATE TABLE `Schools` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  `address` varchar(256) DEFAULT NULL,
  `director_id` int(11) DEFAULT NULL,
  `state` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

INSERT INTO `Schools` VALUES
 (1,'Тестова назва - Колегіум','тестова адреса',1,1),(2,'Test name - Colledge','test address',1,1),(3,'111222333','test address',1,1);
 
 INSERT INTO `Teachers` VALUES
 (2,1,'Тестенко Тест Тестович',2,'zoshch','test@gmail.com','df5sFdf',1,'',NULL),(2,2,'Testenko Test Testovych',3,'maximus','test@gmail.com','LKuJf3y',1,'',NULL),(1,3,'111222333',3,'nata','test@gmail.com','Hjh43kH',1,'',NULL),(NULL,4,'Test Main Teacher',1,'test_admin','test_admin@gmail.com','Install_new!',1,NULL,NULL);
 
 ALTER TABLE `Schools`
ADD CONSTRAINT `Schools_director_id_fk_Teachers_id` FOREIGN KEY (`director_id`) REFERENCES `Teachers` (`id`);

ALTER TABLE `Teachers`
ADD CONSTRAINT `Teachers_school_id_fk_Schools_id` FOREIGN KEY (`school_id`) REFERENCES `Schools` (`id`),
ADD CONSTRAINT `Teachers_role_id_fk_Roles_id` FOREIGN KEY (`role_id`) REFERENCES `Roles` (`id`);