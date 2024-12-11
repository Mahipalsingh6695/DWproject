# from flask import Flask, request, jsonify
# from chatbot_model import load_model_and_tokenizer, generate_response
# from query_manager import search_database

# app = Flask(__name__)
# model, tokenizer = load_model_and_tokenizer()

# @app.route("/chat", methods=["POST"])
# def chat():
#     try:
#         # Check if the query is provided
#         user_query = request.json.get("query")
#         if not user_query:
#             return jsonify({"error": "Query is missing"}), 400
        
#         # Debug: Log user query
#         print(f"User Query: {user_query}")
        
#         # Search the database with the user query
#         results = search_database(user_query)
#         if not results:
#             return jsonify({"error": "No results found in database"}), 404
        
#         # Debug: Log database results
#         print(f"Database Results: {results}")
        
#         # Use the top 3 results as context for the model
#         context = " ".join(results[:3])
        
#         # Debug: Log context
#         print(f"Context: {context}")
        
#         # Generate the chatbot response
#         response = generate_response(model, tokenizer, context + " " + user_query)
        
#         # Debug: Log chatbot response
#         print(f"Chatbot Response: {response}")
        
#         # Return the response as JSON
#         return jsonify({"response": response})
    
#     except Exception as e:
#         # Catch any errors that occur and log them
#         print(f"Error: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     # Run the Flask application in debug mode
#     app.run(debug=True)




from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_model import load_model_and_tokenizer, generate_response

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Load model and tokenizer once during startup
model, tokenizer = load_model_and_tokenizer()

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_query = request.json.get("query")
        if not user_query:
            return jsonify({"error": "Query is missing"}), 400

        response = generate_response(model, tokenizer, user_query)
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
