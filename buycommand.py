from command import Command


class BuyStockCommand(Command):
    def __init__(self, symbol, quantity, fetcher):
        self._symbol = symbol
        self._quantity = quantity
        self._fetcher = fetcher

    def execute(self):
        price = self._fetcher.get_price(self._symbol, "&summary=true")
        result = self._fetcher.set_buy(self._symbol, self._quantity, price)
        return result
