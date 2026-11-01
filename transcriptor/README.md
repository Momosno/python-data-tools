# transcriptor

> **Work in progress.**

Transcribes recorded interviews (Spanish) using the OpenAI transcription API. The goal is a simple tool for non-technical users that will later be integrated into a backend service.

## Current state

- `whisper.py` — working script: sends an audio file to the OpenAI API with a language hint and a context prompt, and prints the transcription. It documents two options: a more accurate (and more expensive) model and a cheaper one that is usually enough.
- `controller.py` — planned interface for the service layer: file size check, compression and transcription. Functions are stubbed.
- `Anotaciones.md` — technical notes (Whisper works internally with 16 kHz mono audio; `ffmpeg` is a system dependency that must exist on the server, not just a pip package).

## Setup

```bash
cd transcriptor
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
echo "OPENAI_API_KEY=your-key" > .env
```

Place an `audio.wav` file in the folder and run:

```bash
python whisper.py
```

Audio files are git-ignored on purpose: interviews can contain personal information.

## Roadmap

- [ ] Audio upload instead of a fixed file name
- [ ] Size check and compression before sending (API size limit)
- [ ] Audio trimming
- [ ] FastAPI endpoint
