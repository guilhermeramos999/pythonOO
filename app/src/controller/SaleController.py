from src.model.Customer import Customer
from src.model.Product import Product
from src.model.Sale import Sale
from src.database.Database import Database


class SaleController:
    @staticmethod
    def createSale(data):
        data = {'customerId': 1, 'productId': 1}

        customerDb = Database.findOneBy(
            'customer', ['id = ' + str(data['customerId'])])
        
        customerDto = Customer(
            customerDb[1], customerDb[2], customerDb[3])

        productDb = Database.findOneBy(
            'customer', ['id = ' + str(data['productId'])])

        productDto = Product(
            productDb[1], productDb[2], productDb[3])

        saleDto = Sale(customerDto, productDto, productDto._value)

        print(saleDto._customer._name)
