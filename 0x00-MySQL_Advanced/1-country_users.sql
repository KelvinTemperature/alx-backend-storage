--create a Table user
--with attributes id, email, name, country
DROP TABLE IF EXIST user;
CREATE TABLE user(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	country CHAR(2) NOT NULL DEFAULT 'US' CHECK(country IN ('US', 'CO', 'TN'))
);
