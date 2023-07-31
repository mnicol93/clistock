from pymongo import MongoClient
from bson.json_util import dumps, loads
from stock import Stock
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
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

    def get_price(self, ticker, fields) -> str:

        final_url = URL+ticker+fields
        response = requests.get(final_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return "The price of " + data['Symbol'] + '-' + data['Summary']['Name'] + " is: " + str(data['Summary']['Price']) + "$"
        else:
            print("Error in fetching")
        return "0.0"

    def get_stock_data(self, ticker, fields) -> float:

        final_url = URL+ticker+fields
        response = requests.get(final_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error in fetching")
        return 0.0

    def set_buy(self, symbol, quantity, data):
        # Connect to the stocks database
        db = self._client["stocks"]
        # Access the collection portfolio1
        collection = db["portfolio1"]

        result = collection.find_one({"symbol": symbol})

        if result == None:
            collection.insert_one(
                {"symbol": symbol, "quantity": quantity, "price": data['Summary']['Price'], "name": data['Summary']['Name'], "weight": 0, "avg_price": data['Summary']['Price']})
        else:
            old_price = result['quantity'] * result['avg_price']
            new_price = quantity * data['Summary']['Price']
            avg_price = (old_price + new_price) / \
                (quantity + result['quantity'])
            quantity += result['quantity']
            collection.update_one({"symbol": symbol}, {
                                  "$set": {"quantity": quantity, "price": data['Summary']['Price'], "avg_price": avg_price}})
        result = collection.find_one({"symbol": symbol})
        return result

    def set_sell(self, symbol, quantity, data):
        # Connect to the stocks database
        db = self._client["stocks"]
        # Access the collection portfolio1
        collection = db["portfolio1"]
        result = collection.find_one({"symbol": symbol})

        if result == None:
            return None
        else:
            result['quantity'] = result['quantity'] - quantity
            collection.update_one({"symbol": symbol}, {
                                  "$set": {"quantity": result['quantity'], "price": data['Summary']['Price']}})
        return result

    def get_portfolio(self) -> dict:
        # Connect to the stocks database
        db = self._client["stocks"]
        # Access the collection portfolio1
        collection = db["portfolio1"]
        result = collection.find({})
        return result
