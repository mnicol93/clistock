from pymongo import MongoClient
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
    client = MongoClient(uri,
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

    def set_buy(symbol, quantity, price):
        # Connect to the sample_airbnb database provided by MongoDB for testing
        db = client['sample_airbnb']
        # Access the collection listingAndReviews
        collection = db['listingsAndReviews']
        return 0

    def set_sell():
        return 0

    def get_portfolio() -> dict:
        return {'key': 'value'}
