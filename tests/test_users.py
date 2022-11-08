from database.db_connection import get_db_connection
from database.users import add_user, email_available, get_user_with_credentials, get_user_by_id
from unittest import TestCase, main


class TestUsers(TestCase):
    """
    The TestUsers class starts by defining 3 helper methods, then writing tests for each
    In order for the tests to work a dummy test account (name: Test_User, email: test@gmail.com)
    is required to be added each time before a test runs. In order to make sure that no one
    adds an account with the email test@gmail.com into our database, an account is created with
    this email when running the database (see schema). Since only unique emails can be added if a
    user tries to add a new account with the email test@gmail.com they won't be able to, reserving
    this email for the below tests. Nevertheless, the tests are ordered from 1-4, so that the
    tests run in order and before the first test_1_add_user test runs the account is deleted from the
    database making sure that when trying to add it back in when testing the add_user function there
    is no duplicate entry of the email. At the end of every test the delete_most_recent method is
    used to delete the account associated with test@gmail.com so that the next test has no dependency
    on the last test. The exception is test test_4_get_user_by_id, where at the end the test@gmail.com
    record is not deleted, so that it stays in the database (effectively going back to the pre-test
    status), deferring any users from trying to add an account with the email test@gmail.com.
    """
    def add_sample_user(self):
        """
        generic helper method that will be referenced to and run before every test below in order to add
        a dummy entry into the database
        """
        add_user('Test_User', 'test@gmail.com', password="12345678")


    def delete_Test_User(self):
        """
        generic helper method that will be referenced to and run at the end of every test below in order to
        remove the dummy entry added into the database
        """

        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""DELETE
                                  FROM users
                                  WHERE email = "test@gmail.com";
                                   """)
                connection.commit()



    def test_1_add_user(self):
        """
        Tests whether a user added to the database through the add_user function from users.py is actually added to the
        database, effectively checking the operation of the database connection.

        Please note the add_user function adds a user into the database (please see def add_sample_user method above
        (first method of this class)) and in order to test this function we need to retrieve what has been added to the
         database through the query_result method below, which is why the first argument of assertEqual below is
         query_result, as we are trying to retrieve what has been added by add_user.

         Please note the negative test of whether an error is raised if an attempt of an existing email addition would
         be covered in future testing of app.py as this method is used there to come up with negative scenarios
        """
        self.delete_Test_User()
        def query_result():
            with get_db_connection() as connection:
                with connection.cursor(dictionary=True) as cursor:
                    cursor.execute("""SELECT u.name, u.email
                                        FROM users AS u
                                        ORDER BY u.ID DESC LIMIT 1
                                       """)
                    return cursor.fetchone()
        self.add_sample_user()
        self.assertEqual(query_result(), {'email': 'test@gmail.com', 'name': 'Test_User'})
        self.delete_Test_User()


    def test_2_email_available(self):
        """
        Tests whether the email_available function from users.py
        returns False if the email is already in the database
        and True if the email is not in the database yet
        """
        self.add_sample_user()
        self.assertEqual(email_available('test@gmail.com'), False)
        self.delete_Test_User()
        self.assertEqual(email_available('test@gmail.com'), True)

    def test_3_get_user_with_credentials(self):
        """
        Tests whether the get_user_with_credentials function correctly
        identifies if the credentials (email, password) entered are
        correct by checking if there is a user with such email and
        password in the database

        Please note the negative test of whether an error is raised if an incorrect email and password and/or password
        are input is would be covered in future testing of app.py as this method is used there to come up with negative
        scenarios
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

        self.assertEqual(get_user_with_credentials("test@gmail.com", "12345678"), {'id': get_id_data(), 'name': 'Test_User', 'email': 'test@gmail.com', 'hashed_password': get_password_data()})
        self.delete_Test_User()

    def test_4_get_user_by_id(self):
        """
        Tests whether the get_user_by_id function correctly returns user details (id and name) based on their
        by checking if the corresponding id is in the database

        Please note the negative test of whether an error is raised if when loading the site a user id is not in the
        database would be covered in future testing of app.py as this method is used there to come up with negative
        scenarios

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

        self.assertEqual(get_user_by_id(get_id_data()), {'id': get_id_data(), 'name': 'Test_User', 'email': 'test@gmail.com'})



if __name__ == '__main__':
    main()