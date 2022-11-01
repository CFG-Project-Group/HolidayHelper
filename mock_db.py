import mysql.connector
from mysql.connector import errorcode, cursor
from unittest import TestCase
from mock import patch
import HolidayHelper.database.users
import HolidayHelper.database.db_connection
from HolidayHelper.config import HOST, DATABASE, USER, PASSWORD

class MockDB(TestCase): #we can inherit this class to create test cases

    @classmethod
    def setUpClass(cls):
        cnx = mysql.connector.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop database if it already exists

        try:
            cursor.execute("DROP DATABASE {}".format('HolidayHelper'))
            cursor.close()
            print("DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format('HolidayHelper', err))

        testconfig = {
            'host': HOST,
            'database': DATABASE,
            'user': USER,
            'password': PASSWORD
        }
        cls.mock_db_config = patch.dict(HolidayHelper.config, testconfig)

    @classmethod
    def tearDownClass(cls):
        cnx = mysql.connector.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP DATABASE {}".format(DATABASE))
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exists. Dropping db failed".format(DATABASE))
        cnx.close()

