CREATE DATABASE HolidayHelper;
USE HolidayHelper;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  hashed_password BLOB,
  city_id int
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


ALTER TABLE cities
ADD CONSTRAINT FK_country
FOREIGN KEY (country_id) REFERENCES countries(id);

