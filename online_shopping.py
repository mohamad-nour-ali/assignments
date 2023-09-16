class product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ("quantity cannot be negative")

    def display_details(self) -> str:
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")


class discountProduct(product):
    def __init__(self, name: str, price: float, quantity: int, discount_percentage) -> None:
        super().__init__(name, price, quantity)
        if 0 <= discount_percentage <= 100:
            self.discount_percentage = discount_percentage
        else:
            raise ("discount persintage should be between 0 and 100")

    def display_details(self) -> str:
        super().display_details()
        print(f"Discount in persentage is : {self.discount_percentage}%")


class shopingCart:
    def __init__(self, products: list = []) -> None:
        self.products = products

    def add_product(self, product: object) -> None:
        self.products.append(product)

    def remove_product(self, product) -> None:
        if product in self.products:
            self.products.remove(product)
        else:
            raise ("this product is not exist in cart")

    def view_cart(self) -> str:
        for product in self.products:
            product.display_details()
            print("*****")


class user(shopingCart):
    def __init__(self, user_name: str, email: str,  products: list = []) -> None:
        super().__init__(products)
        self.user_name = user_name
        self.email = email

    def view_cart(self) -> str:
        return super().view_cart()

    def checkout(self) -> str:
        print(f"Dear {self.user_name}")
        super().view_cart()
        self.products = []


class order:
    def __init__(self, products=[]) -> None:
        self.products = products

    def desplay_products(self) -> None:
        print("your orders :")
        for product in self.products:
            product.display_details()
            print("*******")


# Create products
product1 = product("Laptop", 999.99, 5)
product2 = product(",ous", 999.99, 5)
discounted_product = discountProduct("Smartphone", 499.99, 10, 15)
user_order = order([product1, product2, discounted_product])
# Create a user and add products to the cart
user = user("John", "john@example.com")
user.add_product(product1)
user.add_product(product2)
user.add_product(discounted_product)


# View the user's cart
# user.view_cart()

# View the user's order
# user_order.desplay_products()

# Checkout the cart
# user.checkout()
