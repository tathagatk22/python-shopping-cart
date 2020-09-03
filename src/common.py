import os

from models import *

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


def get_product_by_id(product_id, product_list):
    error = True
    product_to_return = None
    for product in product_list:
        if product.id == product_id:
            error = False
            product_to_return = product
    return error, product_to_return


def display_with_options(params):
    """
    This function will be used to display heading and all the options available
    :param params:
    :return:
    """
    sub_heading = params['heading']
    options = params['options']
    product_list = []
    user_list = []
    if "user_list" in params:
        user_list = params["user_list"]
    if "product_list" in params:
        product_list = params["product_list"]
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
        flag_for_order = False
        flag_for_model = False
        flag_for_all_shopping_cart = False
        for option in options:
            index += 1
            if isinstance(option, ShoppingCart):
                flag_for_model = True
                if "products" in params:
                    products = params.get("products")
                    for product_item in products:
                        if product_item.id == option.product:
                            print("\n\t" + str(index) + ". Product Name : " + str(product_item.product_name).title())
                            print("\n\t   Price :" + str(product_item.selling_price))
                            print("\n\t   Quantity :" + str(option.quantity))
                            print("\n\t   Total Price :" + str(option.total_amount))
                else:
                    flag_for_all_shopping_cart = True
                    for user in user_list:
                        error, product = get_product_by_id(option.product, product_list)
                        if error:
                            continue
                        else:
                            if user.id == option.user:
                                is_bought = ""
                                if option.is_bought:
                                    is_bought = "yes"
                                else:
                                    is_bought = "no"
                                print("\n\t" + str(index) + ". User : " + str(user.fullname).title())
                                print("\n\t   Product Name : " + str(product.product_name).title())
                                print("\n\t   Quantity :" + str(option.quantity))
                                print("\n\t   Total Price :" + str(option.total_amount))
                                print("\n\t   Is sold? :" + str(is_bought)).title()
            if isinstance(option, User):
                flag_for_model = True
                print("\n\t" + str(index) + ". Name : " + str(option.fullname).title())
                print("\n\t   Email :" + str(option.email))
                print("\n\t   Total item bought :" + str(option.total_item_bought))
                print("\n\t   User name :" + str(option.user_name))
            if isinstance(option, Order):
                flag_for_order = True
                flag_for_model = True
                print("\n\t" + str(index) + ". Dated at : " + str(option.created_at))
                print("\n\t   Discount amount :" + str(option.discounted_amount))
                print("\n\t   Total amount for order :" + str(option.final_amount))
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
                if flag_for_model:
                    continue
                print("\n\t " + str(index) + ". " + str(option).title())

        if flag_for_all_shopping_cart:
            print ("\n\n\n")
            index = 0
            print("\n\t " + str(0) + ". Exit to main menu")
        elif flag_for_order:
            print ("\n\n\n")
            flag_for_exit = True
            index = 0
            print("\n\t " + str(0) + ". Exit to main menu")
            index += 1
            print("\n\t " + str(index) + ". View another user order details")

        # Accept valid choice and return choice value
        try:
            if flag_for_all_shopping_cart:
                choice = int(input("\n\t Enter your choice (0) : "))
                if choice in range(0, 1):
                    print("\n")
                    break
            elif flag_for_exit:
                choice = int(input("\n\t Enter your choice (1-" + str(index - 1) + ") : "))
                if choice in range(0, index + 1):
                    print("\n")
                    break
            else:
                choice = int(input("\n\t Enter your choice (1-" + str(index) + ") : "))
                if choice in range(1, index + 1):
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
            while True:
                try:
                    if item in "quantity":
                        input_from_cli = int(input("\n\t Enter value for " + item.replace("_", " ").title() + " : "))
                        user_input.update({item: input_from_cli})
                        break
                    else:
                        input_from_cli = raw_input("\n\t Enter value for " + item.replace("_", " ").title() + " : ")
                        user_input.update({item: input_from_cli})
                        break
                except Exception:
                    return -1
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
        elif item in "stock_available":
            input_from_cli = int(input("\n\t Current value for " + item.replace("_", " ") +
                                       " is " + str(update_params.get("stock_available")) + ", what's the new value :"))
            user_input.update({"stock_available": input_from_cli})
        elif item in "quantity":
            while True:
                if update_params.get("stock_available") > 0:
                    print("\n\t In how much quantity do you want to purchase, currently available are " +
                          str(update_params.get("stock_available")))
                    input_from_cli = int(input("\n\t Please select the quantity :"))
                    if input_from_cli <= update_params.get("stock_available") and input_from_cli != 0:
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
                    total_product_in_cart += option.quantity
        if flag_for_shopping_cart:
            print("\n\t Total products available in cart are " + str(total_product_in_cart))
        for option in options:
            index += 1
            if isinstance(option, ShoppingCart):
                products = params.get("products")
                for product_item in products:
                    if product_item.id == option.product:
                        print("\n\t" + str(index) + ". Product Name : " + str(product_item.product_name).title())
                        print("\n\t   Price :" + str(product_item.selling_price))
                        print("\n\t   Quantity :" + str(option.quantity))
                        print("\n\t   Total Price :" + str(option.total_amount))
        print ("\n\n\n")
        index = 0
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
                choice = int(input("\n\t Enter your choice (1-" + str(index - 1) + ") : "))
                if choice in range(0, index):
                    print("\n")
                    break
        except Exception:
            return -1

    return choice
