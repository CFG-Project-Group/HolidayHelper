from unittest import TestCase, main
from database.db_connection import get_db_connection


class DBConnectionTest(TestCase):

    def test_db_connection(self):
        self.assertTrue(get_db_connection().is_connected())

    def test_response(self):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""SELECT name FROM cities ORDER BY id LIMIT 2;'""")
                response = cursor.fetchall()
        self.assertEqual([{'name': 'London'}, {'name': 'Prague'}], response)

    def test_response_not_in_table(self):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""SELECT name FROM cities where name = 'Warsaw';'""")
                response = cursor.fetchall()
        self.assertEqual(response, [])


if __name__ == "__main__":
    main()
