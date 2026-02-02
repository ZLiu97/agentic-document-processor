import whisper

def transcribe_audio(filepath: str) -> str:
    try:
        model = whisper.load_model("base")
        result = model.transcribe(filepath)
        return result["text"]
    except Exception as e:
        return f"[AUDIO_ERROR] {e}"
