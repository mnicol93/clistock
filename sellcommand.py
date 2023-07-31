from command import Command


class SellStockCommand(Command):
    def __init__(self, symbol, quantity, fetcher):
        self._symbol = symbol
        self._quantity = quantity
        self._fetcher = fetcher

    def execute():
        return 0
