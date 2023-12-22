import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer

st.title("Text Summarizer with BART")

# Load BART model and tokenizer
model_name = "facebook/bart-large-cnn"  # Suitable BART variant for summarization
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Input text box
input_text = st.text_area("Enter your text here:", height=300)

# Submit button
if st.button("Summarize"):
    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate summary
    summary_ids = model.generate(input_ids)
    summary_text = tokenizer.decode(summary_ids[0])

    # Output text box
    st.write("Summary:")
    st.text_area("Summary text:", value=summary_text, height=200)
