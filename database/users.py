import bcrypt  # for making passwords more secure
from database.db_connection import get_db_connection

def add_user(name, email, password):
    """
    Adds a new user to the database.
    Raises an error if the email already exists in the database.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            password_bytes = password.encode()  # this converts my code into bites so I can hash and salt later
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())  # this take my password bytes, adds a salt then hashes
            cursor.execute("""INSERT
                                INTO users
                                     (name, email, hashed_password)
                              VALUES (%s, %s, %s)""", [name, email, hashed_password]) # the %s-s allow to avoid sql attacks, normally we would write VALUES ({name}, {email}..., but write it this way instead to avoid attacks
            connection.commit()


def email_available(email):
    """
    Checks whether an email is available or whether it is already present in the database.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.id, u.name, u.email
                                FROM users AS u
                               WHERE u.email = %s""", [email])
            matching_user = cursor.fetchone()
            return True if matching_user is None else False


def get_user_with_credentials(email, password):   # function to refer to in app tab when logging in
    """
    Retrieves the user with the given credentials, if present.
    If there is no matching user, returns None.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            password_bytes = password.encode()
            cursor.execute("""SELECT u.id, u.name, u.email, u.hashed_password
                                FROM users AS u
                               WHERE u.email = %s""", [email])
            matching_user = cursor.fetchone() # Check their password(although we have hashed and salted tha password before, if we hash and salt the same password again, as the user inputs their password through the below function we should get authenticated:
            if matching_user is not None and bcrypt.checkpw(password_bytes, matching_user.get('hashed_password')):
                return matching_user


def get_user_by_id(user_id):
    """
    If user is present retrieves the user with the given id,
    If there is no matching user, returns None.
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT u.id, u.name, u.email
                                FROM users AS u
                               WHERE u.id = %s""", [user_id])
            matching_user = cursor.fetchone()
            if matching_user is not None:
                return matching_user
