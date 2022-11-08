from database.db_connection import get_db_connection


def add_message(email, first_name, last_name, message):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT INTO contact_messages
                                         (email, first_name, last_name, message)
                                  VALUES (%s, %s, %s, %s)""", [email, first_name, last_name, message])
            # the %s-s allow avoiding sql attacks, normally we would write VALUES ({email}...,
            # but write it this way instead to avoid attacks
            connection.commit()
