import streamlit as st
from transformers import BartForConditionalGeneration, AutoTokenizer

st.title("Text Summarizer with BART")

# Load BART model and tokenizer
model_name = "facebook/bart-large-cnn"  # Suitable BART variant for summarization
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Input text box
TEXT_TO_SUMMARIZE = st.text_area("Enter your text here:", height=300)

# Submit button
if st.button("Summarize"):
    inputs = tokenizer([TEXT_TO_SUMMARIZE.replace("\n", "")], return_tensors="pt")
    # Generate Summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=0)
    summary_text = tokenizer.batch_decode(
        summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )[0]
    # Output text box
    st.write("Summary:")
    st.text_area("Summary text:", value=summary_text, height=200)
