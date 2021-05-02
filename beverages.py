from decimal import Decimal


class Price:
    def __init__(self, small: Decimal, medium: Decimal, large: Decimal):
        self.small = small
        self.medium = medium
        self.large = large


class Beverage:
    def __init__(self, name: str, _type: str, prices: tuple):
        self.name = name
        self.type = _type
        self.prices = prices


class Coffee(Beverage):
    def __init__(self, name, price):
        Beverage.__init__(self, name, "Coffee", price)


class Soda(Beverage):
    def __init__(self, name, price):
        Beverage.__init__(self, name, "Soda", price)


class Juice(Beverage):
    def __init__(self, name, price):
        Beverage.__init__(self, name, "Juice", price)


menu = [
    Coffee("Espresso", Price(15.0, 18.0, 21.5)),
    Coffee("Americano", Price(10.0, 16.0, 20.0)),
    Coffee("Cappuccino", Price(15.0, 18.0, 21.5)),
    Soda("Coca-Cola", Price(10.0, 15.0, 22.0)),
    Soda("Sprite", Price(10.0, 15.0, 22.0)),
    Soda("Fanta", Price(10.0, 15.0, 22.0)),
    Juice("Oragne Juice", Price(7.0, 14.0, 21.0)),
    Juice("Apple Juice", Price(7.0, 14.0, 21.0)),
    Juice("Pineapple Juice", Price(7.0, 14.0, 21.0)),
]
