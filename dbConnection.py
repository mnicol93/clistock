from pymongo import MongoClient

# URI information will go on a config file
uri = "mongodb+srv://cluster0.bzpteb1.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
# Create a Mongo Client Object
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='C:\\Users\\Marc\\Documents\\School\\McMaster\\McMaster\\Semester2\\4SA3\\clistock\\X509-cert-744441256714543753.pem')
# Connect to the sample_airbnb database provided by MongoDB for testing
db = client['sample_airbnb']
# Access the collection listingAndReviews
collection = db['listingsAndReviews']
# Access the document with the given ID
result = collection.find_one({"_id": "1001265"})
print(result["name"])
# Access the document with the given ID, delete it from the database
collection.delete_one({"_id": "1001265"})
# Access the document with the given ID
result = collection.find_one({"_id": "1001265"})
# Print the name of result. It won't be found since it was previously deleted
if (result != None):
    print(result["name"])
else:
    print("Result not found!")
