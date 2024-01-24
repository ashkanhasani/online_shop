class Product:
    def __init__(self, name, price, stock, description, category, image):
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description
        self.category = category
        self.image = image

    @classmethod
    def add(cls):
        name = input(">>> Enter the product name: ")
        price = int(input(">>> Enter the product price: "))
        stock = int(input(">>> Enter the product first stock: "))
        description = input(">>> Enter the product description: ")
        category = input(">>> Enter the product category: ")
        image = input(">>> Enter the url of product image: ")
        return cls(name, price, stock, description, category, image)
