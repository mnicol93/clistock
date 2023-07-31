from command import Command


class BuyStockCommand(Command):
    def __init__(self, symbol, quantity, fetcher):
        self._symbol = symbol
        self._quantity = quantity
        self._fetcher = fetcher

    def execute(self):
        price = self._fetcher.get_price("msft", "&summary=true")
        return 0
