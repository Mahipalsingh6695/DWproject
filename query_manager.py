from pymongo import MongoClient

def search_database(query):
    client = MongoClient("mongodb+srv://Mahipalsingh6695:Mahi_6695@dwproject.q7c0h.mongodb.net/?retryWrites=true&w=majority&appName=dwproject")
    db = client["chatbot_db"]
    collection = db["website_data"]

    results = collection.find({"cleaned_text": {"$regex": query, "$options": "i"}})
    return [result["text"] for result in results]

if __name__ == "__main__":
    query = "example"  # Replace with user input
    results = search_database(query)
    print(f"Search Results: {results}")
