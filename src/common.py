import os

heading = "SCALEREAL E-COMMERCE STORE"


def clear():
    """
    This function will be used to clear the the current output present on the screen
    :return:
    """
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


def display_options(params):
    """
    This function will be used to display heading and all the options available
    :param params:
    :return:
    """
    sub_heading = params['heading']
    options = params['options']
    while True:
        clear()
        print("\n\n")
        print("################################################################")
        print("" + adjust_heading(64, heading.replace("", " ").upper()))
        print("################################################################")
        new_sub_heading = sub_heading.replace("", " ").upper()
        print("" + adjust_heading(64, new_sub_heading))

        # Display list of options
        index = 0
        for option in options:
            index += 1
            if option in ['Exit', 'Return to Main']:
                print("\n\t 0. " + option)
            else:
                print("\n\t " + str(index) + ". " + option)

        # Accept valid choice and return choice value
        try:
            choice = input("\n\t Enter your choice (1-" + str(index - 1) + ") : ")
            if choice in range(0, index):
                print("\n")
                break
        except Exception:
            return -1

    return choice


def adjust_heading(total_char, heading):
    """
    This function will adjust the heading according to the total_har
    :param total_char:
    :param heading:
    :return:
    """
    white_space = ' '
    if (total_char - len(heading)) % 2 == 0:
        spaces_count = (total_char - len(heading)) / 2
        return white_space * spaces_count + heading + white_space * spaces_count
    else:
        front_spaces_count = (total_char - len(heading)) / 2
        end_spaces_count = ((total_char - len(heading)) / 2) + 1
        return white_space * front_spaces_count + heading + white_space * end_spaces_count


def get_option_by_choice(data, choice):
    """
    This function will be used get the choice available in data
    :param data:
    :param choice:
    :return:
    """
    options = data.get('options', [])
    return options[choice]
