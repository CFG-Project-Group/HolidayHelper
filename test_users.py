from mock_db import MockDB
from mock import patch
from database.users import add_user


class TestUtils(MockDB):

    def test_add_user(self):
        with self.mock_db_config:
            self.assertEqual(add_user("""INSERT INTO `test_table` (`id`, `name`, `email`, `hashed_password`) 
                                                                          VALUES ('3', 'Ali', 'ali@gmail.com', 'BLOB')"""), [add_user.name, add_user.email, add_user.hashed_password], True)
            self.assertEqual(add_user("""INSERT INTO `test_table` (`id`, `name`, `email`, `hashed_password`) VALUES
                            ('1', 'Emily', 'emily@gmail.com', 'BLOB')"""), False)
            # self.assertEqual(database.users.add_user("""DELETE FROM `test_table` WHERE id='1' """), True)
            # self.assertEqual(database.users.add_user("""DELETE FROM `test_table` WHERE id='2' """), True)

