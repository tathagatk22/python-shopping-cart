from common import *
from models import *
from db import *
from models import User


def login_menu():
    """
    This function will display login menu for the application
    """
    result = display_with_options(login_options)
    if result > 0:
        if result == 1:
            # if the user is existing
            user = None
            while True:
                user_input = display_with_input(existing_user_input)
                is_successful, user = is_credential_valid(user_input)
                if is_successful:
                    # if the credential are valid
                    break

                else:
                    #  if the credentials are invalid
                    print("\n\t Incorrect Credentials found")
                    while True:
                        retry_sign_up_failed_input = raw_input("\n\t Do you want to try it again y/n:")
                        if retry_sign_up_failed_input == "y" or retry_sign_up_failed_input == "Y":
                            break
                        elif retry_sign_up_failed_input == "n" or retry_sign_up_failed_input == "N":
                            exit()
                        else:
                            # if the input is incorrect
                            continue
                    # will be going to try again for the login
                    continue
            shopping_menu(user)
        else:
            # will be going to add a new user
            while True:
                user_input = display_with_input(new_user_input)
                if check_if_user_already_exist(user_input):
                    # adding new user in database
                    error, response_new_user = add_a_new_user(user_input)
                    if error:
                        # if there is any issues
                        print("\n\t %s" % response_new_user)
                        while True:
                            # will ask user to retry 
                            retry_sign_up_failed_input = raw_input("\n\t Do you want to try it again y/n:")
                            if retry_sign_up_failed_input == "y" or retry_sign_up_failed_input == "Y":
                                # if the user wants to retry
                                break
                            elif retry_sign_up_failed_input == "n" or retry_sign_up_failed_input == "N":
                                exit()
                            else:
                                # if the input is incorrect
                                continue
                        # user will prompted again for the details
                        continue
                    else:
                        while True:
                            # if the user is successfully logged in to the application
                            new_user_option_from_menu = display_with_options(new_user_options)
                            if new_user_option_from_menu == 0:
                                # if the user want to exit
                                exit()
                            elif new_user_option_from_menu == 1:
                                # if the user wants to go to the shopping_menu
                                shopping_menu(response_new_user)
                            else:
                                # if the input is incorrect
                                continue
                        continue
                else:
                    # if the user is already present
                    print("User already exist with same username and email-id, please try another username or email-id")
                    continue

    elif result == 0:
        exit()
    else:
        login_menu()


def shopping_menu(user):
    """
    This function will display shopping menu for the application
    """
    if isinstance(user, User):
        while True:
            if user.is_admin:
                result = display_with_options(admin_shopping_menu_options)
                if result == 0:
                    exit()
                elif result == 1:  # Add Category
                    admin_add_category_result = display_with_options(admin_add_category_menu_options)
                    if admin_add_category_result == 1:
                        while True:
                            user_input = display_with_input(admin_add_category_input)
                            error, response_add_category = add_category(user_input)
                            if error:
                                # if there is any issues
                                print("\n \t%s" % response_add_category)
                                while True:
                                    # will ask user to retry 
                                    retry = raw_input("\n\t Do you want to try it again y/n:")
                                    if retry == "y" or retry == "Y":
                                        # if the user wants to retry
                                        break
                                    elif retry == "n" or retry == "N":
                                        exit()
                                    else:
                                        # if the input is incorrect
                                        continue
                                # user will prompted again for the details
                                continue
                            else:
                                retry = ""
                                while True:
                                    retry = raw_input("\n\t Do you want to try it again y/n:")
                                    if retry == "y" or retry == "Y":
                                        # if the user wants to retry
                                        break
                                    elif retry == "n" or retry == "N":
                                        break
                                    else:
                                        # if the input is incorrect
                                        continue
                                if retry == "y" or retry == "Y":
                                    # if the user wants to retry
                                    continue
                                elif retry == "n" or retry == "N":
                                    break
                    elif admin_add_category_result == 2:
                        continue
                    elif admin_add_category_result == 3:
                        break
                    else:
                        exit()
                elif result == 2:  # Add Products
                    while True:
                        error, list_of_categories = list_all_available_categories()
                        if error:
                            print("\n\t %s" % list_of_categories)
                            while True:
                                # will ask user to retry 
                                retry_getting_input = raw_input(
                                    "\n\t Do you want to try it again y/n:")
                                if retry_getting_input == "y" or retry_getting_input == "Y":
                                    # if the user wants to retry
                                    break
                                elif retry_getting_input == "n" or retry_getting_input == "N":
                                    exit()
                                else:
                                    # if the input is incorrect
                                    continue
                            # user will prompted again for the details
                            continue
                        else:
                            if len(list_of_categories) == 0:
                                print ("No categories are available, please add category first")
                                break
                            user_category_options.update({"options": list_of_categories})
                            user_input_for_category = display_with_options(user_category_options)
                            if user_input_for_category == -1:
                                print("\n\t Incorrect Input")
                                continue
                            else:
                                user_input_of_product_information = display_with_input(admin_add_product_input)
                                error, response_add_product = add_product(list_of_categories[user_input_for_category],
                                                                          user_input_of_product_information)
                                if error:
                                    # if there is any issues
                                    print("\n \t%s" % response_add_product)
                                    while True:
                                        # will ask user to retry
                                        retry = raw_input("\n\t Do you want to try it again y/n:")
                                        if retry == "y" or retry == "Y":
                                            # if the user wants to retry
                                            break
                                        elif retry == "n" or retry == "N":
                                            exit()
                                        else:
                                            # if the input is incorrect
                                            continue
                                    # user will prompted again for the details
                                    continue
                                else:
                                    retry = ""
                                    while True:
                                        print("\n\t Success!!!!")
                                        retry = raw_input("\n\t Do you want to try it again y/n:")
                                        if retry == "y" or retry == "Y":
                                            # if the user wants to retry
                                            break
                                        elif retry == "n" or retry == "N":
                                            break
                                        else:
                                            # if the input is incorrect
                                            continue
                                    if retry == "y" or retry == "Y":
                                        # if the user wants to retry
                                        continue
                                    elif retry == "n" or retry == "N":
                                        break
                elif result == 3:  # Update Product Stock
                    while True:
                        error, list_of_categories = list_all_available_categories()
                        if error:
                            print("\n\t %s" % list_of_categories)
                            while True:
                                # will ask user to retry 
                                retry_getting_input = raw_input(
                                    "\n\t Do you want to try it again y/n:")
                                if retry_getting_input == "y" or retry_getting_input == "Y":
                                    # if the user wants to retry
                                    break
                                elif retry_getting_input == "n" or retry_getting_input == "N":
                                    exit()
                                else:
                                    # if the input is incorrect
                                    continue
                            # user will prompted again for the details
                            continue
                        else:
                            if len(list_of_categories) == 0:
                                print ("No categories are available, please add category first")
                                break
                            # list of categories has been identified
                            user_category_options.update({"options": list_of_categories})
                            user_input_for_category = display_with_options(user_category_options)
                            if user_input_for_category == -1:
                                print("\n\t Incorrect Input")
                                continue
                            else:
                                # on which category the product needs to be updated
                                # extracting all the products available by category_id
                                error, response_product_by_category_id = get_all_products_by_category_id(
                                    list_of_categories[user_input_for_category])
                                if error:
                                    # if there is any issues
                                    print("\n\t %s" % response_product_by_category_id)
                                    while True:
                                        # will ask user to retry
                                        retry_input = raw_input("\n\t Do you want to try it again y/n:")
                                        if retry_input == "y" or retry_input == "Y":
                                            # if the user wants to retry
                                            break
                                        elif retry_input == "n" or retry_input == "N":
                                            exit()
                                        else:
                                            # if the input is incorrect
                                            continue
                                    # user will prompted again for the details
                                    continue
                                else:
                                    # after getting all the products
                                    admin_update_product_options.update({"options": response_product_by_category_id})
                                    # user needs to select a product
                                    product_id = display_with_options(admin_update_product_options)
                                    if product_id == -1:
                                        print("\n\t Incorrect Input")
                                        continue
                                    else:

                                        error, product_info = get_product_for_update_stock_and_price(
                                            response_product_by_category_id[product_id])
                                        if error:
                                            pass
                                        else:

                                            user_input = display_with_update_input(admin_update_product_input,
                                                                                   product_info)
                                            error, response_update_product = update_product_price_and_stock(product_id,
                                                                                                            user_input)
                                            if error:
                                                # if there is any issues
                                                print("\n \t%s" % response_update_product)
                                                while True:
                                                    # will ask user to retry
                                                    retry = raw_input("\n\t Do you want to try it again y/n:")
                                                    if retry == "y" or retry == "Y":
                                                        # if the user wants to retry
                                                        break
                                                    elif retry == "n" or retry == "N":
                                                        exit()
                                                    else:
                                                        # if the input is incorrect
                                                        continue
                                                # user will prompted again for the details
                                                continue
                                            else:
                                                retry = ""
                                                print("\n\t Success!!!!")
                                                while True:
                                                    retry = raw_input("\n\t Do you want to try it again y/n:")
                                                    if retry == "y" or retry == "Y":
                                                        # if the user wants to retry
                                                        break
                                                    elif retry == "n" or retry == "N":
                                                        break
                                                    else:
                                                        # if the input is incorrect
                                                        continue
                                                if retry == "y" or retry == "Y":
                                                    # if the user wants to retry
                                                    continue
                                                elif retry == "n" or retry == "N":
                                                    break
                elif result == 4:  # for Products In Cart
                    while True:
                        error, list_of_pending_carts = list_all_carts()
                        if error:
                            print("\n\t %s" % list_of_pending_carts)
                            while True:
                                # will ask user to retry
                                retry_getting_input = raw_input(
                                    "\n\t Do you want to try it again y/n:")
                                if retry_getting_input == "y" or retry_getting_input == "Y":
                                    # if the user wants to retry
                                    break
                                elif retry_getting_input == "n" or retry_getting_input == "N":
                                    exit()
                                else:
                                    # if the input is incorrect
                                    continue
                            # user will prompted again for the details
                            continue
                        else:
                            if len(list_of_pending_carts) == 0:
                                print ("No shopping carts are available, please add items in cart first")
                                break
                            # list of categories has been identified
                            admin_cart_options.update({"options": list_of_pending_carts})
                            user_input_for_category = display_with_options(admin_cart_options)
                            if user_input_for_category == -1:
                                print("\n\t Incorrect Input")
                                continue
                            else:
                                # on which category the product needs to be updated
                                # extracting all the products available by category_id
                                error, response_product_by_category_id = get_all_products_by_category_id(
                                    user_input_for_category)
                                if error:
                                    # if there is any issues
                                    print("\n\t %s" % response_product_by_category_id)
                                    while True:
                                        # will ask user to retry
                                        retry_input = raw_input("\n\t Do you want to try it again y/n:")
                                        if retry_input == "y" or retry_input == "Y":
                                            # if the user wants to retry
                                            break
                                        elif retry_input == "n" or retry_input == "N":
                                            exit()
                                        else:
                                            # if the input is incorrect
                                            continue
                                    # user will prompted again for the details
                                    continue
                                else:
                                    # after getting all the products
                                    admin_update_product_options.update({"options": response_product_by_category_id})
                                    # user needs to select a product
                                    product_id = display_with_options(admin_update_product_options) - 1
                                    if product_id == -1:
                                        print("\n\t Incorrect Input")
                                        continue
                                    else:
                                        product_info = get_product_for_update_stock_and_price(product_id)
                                        user_input = display_with_update_input(admin_update_product_input, product_info)
                                        error, response_update_product = update_product_price_and_stock(product_id,
                                                                                                        user_input)
                                        if error:
                                            # if there is any issues
                                            print("\n \t%s" % response_update_product)
                                            while True:
                                                # will ask user to retry
                                                retry = raw_input("\n\t Do you want to try it again y/n:")
                                                if retry == "y" or retry == "Y":
                                                    # if the user wants to retry
                                                    break
                                                elif retry == "n" or retry == "N":
                                                    exit()
                                                else:
                                                    # if the input is incorrect
                                                    continue
                                            # user will prompted again for the details
                                            continue
                                        else:
                                            retry = ""
                                            while True:
                                                retry = raw_input("\n\t Do you want to try it again y/n:")
                                                if retry == "y" or retry == "Y":
                                                    # if the user wants to retry
                                                    break
                                                elif retry == "n" or retry == "N":
                                                    break
                                                else:
                                                    # if the input is incorrect
                                                    continue
                                            if retry == "y" or retry == "Y":
                                                # if the user wants to retry
                                                continue
                                            elif retry == "n" or retry == "N":
                                                break
                elif result == 5:
                    pass
                elif result == 6:
                    pass
                elif result == 7:
                    pass
            else:
                result = display_with_options(user_shopping_menu_options)
                if result == 0:  # exit
                    exit()
                elif result == 1:
                    while True:
                        error, list_of_categories = list_all_available_categories()
                        if error:
                            print("\n\t %s" % list_of_categories)
                            while True:
                                # will ask user to retry
                                retry_getting_input = raw_input(
                                    "\n\t Do you want to try it again y/n:")
                                if retry_getting_input == "y" or retry_getting_input == "Y":
                                    # if the user wants to retry
                                    break
                                elif retry_getting_input == "n" or retry_getting_input == "N":
                                    exit()
                                else:
                                    # if the input is incorrect
                                    continue
                            # user will prompted again for the details
                            continue
                        else:
                            if len(list_of_categories) == 0:
                                print ("No categories are available, please add category first")
                                break
                            user_category_options.update({"options": list_of_categories})
                            user_input_for_category = display_with_options(user_category_options)
                            if user_input_for_category == -1:
                                print("\n\t Incorrect Input")
                                continue
                            else:
                                error, response_product_by_category_id = get_all_products_by_category_id(
                                    list_of_categories[user_input_for_category - 1])
                                if error:
                                    # if there is any issues
                                    print("\n\t %s" % response_product_by_category_id)
                                    while True:
                                        # will ask user to retry
                                        retry_input = raw_input("\n\t Do you want to try it again y/n:")
                                        if retry_input == "y" or retry_input == "Y":
                                            # if the user wants to retry
                                            break
                                        elif retry_input == "n" or retry_input == "N":
                                            exit()
                                        else:
                                            # if the input is incorrect
                                            continue
                                    # user will prompted again for the details
                                    continue
                                else:
                                    # after getting all the products
                                    if len(response_product_by_category_id) == 0:
                                        print ("No Products are available, please add products first")
                                        break
                                    else:
                                        admin_update_product_options.update(
                                            {"options": response_product_by_category_id})
                                        # user needs to select a product
                                        product_id = display_with_options(admin_update_product_options)
                                        if product_id == -1:
                                            print("\n\t Incorrect Input")
                                            continue
                                        else:

                                            error, product_info = get_product_for_update_stock_and_price(
                                                response_product_by_category_id[product_id - 1])
                                            if error:
                                                # if there is any issues
                                                print("\n \t%s" % product_info)
                                                while True:
                                                    # will ask user to retry
                                                    retry = raw_input("\n\t Do you want to try it again y/n:")
                                                    if retry == "y" or retry == "Y":
                                                        # if the user wants to retry
                                                        break
                                                    elif retry == "n" or retry == "N":
                                                        exit()
                                                    else:
                                                        # if the input is incorrect
                                                        continue
                                                # user will prompted again for the details
                                                continue
                                            else:
                                                user_input = display_with_update_input(user_update_product_input,
                                                                                       product_info)
                                                product = response_product_by_category_id[product_id]
                                                user_input.update({"user": user.id})
                                                error, response_add_cart = add_cart(product, user_input)
                                                if error:
                                                    # if there is any issues
                                                    print("\n \t%s" % response_add_cart)
                                                    while True:
                                                        # will ask user to retry
                                                        retry = raw_input("\n\t Do you want to try it again y/n:")
                                                        if retry == "y" or retry == "Y":
                                                            # if the user wants to retry
                                                            break
                                                        elif retry == "n" or retry == "N":
                                                            exit()
                                                        else:
                                                            # if the input is incorrect
                                                            continue
                                                    # user will prompted again for the details
                                                    continue
                                                else:
                                                    quantity = user_input.get("quantity")
                                                    product.update({"quantity": quantity,
                                                                    "flag_for_total_quantity_in_cart": True,
                                                                    "stock_available": product.get(
                                                                        "stock_available") - quantity})
                                                    error, response_update_product = update_product_price_and_stock(
                                                        product.get("id"), product)
                                                    if error:
                                                        # if there is any issues
                                                        print("\n \t%s" % response_update_product)
                                                        while True:
                                                            # will ask user to retry
                                                            retry = raw_input("\n\t Do you want to try it again y/n:")
                                                            if retry == "y" or retry == "Y":
                                                                # if the user wants to retry
                                                                break
                                                            elif retry == "n" or retry == "N":
                                                                exit()
                                                            else:
                                                                # if the input is incorrect
                                                                continue
                                                        # user will prompted again for the details
                                                        continue
                                                    else:
                                                        retry = ""
                                                        print("\n\t Success!!!!")
                                                        while True:
                                                            retry = raw_input("\n\t Do you want to try it again y/n:")
                                                            if retry == "y" or retry == "Y":
                                                                # if the user wants to retry
                                                                break
                                                            elif retry == "n" or retry == "N":
                                                                break
                                                            else:
                                                                # if the input is incorrect
                                                                continue
                                                        if retry == "y" or retry == "Y":
                                                            # if the user wants to retry
                                                            continue
                                                        elif retry == "n" or retry == "N":
                                                            break
                elif result == 2:
                    while True:
                        error, list_of_pending_carts = list_all_carts()
                        if error:
                            print("\n\t %s" % list_of_pending_carts)
                            while True:
                                # will ask user to retry
                                retry_getting_input = raw_input(
                                    "\n\t Do you want to try it again y/n:")
                                if retry_getting_input == "y" or retry_getting_input == "Y":
                                    # if the user wants to retry
                                    break
                                elif retry_getting_input == "n" or retry_getting_input == "N":
                                    exit()
                                else:
                                    # if the input is incorrect
                                    continue
                            # user will prompted again for the details
                            continue
                        else:
                            if len(list_of_pending_carts) == 0:
                                print ("No shopping carts are available, please add items in cart first")
                                break
                            # list of categories has been identified
                            user_cart_options.update({"options": list_of_pending_carts})
                            error, response_product = get_all_products()
                            if error:
                                pass
                            else:
                                user_cart_options.update({"products": response_product})
                                user_input_for_category = display_with_cart_params_options(user_cart_options)
                                if user_input_for_category == -1:
                                    print("\n\t Incorrect Input")
                                    continue
                                else:
                                    pass
        login_menu()
