import os
import assemblyai as aai
import gradio as gr
import dotenv

dotenv.load_dotenv()

aai.settings.api_key = os.getenv("AAI_API_KEY")
transcriber = aai.Transcriber()

# transcript = transcriber.transcribe(
#     "https://storage.googleapis.com/aai-web-samples/news.mp4"
# )
# # transcript = transcriber.transcribe("./my-local-audio-file.wav")

# print(transcript.text)


def transcribe_audio(audio_file):
    assert os.path.exists(audio_file)
    transcript = transcriber.transcribe(audio_file).text.replace(".", "")
    output_transcript = []
    for word in transcript.split():
        if word.endswith(("a", "e", "i", "o", "u")):
            output_transcript.append(f"{word}-v")  # Add "-v" suffix
        else:
            output_transcript.append(f"{word}-c")  # Add "-c" suffix
    return " ".join(output_transcript)


iface = gr.Interface(
    fn=transcribe_audio,
    inputs=["file"],
    outputs="text",
    title="Speech-to-Text Transcription",
)
iface.launch(share=True)
