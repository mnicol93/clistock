from command import Command


class SellStockCommand(Command):
    def __init__(self, symbol, quantity, fetcher):
        self._symbol = symbol
        self._quantity = quantity
        self._fetcher = fetcher

    def execute(self):
        data = self._fetcher.get_stock_data(self._symbol, "&summary=true")
        result = self._fetcher.set_sell(self._symbol, self._quantity, data)
        return result
