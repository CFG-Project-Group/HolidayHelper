CREATE DATABASE HolidayHelper;
USE HolidayHelper;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  hashed_password BLOB
);

INSERT INTO users
(name, email, hashed_password)
VALUES
('Test_User', 'test@gmail.com', '12345678');

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


CREATE TABLE IF NOT EXISTS weather_images (
weather_condition VARCHAR(50) unique primary key,
image_address VARCHAR(1000));

INSERT INTO weather_images VALUES
    ('thunderstorm with light rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('thunderstorm with rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('thunderstorm with heavy rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('light thunderstorm','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('thunderstorm','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('heavy thunderstorm','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('ragged thunderstorm','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('thunderstorm with light drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('thunderstorm with drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('thunderstorm with heavy drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('light intensity drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('heavy intensity drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('light intensity drizzle rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('drizzle rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('heavy intensity drizzle rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('shower rain and drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('heavy shower rain and drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('shower drizzle','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('light rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_7-512.png'),
    ('moderate rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_16-512.png'),
    ('heavy intensity rain','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Hail_Heavy.png'),
    ('very heavy rain','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Hail_Heavy.png'),
    ('extreme rain','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Hail_Heavy.png'),
    ('freezing rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_16-512.png'),
    ('light intensity shower rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_16-512.png'),
    ('shower rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('heavy intensity shower rain','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Hail_Heavy.png'),
    ('ragged shower rain','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_17-512.png'),
    ('light snow','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_36-256.png'),
    ('snow','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_35-256.png'),
    ('heavy snow','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_35-256.png'),
    ('sleet','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Sleet.png'),
    ('light shower sleet','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Sleet.png'),
    ('shower sleet','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Sleet.png'),
    ('light rain and snow','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Sleet.png'),
    ('rain and snow','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Sleet.png'),
    ('light shower snow','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Sleet.png'),
    ('shower snow','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Sleet.png'),
    ('heavy shower snow','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Sleet.png'),
    ('mist','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_30-256.png'),
    ('smoke','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_46-512.png'),
    ('haze','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_30-256.png'),
    ('fog','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_30-256.png'),
    ('tornado','https://cdn0.iconfinder.com/data/icons/weather-line-19/32/Tornado-256.png'),
    ('clear sky','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_3-512.png'),
    ('few clouds','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_2-512.png'),
    ('scattered clouds','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_1-512.png'),
    ('broken clouds','https://cdn4.iconfinder.com/data/icons/the-weather-is-nice-today/64/weather_1-512.png'),
    ('overcast clouds','https://cdn4.iconfinder.com/data/icons/iconsland-weather/PNG/256x256/Overcast.png');