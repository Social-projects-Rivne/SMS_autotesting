SET foreign_key_checks = 0;

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

INSERT INTO `Teachers` VALUES
 (NULL,4,'Test Main Teacher',1,'test_admin','test_admin@gmail.com','Install_new!',1,NULL,NULL);
 
ALTER TABLE `Teachers`
ADD CONSTRAINT `Teachers_school_id_fk_Schools_id` FOREIGN KEY (`school_id`) REFERENCES `Schools` (`id`),
ADD CONSTRAINT `Teachers_role_id_fk_Roles_id` FOREIGN KEY (`role_id`) REFERENCES `Roles` (`id`);