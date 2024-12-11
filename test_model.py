from transformers import AutoModelForCausalLM, AutoTokenizer

def load_model_and_tokenizer():
    """
    Load the Hugging Face model and tokenizer.
    Replace 'gpt2' with your specific model name.
    """
    model_name = "gpt2"  # Replace this with your model name
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

def test_model():
    """
    Test the model with a sample input to ensure it's working correctly.
    """
    model, tokenizer = load_model_and_tokenizer()

    # Sample input
    input_text = "Why we use OpenAI ?"
    print(f"Input: {input_text}")

    # Tokenize the input
    inputs = tokenizer(input_text, return_tensors="pt")
    print(f"Tokenized Inputs: {inputs}")

    # Generate a response
    output_ids = model.generate(**inputs, max_length=50)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    print(f"Model Response: {response}")

if __name__ == "__main__":
    test_model()
