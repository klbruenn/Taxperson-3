
class Item():
    """
    An Item is priced in pennies (cents),
    and may or may not be considered necessary.
    """
    price = 100
    necessary = True

    def setPrice(self, aPrice):
        self.price = aPrice

    def setNecessary(self, aBoolean):
        self.necessary = aBoolean