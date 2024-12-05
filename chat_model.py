from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can use "gpt3" with OpenAI's API if desired.
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_response(prompt, max_length=50):
    """
    Generate a response using GPT-2.
    Args:
        prompt (str): The input prompt or user query.
        max_length (int): The maximum length of the generated text.
    Returns:
        str: The generated response.
    """
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response