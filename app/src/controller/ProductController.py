from src.database.Database import Database
from src.model.Product import Product

class ProductController:
    @staticmethod
    def createProduct(data):

        data = {'name': 'PS5', 'description': 'A Sony Console', 'value': 4499.9}
        try:
            productDto = Product(data['name'], data['description'], data['value'])
            Database.create('product', productDto.toArray())
        except ValueError as e:
            print(e)

    @staticmethod
    def updateProduct(data):

        data = ["name = 'PlayStation 5'"]
        try:
            Database.update('product', data, ['id = 1'])
        except ValueError as e:
            print(e)

    def deleteProduct(data):
        try:
            Database.remove('product', ['id = 1'])
        except ValueError as e:
            print(e)

    def findOneProduct(data):
        try:
            result = Database.findOneBy('product', ['id = 1'])
            print(result)
        except ValueError as e:
            print(e)

    def findAllProducts(data):
        try:
            result = Database.findAll('product')
            print(result)
        except ValueError as e:
            print(e)
