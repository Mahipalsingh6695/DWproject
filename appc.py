# import gradio as gr
# from query_manager import search_database
# from chatbot_model import load_model_and_tokenizer, generate_response

# # Load the Hugging Face model and tokenizer
# model, tokenizer = load_model_and_tokenizer()

# # Define the chatbot function
# def chatbot_response(user_input):
#     # Fetch data from MongoDB
#     website_data = search_database()
    
#     # Construct the context from the website data
#     context = " ".join([item["content"] for item in website_data[:10]])  # Use the first 10 entries
#     prompt = f"{context}\n\nUser: {user_input}\nChatbot:"
    
#     # Generate response
#     response = generate_response(model, tokenizer, prompt)
#     return response

# # Create Gradio interface
# with gr.Blocks() as demo:
#     gr.Markdown("# Chatbot for Website Data")
    
#     with gr.Row():
#         with gr.Column():
#             user_input = gr.Textbox(
#                 label="Your Query",
#                 placeholder="Ask a question about the website..."
#             )
#         with gr.Column():
#             chatbot_output = gr.Textbox(label="Chatbot Response")
    
#     submit_button = gr.Button("Submit")
    
#     submit_button.click(chatbot_response, inputs=[user_input], outputs=[chatbot_output])

# # Launch the Gradio app
# if __name__ == "__main__":
#     demo.launch()
