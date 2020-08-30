import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Product, ShoppingCart

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


def is_credential_valid(user_input):
    """
    This function will validate the credentials which are being accepted at the time of logging in the application
    """
    user_name = user_input.get("user_name")
    password = user_input.get("password")
    engine = create_db_engine()
    Session = sessionmaker(engine)
    session = Session()
    user_list = session.query(User).filter(User.user_name == user_name, User.password == password).all()
    session.close()
    if len(user_list) > 0:
        return True, user_list[0]
    else:
        return False, None


def add_a_new_user(user_input):
    """
    This function will add the credentials signing in the application
    """
    error = True
    response = None
    user_name = user_input.get("user_name")
    email = user_input.get("email_id")
    password = user_input.get("password")
    full_name = user_input.get("full_name")
    is_admin = user_input.get("are_you_a_admin")
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        session.add(User(
            email=email,
            user_name=user_name,
            password=password,
            fullname=full_name,
            is_admin=is_admin,
            profit=0,
            total_item_bought=0))
        session.commit()
        user_list = session.query(User).filter(User.user_name == user_name)
        response = user_list[0]
        session.close()
        error = False
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response


def add_category(user_input):
    """
    This function will add the credentials signing in the application
    """
    error = True
    response = None
    category_name = user_input.get("Category_Name")
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        session.add(Category(
            items_sold=0,
            category_name=str(category_name).title(),
            profit=0))
        session.commit()
        session.close()
        error = False
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response


def list_all_available_categories():
    error = True
    response = None
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        category_list = []
        category_list_from_db = session.query(Category).all()
        for item in category_list_from_db:
            category_list.append({"name": item.category_name, "id": item.id})
        session.close()
        error = False
        response = category_list
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response


def check_if_user_already_exist(user_input):
    user_name = user_input.get("user_name")
    email = user_input.get("email_id")
    engine = create_db_engine()
    Session = sessionmaker(engine)
    session = Session()
    user_list = session.query(User).filter(User.user_name == user_name, User.email == email).all()
    session.close()
    if len(user_list) > 0:
        return False
    else:
        return True


def add_product(category, user_input):
    """
    This function will add the credentials signing in the application
    """
    error = True
    response = None
    category_id = category.get("id")
    product_name = user_input.get("product_name")
    product_details = user_input.get("product_details")
    buying_price = user_input.get("buying_price")
    selling_price = user_input.get("selling_price")
    remaining_stock = user_input.get("remaining_stock")
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        session.add(Product(product_name=product_name,
                            category_id=category_id,
                            product_details=product_details,
                            buying_price=buying_price,
                            selling_price=selling_price,
                            remaining_stock=remaining_stock,
                            total_quantity_in_cart=0,
                            sold_count=0,
                            profit=0))
        session.commit()
        session.close()
        error = False
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response


def get_all_products_by_category_id(category):
    error = True
    response = None
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        product_list = []
        product_list_from_db = session.query(Product).filter(
            Product.category_id == category.get("id", Product.remaining_stock > 0)).all()
        for item in product_list_from_db:
            product_list.append({"name": item.product_name, "id": item.id, "stock_available": item.remaining_stock,
                                 "buying_price": item.buying_price, "selling_price": item.selling_price})
        session.close()
        error = False
        response = product_list
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response


def update_product_price_and_stock(product_id, user_input):
    """
    This function will add the credentials signing in the application
    """
    error = True
    response = None
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        if "stock_available" in user_input:
            if user_input.get("flag_for_total_quantity_in_cart"):
                product = session.query(Product).filter(Product.id == product_id).one()
                session.query(Product).filter(Product.id == product_id).update(
                    {Product.remaining_stock: user_input.get("stock_available"),
                     Product.total_quantity_in_cart: product.total_quantity_in_cart + user_input.get("quantity")})
            else:
                product = session.query(Product).filter(Product.id == product_id).one()
                session.query(Product).filter(Product.id == product_id).update(
                    {Product.remaining_stock: user_input.get("stock_available"),
                     Product.total_quantity_in_cart: product.total_quantity_in_cart - user_input.get("quantity")})
        else:
            session.query(Product).filter(Product.id == product_id). \
                update({Product.buying_price: user_input.get("buying_price"),
                        Product.selling_price: user_input.get("selling_price"),
                        Product.remaining_stock: user_input.get("remaining_stock")})
        session.commit()
        session.close()
        error = False
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response


def get_product_for_update_stock_and_price(product):
    error = True
    response = None
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        product_info = session.query(Product).filter(Product.id == product.get("id"))
        product = {}
        for item in product_info:
            product.update({"buying_price": item.buying_price,
                            "selling_price": item.selling_price,
                            "remaining_stock": item.remaining_stock})
            session.commit()
            session.close()
            error = False
        response = product
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response


def list_all_carts():
    error = True
    response = None
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        cart_list = []
        cart_list_from_db = session.query(ShoppingCart).all()
        for item in cart_list_from_db:
            cart_list.append(item)
        session.close()
        error = False
        response = cart_list
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response


def add_cart(product, params):
    """
    This function will add the credentials signing in the application
    """
    error = True
    response = None
    total_amount = int(params.get("quantity")) * int(product.get("selling_price"))
    params.update({"total_amount": total_amount,
                   "product": product.get("id"),
                   "is_bought": False})
    # self.user = params.get("user")
    # self.product = params.get("product")
    # self.quantity = params.get("quantity")
    # self.total_amount = params.get("total_amount")
    # self.is_bought = params.get("is_bought")

    # self.user = user
    # self.product = product
    # self.quantity = quantity
    # self.total_amount = total_amount
    # self.is_bought = is_bought
    # self.order_id = order_id
    # product_name = user_input.get("product_name")
    # product_details = user_input.get("product_details")
    # buying_price = user_input.get("buying_price")
    # selling_price = user_input.get("selling_price")
    # remaining_stock = user_input.get("remaining_stock")
    engine = None
    Session = None
    session = None

    try:
        engine = create_db_engine()
        Session = sessionmaker(engine)
        session = Session()
        is_update = False
        session.add(ShoppingCart(is_update=False, params=params))
        session.commit()
        session.close()
        error = False
    except Exception as e:
        response = e.message
    finally:
        if session is not None:
            session.close()
        return error, response
