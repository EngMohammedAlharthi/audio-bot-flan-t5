# 🎙️ Audio Bot (Whisper + Flan‑T5)

This is a fully local voice-to-AI bot that:

1. Converts speech from an audio file (`input.wav`) into text using OpenAI's Whisper,  
2. Sends that transcribed text to a Q&A model (Google's Flan‑T5‑Base),  
3. Converts the model's reply back into spoken audio using gTTS,  
4. Saves the response as `reply.mp3`.

No OpenAI key required. No internet inference. 100% local.

---

## 📂 Project Structure

```
/audio_bot
├── main.py              # Core script
├── requirements.txt     # Dependencies
├── input.wav            # Your input audio (you add this)
├── reply.mp3            # Auto-generated reply audio
└── .gitignore           # To skip temporary/cache/audio files
```

---

## 🛠️ Installation & Usage

### 1. Clone or download this repo

Or just copy the files into your project folder.

---

### 2. Install required packages

Make sure Python 3.8+ is installed. Then in terminal:

```bash
pip install -r requirements.txt
```

If `ffmpeg` is missing, run (via conda):

```bash
conda install -c conda-forge ffmpeg
```

---

### 3. Add your voice message

Add an English `.wav` audio file to your folder and name it:

```
input.wav
```

You can create this using your phone or Audacity, etc.

---

### 4. Run the bot

In terminal (inside the project folder):

```bash
python main.py
```

Output:
- Text version of your message (transcript)
- Bot’s reply in text and audio (`reply.mp3`)

---

## ✅ Example

Let’s say you record this:

> Hello, I’m a new electrical engineer. I built a hybrid solar and hydrogen energy system. What do you think? Any ideas to improve it?

The app will respond with:

> That’s a great initiative. You could explore adding battery storage or IoT-based monitoring to enhance efficiency and track usage in real-time.

---

## 🧠 Models Used

| Component     | Model Name              | Source                     |
|---------------|--------------------------|-----------------------------|
| Speech → Text | `openai/whisper`         | [Whisper GitHub](https://github.com/openai/whisper) |
| Text → Reply  | `google/flan-t5-base`    | [HuggingFace](https://huggingface.co/google/flan-t5-base) |
| Text → Audio  | `gTTS`                   | [gTTS PyPI](https://pypi.org/project/gTTS/) |

---

## 🧪 requirements.txt contents

```
openai-whisper
transformers
gTTS
```

---

## 🚧 Issues You May Face

### 🔻 Whisper can't load `input.wav`
Install ffmpeg:
```bash
conda install -c conda-forge ffmpeg
```

---

### 🔻 Output is gibberish (e.g. "hello im quistons")
Solution: use a better model.  
✔ This project uses: `google/flan-t5-base`  
(If you used `flan-t5-small`, expect weird results.)

---

### 🔻 No `reply.mp3` generated
Check that:
- `input.wav` exists in the folder
- You’re connected to the internet for gTTS (text-to-speech)
- The input is in **English**

---

## 🧾 .gitignore (recommended)

```
*.wav
*.mp3
__pycache__/
```

---

## 📌 Description

A local Python chatbot that listens to voice input, understands it, generates a smart reply using Flan‑T5, and talks back—all offline except for gTTS speech synthesis.

Perfect for basic voice AI prototypes or embedded AI devices.

---

## ✍️ Author

Made by [Mohammed Alharthi]  
Inspired by OpenAI, HuggingFace, and gTTS projects.
