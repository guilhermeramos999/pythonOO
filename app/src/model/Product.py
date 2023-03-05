class Product:
    def __init__(self, name, description, value) -> None:
        self._name = self.validateName(name)
        self._description = self.validateDescription(description)
        self._value = self.validateValue(value)
        pass

    def validateName(self,name):
        if (name != ""):
            return name
        raise ValueError("empty product name")

    def validateDescription(self,description):
        if (description != ""):
            return description
        raise ValueError("empty product description")

    def validateValue(self,value):
        return value
        # print(value)
        # if (value > 1):
        #     return value
        # raise ValueError("invalid value")

    def toArray(self):
        return [self._name, self._description, self._value]
