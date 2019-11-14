create database twitter;
DROP DATABASE twitter;

SHOW TABLES;
use twitter;


CREATE TABLE users (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(100) NOT NULL,
  fullname varchar(255) NOT NULL,
  status smallint(1) NOT NULL,
  gender varchar(1) NOT NULL,
  email varchar(150) NOT NULL,
  password varchar(150) NOT NULL,
  location varchar(255) NOT NULL,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY unique_idx (`username`),
  KEY fullname (`fullname`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

CREATE TABLE users_avatars (
  user_id int(11) NOT NULL,
  url text NOT NULL,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  CONSTRAINT user_avatars_user_id FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE tweets (
  id int(11) NOT NULL AUTO_INCREMENT,
  user_id int(11) NOT NULL,
  type varchar(20) NOT NULL,
  message varchar(255) NOT NULL,
  parent_id int(11) NOT NULL,
  favourite_count int(11) NOT NULL,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY tweets_user_id (`user_id`),
  CONSTRAINT tweets_user_id FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

CREATE TABLE user_followers (
  id int(11) NOT NULL AUTO_INCREMENT,
  user_id int(11) NOT NULL,
  following_id int(11) NOT NULL,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY user_followers_user_id (`user_id`),
  CONSTRAINT user_followers_user_id FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;


CREATE TABLE favourites (
  tweet_id int(11) NOT NULL,
  user_id int(11) NOT NULL,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`tweet_id`,`user_id`),
  KEY favourites_user_id (`user_id`),
  CONSTRAINT favourites_tweet_id FOREIGN KEY (`tweet_id`) REFERENCES tweets (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT favourites_user_id FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO users (username, fullname, status, gender, email, password, location) VALUES ('hadildo', 'Nurhadi Aldo', 1, 'm', 'hadildo@tronjaltronjol.com', '123456', 'Jawa Timur');
INSERT INTO users (username, fullname, status, gender, email, password, location) 
VALUES ('syamsul', 'Muhammad Syamsul', 1, 'm', 'syamsul@tronjaltronjol.com', '123456', 'Jawa Timur');
INSERT INTO users (id,username, fullname, status, gender, email, password, location) 
VALUES (3,'arif', 'Muhammad Syamsul', 1, 'm', 'syamsul@tronjaltronjol.com', '123456', 'Jawa Timur');
INSERT INTO tweets (user_id, type, message, parent_id, favourite_count)VALUES 
(1,'tweets', 'Maju terus panjang jalan', 0, 0);
INSERT INTO tweets (user_id, type, message, parent_id, favourite_count)VALUES 
(1,'tweets', 'Jalan itu bukan khayalan semata wayang', 0, 0);
INSERT INTO tweets (user_id, type, message, parent_id, favourite_count)VALUES 
(3,'tweets', 'Hi semua!', 0, 0);
INSERT INTO tweets (user_id, type, message, parent_id, favourite_count)VALUES 
(2,'tweets', 'Hi juga!', 0, 0);
UPDATE tweets SET user_id=3 WHERE message='Hi semua!';
DELETE FROM tweets WHERE id BETWEEN 1 AND 3;
SELECT * FROM users;
SELECT * FROM tweets;
SELECT id, user_id, type, message, parent_id FROM tweets WHERE message LIKE 'H%' OR user_id BETWEEN 1 AND 2 ORDER BY id DESC;
SELECT username, fullname FROM users WHERE fullname IS NOT NULL;
UPDATE users SET fullname='Nurhadi Aldo Tronjal Tronjol' WHERE id=1;
UPDATE users SET gender='o' WHERE username='syamsul1995';
DELETE FROM users WHERE id=5;