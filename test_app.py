import unittest
import HolidayHelper.app
import HolidayHelper.database.users
import HolidayHelper.database.db_connection
from unittest.mock import patch
from flask.ext.testing import TestCase



class BaseTestCase(TestCase):
    """A base test case for flask-tracking."""

    def create_app(self):
        app.config.from_object('config.TestConfiguration')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestApp(unittest.TestCase):
    @classmethod # this means we are working with the class rather than the instance of the class
    def setUpClass(cls): # can eg define values in a database for the duration of the below tests then tear down using the next method below
        print('setupClass')

    @classmethod
    def tearDownClass(cls): # whereas set up runs its code before every test, tear down runs after every test
        print('teardownClass')

    def test_User(self):
        pass

    def test_user_loader(self):
        # HolidayHelper.app.view_home
        pass









if __name__ == '__main__':
    unittest.main()
