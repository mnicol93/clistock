from command import Command


class ShowPortfolio(Command):
    def __init__(self, fetcher):
        self._fetcher = fetcher

    def execute(self):
        result = self._fetcher.get_portfolio()
        return result
