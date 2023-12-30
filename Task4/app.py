import os
import gradio as gr
from transformers import BartForConditionalGeneration, AutoTokenizer

model_name = os.path.join(
    os.getcwd(),
    "model/models--facebook--bart-large-cnn/snapshots/08436bb998cc59c90294f46c0ec716bf86556c71",
)
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def summarizer(text):
    inputs = tokenizer([text.replace("\n", "")], return_tensors="pt")
    # Generate Summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=0)
    summary_text = tokenizer.batch_decode(
        summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )[0]
    return summary_text


iface = gr.Interface(
    fn=summarizer,
    inputs="text",
    outputs="text",
    title="Text Summarizer with BART",
    flagging_dir="/tmp/flagged",
)

iface.launch(server_port=8080)
