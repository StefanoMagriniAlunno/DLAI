from transformers import GPT2Config, GPT2Model


class GPT2HintModel(GPT2Model):
    def __init__(self, config: GPT2Config):
        super(GPT2HintModel, self).__init__(config)
        # Si possono aggiungere ulteriori layer per il fine-tuning

    def forward(
        self,
        input_ids,
        attention_mask=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        encoder_hidden_states=None,
        encoder_attention_mask=None,
        past_key_values=None,
        use_cache=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
    ):
        outputs = super(GPT2HintModel, self).forward(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            encoder_hidden_states=encoder_hidden_states,
            encoder_attention_mask=encoder_attention_mask,
            past_key_values=past_key_values,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        # Applicare ulteriori layer
        return outputs


class GPT2AnswerModel(GPT2Model):
    def __init__(self, config: GPT2Config):
        super(GPT2AnswerModel, self).__init__(config)
        # Si possono aggiungere ulteriori layer per il fine-tuning

    def forward(
        self,
        input_ids,
        attention_mask=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        encoder_hidden_states=None,
        encoder_attention_mask=None,
        past_key_values=None,
        use_cache=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
    ):
        outputs = super(GPT2AnswerModel, self).forward(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            encoder_hidden_states=encoder_hidden_states,
            encoder_attention_mask=encoder_attention_mask,
            past_key_values=past_key_values,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        # Applicare ulteriori layer
        return outputs


if __name__ == "__main__":

    import os

    import torch
    from transformers import GPT2Tokenizer

    config = GPT2Config.from_pretrained(
        "gpt2", chache_dir=os.path.join(os.getcwd(), r"/data/db/gpt2/config")
    )
    model = GPT2HintModel.from_pretrained(
        os.path.join(os.getcwd(), r"/data/db/gpt2/model"), config=config
    )
    tokenizer = GPT2Tokenizer.from_pretrained(
        os.path.join(os.getcwd(), r"/data/db/gpt2/tokenizer")
    )
    tokenizer.add_special_tokens({"pad_token": tokenizer.eos_token})

    inputs_list = ["cane", "gatto", "cavallo"]
    batch_tokenized = tokenizer(
        inputs_list, return_tensors="pt", padding=True, truncation=True
    )
    input_ids = batch_tokenized["input_ids"]
    attention_mask = batch_tokenized["attention_mask"]
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    input_ids = input_ids.to(device)
    attention_mask = attention_mask.to(device)
    model = model.to(device)
    outputs = model(input_ids, attention_mask=attention_mask)
    last_word_states = outputs.last_hidden_state[:, -1, :]
    print("Last Hidden States for the last word in each sequence:")
    print(last_word_states)
