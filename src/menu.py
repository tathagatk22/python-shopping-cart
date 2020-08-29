from common import display_options, get_option_by_choice
from models import login


def login_menu():
    """
    This function will display login menu for the application
    """
    result = display_options(login)
    if result > 0:
        pass
        login_type = get_option_by_choice(login, result - 1)

        if login_type == 1:
            pass
        else:
            pass

    elif result == 0:
        exit()
    else:
        login_menu()



