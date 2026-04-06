import whisper, pyperclip
from pathlib import Path

model = whisper.load_model("base")
filepath = str(list(Path("./get-transcript").glob("*.ogg"))[0])

# from faster_whisper import WhisperModel
# model = WhisperModel(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\models", device="cpu", compute_type="int8")

# Transcribe an audio file
# segments, info = model.transcribe(filepath, beam_size=5)

# print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})")
# print(f"Duration: {info.duration:.2f} seconds\n")
# result = ""
# for segment in segments:
#   print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
#   result += segement.text
#   pyperclip.copy(result)

pyperclip.copy(model.transcribe(filepath, language = "en", task='transcribe', verbose=True)["text"])

def close_window(count=8):
	from countdown import countdown
	countdown(mins=0, secs=count)

close_window()