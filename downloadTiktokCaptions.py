
print(">>> Importing required libraries...", "\n")
import yt_dlp, pyperclip, whisper, os, subprocess, re, unicodedata, tldextract, sys
from countdown import countdown
print(">>> Imported required libraries.", 2*"\n")

# change curren working directory

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\downloadTiktokCaptions")

def handle_error(error = ""):
	print(">>>", error)
	input()
	sys.exit()

def is_tiktok_url(url):
	extracted = tldextract.extract(url)
	# Check domain and suffix
	return extracted.domain == 'tiktok' and extracted.suffix == 'com'


def sanitize_filename(title, max_length=100, replacement='_'):
	"""
	Comprehensive filename sanitizer for Windows.
	Handles emojis, unicode, reserved names, and path length.
	"""
	if not title:
		return "untitled_video"

	title = unicodedata.normalize('NFKD', title)
	title = title.encode('ascii', 'ignore').decode('ascii')
	title = re.sub(r'[<>:"/\\|?*]', replacement, title)
	title = "".join(char for char in title if ord(char) > 31)
	
	# Handle Windows reserved names
	reserved = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 
				'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 
				'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'}
	base_name = title.upper().split('.')[0]  # Check before extension
	if base_name in reserved:
		title = f"_{title}"
	
	# No trailing spaces or dots (Windows forbids)
	title = title.rstrip(' .')
	
	# Limit length (leave room for .srt extension)
	max_name_length = max_length - 4  # Account for ".srt"
	if len(title) > max_name_length:
		title = title[:max_name_length]
	
	# Ensure not empty
	if not title or title.isspace():
		title = "untitled_video"
	
	return title


def get_subtitles(url, lang='en', whisper_model='base'):
	"""
	Attempt to download subtitles from video using yt-dlp.
	If none exist, download audio and transcribe with Whisper.
	"""
	# Step 1: Check if video has subtitles without downloading
	ydl_opts = {
		'quiet': True,
		'skip_download': True,
		'writesubtitles': False,  # just check
	}
	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			info = ydl.extract_info(url, download=False)
			has_subs = info.get('subtitles') and any(info['subtitles'].values())
	except Exception as e:
		handle_error(e)
	
	if has_subs:
		print(">>> Subtitles found. Downloading...")
		# Download subtitles only
		sub_opts = {
			'skip_download': True,
			'writesubtitles': True,
			'subtitleslangs': [lang],
			'subtitlesformat': 'vtt/srt',
			'outtmpl': '%(title)s.%(ext)s',
		}

		try:
			with yt_dlp.YoutubeDL(sub_opts) as ydl:
				ydl.download([url])
		except Exception as e:
			handle_error(e)

		print(">>> Subtitles saved.")
		return True
	else:
		print(">>> No subtitles found. Falling back to Whisper transcription...")
		return transcribe_with_whisper(url, lang, whisper_model)

def transcribe_with_whisper(url, lang='en', model_size='base'):
	"""
	Download audio from video and transcribe using Whisper.
	Saves subtitles as SRT file.
	"""
	# Download audio only
	audio_path = 'temp_audio.mp3'
	ydl_opts = {
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'outtmpl': 'temp_audio',  # will become temp_audio.mp3
		'quiet': True,
	}
	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			if os.path.exists(audio_path):
				os.remove(audio_path)
			info = ydl.extract_info(url, download=True)
			title = info.get('title', 'subtitles')
	except Exception as e:
		handle_error(e)

	# Check downloaded file
	
	if not os.path.exists(audio_path):
		print(">>> Audio download failed.")
		return False
	
	# Load Whisper model and transcribe
	print(f">>> Loading Whisper model '{model_size}'...")

	try:
		model = whisper.load_model(model_size)
	except Exception as e:
		handle_error(e)

	print(">>> Transcribing audio...")

	try:
		result = model.transcribe(audio_path, language=lang, task='transcribe')
	except Exception as e:
		handle_error(e)

	# Save as SRT
	srt_filename = f"{sanitize_filename(title)}.srt"
	try:
		with open(srt_filename, 'w', encoding='utf-8') as f:
			for segment in result['segments']:
				start = format_timestamp(segment['start'])
				end = format_timestamp(segment['end'])
				f.write(f"{segment['id']+1}\n{start} --> {end}\n{segment['text'].strip()}\n\n")
	except Exception as e:
		handle_error(e)

	print(f">>> Whisper subtitles saved to '{srt_filename}'")
	
	# Clean up temporary audio
	os.remove(audio_path)
	return True

def format_timestamp(seconds):
	"""Convert seconds to SRT timestamp format (HH:MM:SS,mmm)."""
	h = int(seconds // 3600)
	m = int((seconds % 3600) // 60)
	s = int(seconds % 60)
	ms = int((seconds - int(seconds)) * 1000)
	return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

# Example usage
if __name__ == '__main__':
	url = pyperclip.paste()
	while not is_tiktok_url(url):
		print(">>> There must be a valid tiktok url in your clipboard!")
		url = pyperclip.paste()
		countdown(0,5)
	else:
		print(f">>> url is '{url}'")
		get_subtitles(url, lang='en', whisper_model='base')
		
