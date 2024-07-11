import torch
from common import main
from justone.llmbot import LLMbot

torch.device("cuda" if torch.cuda.is_available() else "cpu")

logger = main()

mybot = LLMbot(logger)
mybot.eval()

question = "What is the capital of France?"
context = "France is a country in Europe. The capital of France is Paris."

inputs = mybot.tokenizer(question, context, return_tensors="pt")

# sposto su gpu se disponibile
inputs.to(mybot.device)

with torch.no_grad():
    outputs = mybot.model(**inputs)

start_logits = outputs.start_logits
end_logits = outputs.end_logits

start_index = torch.argmax(start_logits)
end_index = torch.argmax(end_logits)

tokens = inputs.input_ids[0][start_index : end_index + 1]
answer = mybot.tokenizer.decode(tokens)

print(f"Answer: {answer}")

del mybot
