import nltk
from pymongo import MongoClient

nltk.download('punkt')

def clean_text(text):
    # Tokenize, lowercase, and remove stopwords or punctuation
    tokens = nltk.word_tokenize(text.lower())
    return " ".join(tokens)

def preprocess_data():
    client = MongoClient("mongodb+srv://Mahipalsingh6695:Mahi_6695@dwproject.q7c0h.mongodb.net/?retryWrites=true&w=majority&appName=dwproject")
    db = client["chatbot_db"]
    collection = db["website_data"]

    for document in collection.find():
        cleaned_text = clean_text(document["text"])
        collection.update_one(
            {"_id": document["_id"]},
            {"$set": {"cleaned_text": cleaned_text}}
        )

    print("Data preprocessing completed.")

if __name__ == "__main__":
    preprocess_data()
