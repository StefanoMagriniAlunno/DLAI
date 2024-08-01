import torch
from transformers import GPT2ForQuestionAnswering, GPT2Tokenizer

# Load pre-trained model and tokenizer
model = GPT2ForQuestionAnswering.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Encode text
context = "the secret word on their boards. All clues are revealed simultaneously, and any duplicate clues are discarded. However, if a clue matches the secret word, it cannot be discarded and must be considered by the guesser to avoid confusion. The guesser then tries to guess the secret word based on the remaining unique clues. Correct guesses earn points, while incorrect guesses do not. The game continues for a set number of rounds or until all cards are used, and the team with the most points wins."
question = "What is your one hint related to 'house' ?"

# Encode context and question
input = tokenizer.encode_plus(question, context, return_tensors="pt")

# Get answer
outputs = model(**input)

start_index = torch.argmax(outputs.start_logits)
end_index = torch.argmax(outputs.end_logits) + 1

answer = tokenizer.convert_tokens_to_string(
    tokenizer.convert_ids_to_tokens(input["input_ids"][0][start_index:end_index])
)

print(answer)
