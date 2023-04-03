
from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


def get_token_count(text: str):
    tokens = tokenizer(text)['input_ids']
    
    return len(tokens)
