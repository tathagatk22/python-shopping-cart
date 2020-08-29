from db import create_schema
from menu import login_menu


def init():
    """
    This function will be initialized at the initial stage of the application
    """
    create_schema()


if __name__ == '__main__':
    init()
    login_menu()

