import os
import assemblyai as aai
import gradio as gr
import dotenv

dotenv.load_dotenv()
aai.settings.api_key = os.getenv("AAI_API_KEY")
transcriber = aai.Transcriber()


def transcribe_audio(audio_file):
    # Adapt this line for Lambda's temp file system if needed
    assert os.path.exists(audio_file)
    transcript = transcriber.transcribe(audio_file).text.replace(".", "")
    output_transcript = []
    for word in transcript.split():
        if word.endswith(("a", "e", "i", "o", "u")):
            output_transcript.append(f"{word}-v")
        else:
            output_transcript.append(f"{word}-c")
    return " ".join(output_transcript)


iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(sources=["microphone", "upload"], type="filepath"),
    outputs="text",
    title="Speech-to-Text Transcription",
    flagging_dir="/tmp/flagged",
)

iface.launch(server_port=8080)
