import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carica il tokenizer e il modello GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Sposta il modello su GPU
device = torch.device("cuda")
model.to(device)

# Testo di input
input_text = "Once upon a time"

# Tokenizza il testo di input (aggiungi il token di fine sequenza)
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Sposta input_ids su GPU
input_ids = input_ids.to(device)

# Crea l'attention mask
attention_mask = torch.ones(input_ids.shape, device=device)

# Genera il testo
output = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_length=100,
    num_return_sequences=1,
    pad_token_id=tokenizer.eos_token_id,
)

# Decodifica e stampa il testo generato
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(output_text)
