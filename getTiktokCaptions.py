print(">>> Importing required libraries...")
import yt_dlp, pyperclip, whisper, os, subprocess, re, unicodedata, tldextract, sys
from countdown import countdown
print(">>> Imported required libraries.")

# change current working directory
os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\getTiktokCaptions")

def handle_error(error = ""):
    print(">>>", error)
    input()
    sys.exit()

def is_tiktok_url(url):
    extracted = tldextract.extract(url)
    return extracted.domain == 'tiktok' and extracted.suffix == 'com'

def copy_to_clipboard(text):
    """Copy text to clipboard using pyperclip."""
    try:
        pyperclip.copy(text)
        print(">>> Subtitles copied to clipboard!")
        return True
    except Exception as e:
        print(f">>> Failed to copy to clipboard: {e}")
        return False

def get_subtitles(url, lang='en', whisper_model='base'):
    """
    Attempt to get subtitles from video using yt-dlp without downloading.
    If none exist, download audio and transcribe with Whisper.
    Copies result to clipboard instead of saving to file.
    """
    # Step 1: Check if video has subtitles without downloading
    ydl_opts = {
        'quiet': False,
        'skip_download': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            subtitles = info.get('subtitles', {})
            has_subs = subtitles and any(subtitles.values())
            title = info.get('title', 'video')
    except Exception as e:
        handle_error(e)
    
    if has_subs:
        print(">>> Subtitles found. Extracting...")
        
        # Get the subtitle URL for the requested language
        sub_list = subtitles.get(lang, []) or subtitles.get('en', []) or list(subtitles.values())[0]
        if not sub_list:
            print(">>> Requested language not available, falling back to Whisper...")
            return transcribe_with_whisper(url, lang, whisper_model)
        
        sub_url = sub_list[0].get('url') if isinstance(sub_list, list) else sub_list.get('url')
        
        if not sub_url:
            print(">>> Could not get subtitle URL, falling back to Whisper...")
            return transcribe_with_whisper(url, lang, whisper_model)
        
        # Download subtitle content directly to memory
        try:
            import urllib.request
            with urllib.request.urlopen(sub_url) as response:
                sub_content = response.read().decode('utf-8')
            
            # Convert VTT to plain text (remove timestamps and formatting)
            clean_text = vtt_to_text(sub_content)
            copy_to_clipboard(clean_text)
            print(f">>> Extracted subtitles for: {title}")
            return True
            
        except Exception as e:
            print(f">>> Failed to download subtitles: {e}")
            print(">>> Falling back to Whisper...")
            return transcribe_with_whisper(url, lang, whisper_model)
    else:
        print(">>> No subtitles found. Falling back to Whisper transcription...")
        return transcribe_with_whisper(url, lang, whisper_model)

def vtt_to_text(vtt_content):
    """Convert VTT subtitle content to plain text."""
    lines = vtt_content.split('\n')
    text_lines = []
    
    for line in lines:
        line = line.strip()
        # Skip empty lines, timestamps, WEBVTT header, and cue settings
        if (not line or 
            '-->' in line or 
            line.startswith('WEBVTT') or 
            line.startswith('NOTE') or
            line[0:1].isdigit() and '-->' in line):
            continue
        # Remove HTML-like tags
        line = re.sub(r'<[^>]+>', '', line)
        if line:
            text_lines.append(line)
    
    return ' '.join(text_lines)

def transcribe_with_whisper(url, lang='en', model_size='base'):
    """
    Download audio from video, transcribe using Whisper, copy to clipboard.
    Cleans up audio file after transcription.
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
        'outtmpl': 'temp_audio',
        'quiet': False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if os.path.exists(audio_path):
                os.remove(audio_path)
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'subtitles')
    except Exception as e:
        handle_error(e)

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
        result = model.transcribe(audio_path, language=lang, task='transcribe', verbose=True)
    except Exception as e:
        handle_error(e)

    # Build transcript text (without timestamps for cleaner clipboard content)
    transcript_lines = []
    for segment in result['segments']:
        transcript_lines.append(segment['text'].strip())
    
    full_transcript = ' '.join(transcript_lines)
    
    # Copy to clipboard instead of saving file
    copy_to_clipboard(full_transcript)
    print(f">>> Transcribed: {title}")
    
    # Clean up temporary audio
    os.remove(audio_path)
    return True

# Remove unused sanitize_filename and format_timestamp functions
# (or keep them if you want to add optional file-saving later)

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