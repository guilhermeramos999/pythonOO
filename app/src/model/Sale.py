class Sale:
    def __init__(self, customer, product, amount) -> None:
        self._customer = customer
        self._product = product
        self._amount = amount
        pass

    def toArray(self):
        return [self._customer, self._product, self._amount]
