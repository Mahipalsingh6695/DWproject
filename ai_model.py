# ai_model.py
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Load Hugging Face Model (DialoGPT-medium)
def initialize_ai_model():
    model_name = "microsoft/DialoGPT-medium"  # You can replace with any Hugging Face model
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return pipeline('conversational', model=model, tokenizer=tokenizer)

# Generate AI response based on user input
def generate_ai_response(ai_pipeline, user_input):
    return ai_pipeline(user_input)[0]['generated_text']

# Combine AI model responses with database knowledge
def chatbot_response(user_input, ai_pipeline):
    # Fetch knowledge from SQLite database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    conn.close()

    # Database content to add context to AI response
    database_context = " ".join([row[1] for row in rows])

    # Formulate prompt with user input and database content
    prompt = f"User: {user_input}\nKnowledge Base: {database_context}\nAI:"
    ai_response = generate_ai_response(ai_pipeline, prompt)

    return ai_response

