from database.db_connection import get_db_connection


def add_subscription(email):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT INTO subscriptions
                                         (email)
                                  VALUES (%s)""", [email])
            # the %s-s allow avoiding sql attacks, normally we would write VALUES ({email}...,
            # but write it this way instead to avoid attacks
            connection.commit()
