# from flask import Flask, request, jsonify, render_template
# from pymongo import MongoClient
# import openai
# import os

# app = Flask(__name__)

# # MongoDB setup
# client = MongoClient(os.getenv('MONGO_URI'))
# db = client['chatbot']
# collection = db['data']

# # OpenAI setup
# openai.api_key = os.getenv('OPENAI_API_KEY')

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_message = request.json.get("message")
#     try:
#         # Check MongoDB for a matching response
#         db_response = collection.find_one({"content": {"$regex": user_message, "$options": "i"}})
#         if db_response:
#             return jsonify({"reply": f"From database: {db_response['content']}"})
        
#         # Use OpenAI for AI-based response
#         ai_response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=f"You are a helpful chatbot. Answer: {user_message}",
#             max_tokens=150
#         )
#         return jsonify({"reply": ai_response.choices[0].text.strip()})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
