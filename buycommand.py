from command import Command


class BuyStockCommand(Command):
    def __init__(self, symbol, price, quantity, fetcher):
        self._symbol = symbol
        self._price = price
        self._quantity = quantity
        self._fetcher = fetcher

    def execute():
        return 0
