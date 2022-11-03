from database.db_connection import get_db_connection
from database.users import add_user, email_available, get_user_with_credentials, get_user_by_id
from unittest import TestCase, main


class TestUsers(TestCase):
    def add_sample_user(self):
        """
        generic function that will be referenced to and run before every test below in order to add
        a dummy entry into the database
        """
        add_user('Mary', 'mary@gmail.com', password="12345678")

    def delete_most_recent(self):
        """
        generic function that will be referenced to and run at the end of every test below in order to
        remove the dummy entry added into the database
        """
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""DELETE
                                  FROM users AS u
                                  ORDER BY u.ID DESC LIMIT 1;
                                   """)
                connection.commit()


    def test_add_user(self):
        """
        Tests whether a user added to the database through the
        add_user function from users.py is actually added to the
        database, effectively checking the operation of the
        database connection
        """
        def query_result():
            with get_db_connection() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute("""SELECT u.name, u.email
                                        FROM users AS u
                                        ORDER BY u.ID DESC LIMIT 1
                                       """)
                    return cursor.fetchone()
        self.add_sample_user()
        self.assertEqual(query_result(), {'email': 'mary@gmail.com', 'name': 'Mary'})
        self.delete_most_recent()

    def test_email_available(self):
        """
        Tests whether the email_available function from users.py
        returns False if the email is already in the database
        and True if the email is not in the database yet
        """
        self.add_sample_user()
        self.assertEqual(email_available('mary@gmail.com'), False)
        self.assertEqual(email_available('mary2@gmail.com'), True)
        self.delete_most_recent()

    def test_get_user_with_credentials(self):
        """
        Tests whether the get_user_with_credentials function correctly
        identifies if the credentials (email, password) entered are
        correct by checking if there is a user with such email and
        password in the database
        """

        self.add_sample_user()
        def get_password_data():
            with get_db_connection() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    data = cursor.execute(f"""SELECT hashed_password
                                                FROM users
                                            ORDER BY id DESC LIMIT 1""")
                    data1 = cursor.fetchone()
                    return data1["hashed_password"]
        def get_id_data():
            with get_db_connection() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    data = cursor.execute(f"""SELECT id
                                                FROM users
                                            ORDER BY id DESC LIMIT 1""")
                    data2 = cursor.fetchone()
                    return data2["id"]

        self.assertEqual(get_user_with_credentials("mary@gmail.com", "12345678"), {'id': get_id_data(), 'name': 'Mary', 'email': 'mary@gmail.com', 'hashed_password': get_password_data()})
        self.delete_most_recent()

    def test_get_user_by_id(self):
        """
        Tests whether the get_user_by_id function correctly
        returns user details (id and name) based on their
        by checking if the corresponding id is in the database
        """
        self.add_sample_user()

        def get_id_data():
            with get_db_connection() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    data = cursor.execute(f"""SELECT id
                                                FROM users
                                            ORDER BY id DESC LIMIT 1""")
                    data2 = cursor.fetchone()
                    return data2["id"]

        self.assertEqual(get_user_by_id(get_id_data()), {'id': get_id_data(), 'name': 'Mary', 'email': 'mary@gmail.com'})
        self.delete_most_recent()

if __name__ == '__main__':
    main()
