from sqlalchemy import Column, Integer, Sequence, String, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_name = Column(Text, nullable=False, unique=True)
    password = Column(String(12), nullable=False)
    fullname = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    profit = Column(Integer, nullable=False)
    total_item_bought = Column(Integer, nullable=False)

    def __init__(self, user_name, password, fullname, email, is_admin, profit, total_item_bought):
        self.user_name = user_name
        self.password = password
        self.fullname = fullname
        self.email = email
        self.is_admin = is_admin
        self.profit = profit
        self.total_item_bought = total_item_bought

    def to_json(self):
        return dict(fullname=self.fullname,
                    user_name=self.user_name,
                    email=self.email,
                    is_admin=self.is_admin,
                    profit=self.profit,
                    total_item_bought=self.total_item_bought)


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, Sequence('order_id_seq'), primary_key=True)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    actual_amount_total = Column(Integer, nullable=False)
    discounted_amount = Column(Integer, nullable=False)
    final_amount = Column(Integer, nullable=False)
    created_at = Column(Text, nullable=False)
    profit_by_order = Column(Integer, nullable=False)

    def __init__(self, user, actual_amount_total, discounted_amount, final_amount, created_at, profit_by_oder):
        self.user = user
        self.actual_amount_total = actual_amount_total
        self.discounted_amount = discounted_amount
        self.final_amount = final_amount
        self.created_at = created_at
        self.profit_by_order = profit_by_oder

    def to_json(self):
        return dict(user=self.user,
                    actual_amount_total=self.actual_amount_total,
                    discounted_amount=self.discounted_amount,
                    final_amount=self.final_amount,
                    profit_by_order=self.profit_by_order,
                    created_at=self.created_at)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, Sequence('category_id_seq'), primary_key=True)
    category_name = Column(Text, nullable=False, unique=True)
    profit = Column(Integer, nullable=False)
    items_sold = Column(Integer, nullable=False)

    def __init__(self, category_name, profit, items_sold):
        self.category_name = category_name
        self.items_sold = items_sold
        self.profit = profit

    def to_json(self):
        return dict(category_name=self.category_name,
                    items_sold=self.items_sold,
                    profit=self.profit)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    product_name = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    product_details = Column(Text, nullable=False)
    buying_price = Column(Integer, nullable=False)
    selling_price = Column(Integer, nullable=False)
    remaining_stock = Column(Integer, nullable=False)
    total_quantity_in_cart = Column(Integer, nullable=False)
    sold_count = Column(Integer, nullable=False)
    profit = Column(Integer, nullable=False)

    def __init__(self, product_name, category_id, product_details, buying_price, selling_price, remaining_stock,
                 total_quantity_in_cart, sold_count, profit):
        self.product_name = product_name
        self.category_id = category_id
        self.product_details = product_details
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.remaining_stock = remaining_stock
        self.total_quantity_in_cart = total_quantity_in_cart
        self.sold_count = sold_count
        self.profit = profit

    def to_json(self):
        return dict(product_name=self.product_name,
                    category_id=self.category_id,
                    product_details=self.product_details,
                    buying_price=self.buying_price,
                    selling_price=self.selling_price,
                    remaining_stock=self.remaining_stock,
                    total_quantity_in_cart=self.total_quantity_in_cart,
                    sold_count=self.sold_count,
                    profit=self.profit)


class ShoppingCart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, Sequence('cart_id_seq'), primary_key=True)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
    product = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Integer, nullable=False)
    is_bought = Column(Boolean, nullable=False)
    order_id = Column(Integer, ForeignKey("order.id"))

    def __init__(self, is_update, params):
        if is_update:
            self.user = params.get("user")
            self.product = params.get("product")
            self.quantity = params.get("quantity")
            self.total_amount = params.get("total_amount")
            self.is_bought = params.get("is_bought")
            self.order_id = params.get("order_id")
        else:
            self.user = params.get("user")
            self.product = params.get("product")
            self.quantity = params.get("quantity")
            self.total_amount = params.get("total_amount")
            self.is_bought = params.get("is_bought")

    def to_json(self):
        return dict(user=self.user,
                    product=self.product,
                    quantity=self.quantity,
                    total_amount=self.total_amount,
                    is_bought=self.is_bought,
                    order_id=self.order_id)


login_options = {
    "heading": "Select User Type",
    "options": [
        "Existing",
        "New User",
        "Exit",
    ]
}
new_user_input = {
    "heading": "Please provide valid input",
    "options": [
        "user_name",
        "password",
        "full_name",
        "email_id",
        "are_you_a_admin",
    ]
}
existing_user_input = {
    "heading": "Please provide valid input",
    "options": [
        "user_name",
        "password",
    ]
}
new_user_options = {
    "heading": "Please select",
    "options": [
        "Do you want to continue to application?",
        "Exit",
    ]
}
user_shopping_menu_options = {
    "heading": "Welcome to the store",
    "options": [
        "Go to categories",
        "Go to cart",
        "Go to products which are high in demand",
        "Exit"
    ]
}
admin_shopping_menu_options = {
    "heading": "Welcome to the store",
    "options": [
        "Add category",
        "Add products",
        "Update product stock",
        "Products in cart",
        "Total order placed",
        "Total profit",
        "Exit"
    ]
}
admin_add_category_menu_options = {
    "heading": "Add a new Category",
    "options": [
        "Category Name",
        "Previous menu",
        "Log out",
        "Exit"
    ]
}

admin_add_category_input = {
    "heading": "Please provide valid input",
    "options": [
        "category_name",
    ]
}
user_category_options = {
    "heading": "Please select any category",
    "options": []
}
admin_cart_options = {
    "heading": "Please select any category",
    "options": []
}

admin_update_product_options = {
    "heading": "Please select any product",
    "options": []
}
admin_add_product_input = {
    "heading": "Please provide valid input",
    "options": [
        "product_name",
        "product_details",
        "buying_price",
        "selling_price",
        "remaining_stock",
    ]
}
admin_update_product_input = {
    "heading": "Please provide valid input",
    "options": [
        "buying_price",
        "selling_price",
        "remaining_stock",
    ]
}
user_update_product_input = {
    "heading": "Please provide valid input",
    "options": [
        "quantity"
    ]
}
