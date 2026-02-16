import whisper
try:
	model = whisper.load_model("base")
except Exception as e:
	print()
	print(e)
	input()

input()