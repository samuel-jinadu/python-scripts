from faster_whisper import download_model
import os

# Define the path (use raw string r-prefix to handle backslashes and spaces)
output_path = r"C:\Users\Samuel\Desktop\Remote Job\practice\python\models"

# Create directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Download base model to that location
model_path = download_model("base", output_dir=output_path)

print(f"Model downloaded to: {model_path}")

def close_window(count=8):
	from countdown import countdown
	countdown(mins=0, secs=count)

close_window()