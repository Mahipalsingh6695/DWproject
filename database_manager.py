from pymongo import MongoClient
import json

def connect_to_mongodb():
    client = MongoClient("mongodb+srv://Mahipalsingh6695:Mahi_6695@dwproject.q7c0h.mongodb.net/?retryWrites=true&w=majority&appName=dwproject")  # Update with Atlas connection string if needed
    db = client["chatbot_db"]
    collection = db["website_data"]
    return collection

def store_data_in_mongodb(collection, json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        collection.insert_many(data)
        print(f"Inserted {len(data)} records into MongoDB")

if __name__ == "__main__":
    collection = connect_to_mongodb()
    store_data_in_mongodb(collection, "website_data.json")
