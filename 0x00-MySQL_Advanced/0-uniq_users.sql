--create a Table user
--with attributes id, email, name
DROP TABLE IF EXIST user;
CREATE TABLE user(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
