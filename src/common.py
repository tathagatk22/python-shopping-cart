import os

from models import ShoppingCart

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


def display_with_options(params):
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
        flag_for_exit = False
        for option in options:
            index += 1
            if type(option) is dict:
                if "buying_price" in option:
                    print("\n\t " + str(index) + ". " + str(
                        option.get("name").title() + " with price :" + str(option.get("buying_price"))))
                else:
                    print("\n\t " + str(index) + ". " + str(option.get("name").title()))
            elif option in ['Exit', 'Return to Main']:
                flag_for_exit = True
                print("\n\t 0. " + option)
            else:
                print("\n\t " + str(index) + ". " + str(option).title())

        # Accept valid choice and return choice value
        try:
            if flag_for_exit:
                choice = int(input("\n\t Enter your choice (1-" + str(index - 1) + ") : "))
                if choice in range(0, index):
                    print("\n")
                    break
            else:
                choice = int(input("\n\t Enter your choice (1-" + str(index) + ") : "))
                if choice in range(0, index):
                    print("\n")
                    break
        except Exception:
            return -1

    return choice


def display_with_input(params):
    """
    This function will be used to display heading and all the options available
    :param params:
    :return:
    """
    user_input = {}
    sub_heading = params['heading']
    options = params['options']
    clear()
    print("\n\n")
    print("################################################################")
    print("" + adjust_heading(64, heading.replace("", " ").upper()))
    print("################################################################")
    new_sub_heading = sub_heading.replace("", " ").upper()
    print("" + adjust_heading(64, new_sub_heading))
    for item in options:
        if item is "are_you_a_admin":
            while True:
                input_from_cli = raw_input("\n\t Are you a admin y/n:")
                if input_from_cli == "y" or input_from_cli == "Y":
                    user_input.update({item: True})
                    break
                elif input_from_cli == "n" or input_from_cli == "N":
                    user_input.update({item: False})
                    break
                else:
                    continue
        else:
            input_from_cli = raw_input("\n\t Enter value for " + item.replace("_", " ") + " :")
            user_input.update({item: input_from_cli})
    return user_input


def display_with_update_input(params, update_params):
    """
    This function will be used to display heading and all the options available
    :param params:
    :param update_params
    :return:
    """
    user_input = {}
    sub_heading = params['heading']
    options = params['options']
    clear()

    print("\n\n")
    print("################################################################")
    print("" + adjust_heading(64, heading.replace("", " ").upper()))
    print("################################################################")
    new_sub_heading = sub_heading.replace("", " ").upper()
    print("" + adjust_heading(64, new_sub_heading))
    for item in options:
        if item in "buying_price":
            input_from_cli = int(input("\n\t Current value for " + item.replace("_", " ") +
                                       " is " + str(update_params.get("buying_price")) + ", what's the new value :"))
            user_input.update({"buying_price": input_from_cli})
        elif item in "selling_price":
            input_from_cli = int(input("\n\t Current value for " + item.replace("_", " ") +
                                       " is " + str(update_params.get("selling_price")) + ", what's the new value :"))
            user_input.update({"selling_price": input_from_cli})
        elif item in "remaining_stock":
            input_from_cli = int(input("\n\t Current value for " + item.replace("_", " ") +
                                       " is " + str(update_params.get("remaining_stock")) + ", what's the new value :"))
            user_input.update({"remaining_stock": input_from_cli})
        elif item in "quantity":
            while True:
                if update_params.get("remaining_stock") > 0:
                    print("\n\t In how much quantity do you want to purchase, currently available are " +
                          str(update_params.get("remaining_stock")))
                    input_from_cli = int(input("\n\t Please select the quantity :"))
                    if input_from_cli < update_params.get("remaining_stock") and input_from_cli != 0:
                        user_input.update({"quantity": input_from_cli})
                        break
                    else:
                        print("\n\t Please enter a valid input")
                        continue
    return user_input


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


def display_with_cart_params_options(params):
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
        flag_for_exit = False
        total_product_in_cart = 0
        flag_for_shopping_cart = False
        for option in options:
            if isinstance(option, ShoppingCart):
                flag_for_shopping_cart = True
                if not option.is_bought:
                    total_product_in_cart += 1
        if flag_for_shopping_cart:
            print("\n\t Total products available in cart are " + str(total_product_in_cart))
        for option in options:
            index += 1
            if isinstance(option, ShoppingCart):
                products = params.get("products")
                for product_item in products:
                    if product_item.id == option.product:
                        print("\n\t " + str(index) + ". Product Name : " + str(product_item.product_name).title()
                              + " with price :" + str(product_item.selling_price)
                              + " and quantity :" + str(option.quantity)
                              + " and total price :" + str(option.total_amount))
        index += 1
        print("\n\t " + str(index) + ". If you want to remove items from cart")
        index += 1
        print("\n\t " + str(index) + ". If you want to checkout?")
        index += 1
        flag_for_exit = True
        print("\n\t " + str(0) + ". Exit")
        # Accept valid choice and return choice value
        try:
            if flag_for_exit:
                choice = int(input("\n\t Enter your choice (1-" + str(index -1) + ") : "))
                if choice in range(0, index):
                    print("\n")
                    break
        except Exception:
            return -1

    return choice
