class Customer:
    def __init__(self, name, email, password) -> None:
        self._name = name
        self._email = email
        self._password = password
        pass

    def toArray(self):
        return [self._name, self._email, self._password]
