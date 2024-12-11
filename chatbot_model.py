from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model_and_tokenizer():
    model_name = "gpt2"  # Replace with the desired model (e.g., 'mistral/Mistral-7B' for Mistral 7B)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def generate_response(model, tokenizer, prompt):
    # Ensure the tokenizer has a pad_token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token  # Use eos_token as the pad_token if none exists
    
    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

    # Generate response with sampling enabled
    outputs = model.generate(
        inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_length=100,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,   # Used in sampling-based generation
        top_p=0.9,         # Used in sampling-based generation
        top_k=50,          # Used in sampling-based generation
        do_sample=True,    # Enable sampling
        pad_token_id=tokenizer.pad_token_id  # Ensure pad_token_id is correctly set
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == "__main__":
    model, tokenizer = load_model_and_tokenizer()
    user_query = "What is the purpose of AI?"
    response = generate_response(model, tokenizer, user_query)
    print(f"Chatbot Response: {response}")



