CREATE DATABASE HolidayHelper;
USE HolidayHelper;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  hashed_password BLOB
);

CREATE TABLE cities(
id INT PRIMARY KEY auto_increment,
name VARCHAR(50) NOT NULL,
latitude decimal(6,4) NOT NULL,
longitude decimal(6,4) NOT NULL,
country_id INT NOT NULL
);

CREATE TABLE countries(
id INT PRIMARY KEY auto_increment,
name VARCHAR(50) NOT NULL,
currency_id int NOT NULL
);

CREATE TABLE currency(
currency_id int PRIMARY KEY auto_increment ,
name VARCHAR(50) unique,
code CHAR(3) unique);


CREATE TABLE country_languages(
country_id int NOT NULL,
language_id int
);

CREATE TABLE languages (
id int PRIMARY KEY auto_increment,
language_name VARCHAR(50) UNIQUE
);


CREATE TABLE messages (
id inT PRIMARY KEY auto_increment,
user_id_from int,
user_id_to int,
timestamp datetime,
content varchar(1000)
);

INSERT INTO cities
(name, latitude, longitude, country_id)
VALUES
('London', 51.5085, -0.1257, 1),
('Prague', 50.0755, 14.4378, 2),
('Budapest', 47.4979, 19.0402, 3),
('Barcelona', 41.3874, 2.1686,4);

INSERT INTO currency
(name, code)
VALUES
('British pound', 'GBP'),
('Czech koruna', 'CZK'),
('Hungarian forint', 'HUF'),
('Euro', 'EUR');


INSERT INTO countries(name, currency_id)
VALUES
('UK', 1),
('Czech Republic', 2),
('Hungary', 3),
('Spain', 4);


INSERT INTO country_languages(country_id, language_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);


INSERT INTO languages (language_name)
VALUES
('english'),
('czech'),
('hungarian'),
('spanish');

ALTER TABLE cities
ADD CONSTRAINT FK_country
FOREIGN KEY (country_id) REFERENCES countries(id);

ALTER TABLE countries
ADD CONSTRAINT FK_currency
FOREIGN KEY (currency_id) REFERENCES currency(currency_id);

ALTER TABLE country_languages
ADD CONSTRAINT FK_country_languages
FOREIGN KEY (country_id) REFERENCES countries(id);

ALTER TABLE country_languages
ADD CONSTRAINT FK_country_languages2
FOREIGN KEY (language_id) REFERENCES languages(id);

ALTER TABLE messages
add constraint fk_user_id_from
foreign key (user_id_from) references users(id);

ALTER TABLE messages
add constraint fk_user_id_to
foreign key (user_id_to) references users(id);

ALTER TABLE cities
ADD CONSTRAINT FK_country
FOREIGN KEY (country_id) REFERENCES countries(id);

