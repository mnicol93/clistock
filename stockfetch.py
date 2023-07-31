from pymongo import MongoClient
from bson.json_util import dumps, loads
from stock import Stock
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# TODO: config file for key
headers = {'key': config.get("API", "api_key")}
URL = "https://api.aletheiaapi.com/StockData?symbol="


class StockDataFetcher:
    __instance = None
    uri = config.get("DATABASE", "url")
    # Create a Mongo Client Object
    _client = MongoClient(uri,
                          tls=True,
                          tlsCertificateKeyFile=config.get("DATABASE", "key"))

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(StockDataFetcher, cls).__new__(cls)
        return cls.__instance

    def get_price_str(self, ticker, fields) -> str:

        final_url = URL+ticker+fields
        response = requests.get(final_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return "The price of " + data['Symbol'] + '-' + data['Summary']['Name'] + " is: " + str(data['Summary']['Price']) + "$"
        else:
            print("Error in fetching")
        return "0.0"

    def get_price(self, ticker, fields) -> float:

        final_url = URL+ticker+fields
        response = requests.get(final_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['Summary']['Price']
        else:
            print("Error in fetching")
        return 0.0

    def set_buy(self, symbol, quantity, price):
        # Connect to the stocks database
        db = self._client["stocks"]
        # Access the collection portfolio1
        collection = db["portfolio1"]
        result = collection.find_one({"symbol": symbol})

        if result == None:
            collection.insert_one(Stock(symbol, quantity, price))
        else:
            old_price = result['quantity'] * result['avg_price']
            new_price = quantity * price
            avg_price = (old_price + new_price) / \
                (quantity + result['quantity'])
            quantity += result['quantity']
            collection.update_one({"symbol": symbol}, {
                                  "$set": {"quantity": quantity, "price": price, "avg_price": avg_price}})
        return result

    def set_sell():
        return 0

    def get_portfolio() -> dict:
        return {'key': 'value'}
