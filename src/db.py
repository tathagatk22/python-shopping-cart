import os

from sqlalchemy import create_engine

from models import Base

DB_Name = None
DB_User = None
DB_Password = None
DB_Host = None
DB_Port = None


def check_for_env():
    """
    This function will be used to extract and assign values from environment variables to variables
    """
    global DB_Name, DB_Host, DB_User, DB_Password, DB_Host, DB_Port
    DB_Name = os.getenv("DB_Name")
    if DB_Name is None:
        raise Exception("env DB_Name not found")
    DB_User = os.getenv("DB_User")
    if DB_Name is None:
        raise Exception("env DB_User not found")
    DB_Password = os.getenv("DB_Password")
    if DB_Name is None:
        raise Exception("env DB_Password not found")
    DB_Host = os.getenv("DB_Host")
    if DB_Name is None:
        raise Exception("env DB_Host not found")
    DB_Port = os.getenv("DB_Port")
    if DB_Name is None:
        raise Exception("env DB_Port not found")


def create_db_engine():
    """
    This function will connect to postgres database engine using environment variables as credentials
    """
    check_for_env()
    db_string = "postgres://%s:%s@%s:%s/%s" % (DB_User, DB_Password, DB_Host, DB_Port, DB_Name)
    return create_engine(db_string)


def create_schema():
    """
    This function will be used to create schemas required for the application
    """
    engine = create_db_engine()
    # to create all the models
    Base.metadata.create_all(engine)
