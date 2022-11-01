from database.db_connection import get_db_connection


class WeatherPicture:

    def __init__(self, weather_description):
        self.weather_description = weather_description.lower()

    def get_picture_address(self):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(f"""SELECT image_address from weather_images 
                                    WHERE weather_condition = '{self.weather_description.lower()}'""")
                address = cursor.fetchall()
                try:
                    return address[0]
                except IndexError:
                    return {}

    def get_weather_picture(self):
        image = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/draw2.webp"

        picture_address = self.get_picture_address()
        if len(picture_address) == 1:
            icon = self.get_picture_address()
            return icon
        else:
            return image

