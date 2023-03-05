from src.database.Database import Database
from src.model.Customer import Customer


class CustomerController:
    @staticmethod
    def createCustomer(data):

        data = {'name': 'fic-name',
                'email': 'fic-email@mail.com', 'password': 'pass123'}
        try:
            customerDto = Customer(
                data['name'], data['email'], data['password'])
            Database.create('customer', customerDto.toArray())
        except ValueError as e:
            print(e)

    @staticmethod
    def updateCustomer(data):

        data = ["password = '321pass'"]
        try:
            Database.update('customer', data, ['id = 1'])
        except ValueError as e:
            print(e)

    def deleteCustomer(data):
        try:
            Database.remove('customer', ['id = 1'])
        except ValueError as e:
            print(e)

    def findOneCustomer(data):
        try:
            result = Database.findOneBy('customer', ['id = 1'])
            print(result)
        except ValueError as e:
            print(e)

    def findAllCustomers(data):
        try:
            result = Database.findAll('customer')
            print(result)
        except ValueError as e:
            print(e)
