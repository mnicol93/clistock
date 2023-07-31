from command import Command


class SellStockCommand(Command):
    def __init__(self, symbol, price, quantity):
        self._symbol = symbol
        self._price = price
        self._quantity = quantity

    def execute():
        return 0
