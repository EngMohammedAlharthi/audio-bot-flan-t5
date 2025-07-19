# main.py
import whisper
from transformers import pipeline
from gtts import gTTS

def transcribe(audio_path):
    model = whisper.load_model("small")
    return model.transcribe(audio_path)["text"]

# setup Flan-T5-base for on-device Q&A
qa = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1,
    do_sample=False
)

def generate_response(text):
    prompt = f"Question: {text}\nAnswer:"
    out = qa(prompt, max_length=200)
    return out[0]["generated_text"].strip()

def synthesize(text, output_path):
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)

def main():
    transcript = transcribe("input.wav")
    print("Transcript:\n", transcript, "\n")

    reply = generate_response(transcript)
    print("Reply:\n", reply, "\n")

    synthesize(reply, "reply.mp3")
    print("Generated reply.mp3")

if __name__ == "__main__":
    main()
