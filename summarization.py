from transformers import BartTokenizer, BartForConditionalGeneration, pipeline

# load pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# define text input
articles = """ This code will run on CPU by default. However, please note that BERT models are computationally intensive, and running this code on CPU might be slower compared to using a GPU. Additionally, due to the size and complexity of the BERT model, processing longer documents may also take longer. """

# Tokenize the input text
input_tokenize = tokenizer.encode(
    "summarize: " + articles, return_tensors='pt', max_length=1024, truncation=True)

# Summarize the input text using BART
summary_ids = model.generate(input_tokenize, max_length=150,
                             min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Original Article: ")
print(article)

print("\n Summarized Article: ")
print(summary)
