print("Importing required libraries...", "\n")
import random, subprocess, platform

print("Imported required libraries.", 2*"\n")


def speak(text=""):
   """Uses native OS speech commands - fast, no hangs, no threads"""
   if not text:
   	return
   
   print(text, flush=True)
   
   system = platform.system()
   
   try:
   	if system == "Darwin":  # macOS - 'say' is built-in
   		# Fix: No need to escape quotes when passing list args to subprocess
   		subprocess.run(["say", text], timeout=30, check=False)
   		
   	elif system == "Windows":  # Windows - PowerShell SAPI
   		# Fix: PowerShell uses "" (doubled quotes) to escape quotes inside strings, not \"
   		safe_text = text.replace('"', '""')
   		cmd = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{safe_text}");'
   		subprocess.run(["powershell", "-c", cmd], timeout=30, check=False)
   		
   	else:  # Linux - requires 'espeak' or 'spd-say' installed
   		# Fix: No need to escape quotes when passing list args to subprocess
   		subprocess.run(["spd-say", text], timeout=30, check=False)
   		
   except FileNotFoundError:
   	pass
   except subprocess.TimeoutExpired:
   	pass
   except Exception:
   	pass


# === GAME LOGIC ===
secret = random.randint(1, 10)
no_of_guesses = 3

speak('Heyy! I am thinking of a number between 1 and 10')
speak('You get only ' + str(no_of_guesses) + ' chances')
speak('Choose wisely ;)')
print()

guess = None

for guessTaken in range(no_of_guesses, 0, -1):
   print()
   if guessTaken == 1:
   	speak("Last chance fellow daoist...")
   else:
   	speak('You have only ' + str(guessTaken) + ' chances left')
   
   try:
   	guess = input().strip()
   except EOFError:
   	break
   	
   if guess.isdigit():
   	guess = int(guess)  # Fix: Removed unnecessary float() conversion
   else:
   	speak("Thats not even a number! Good job wasting a chance!")
   	continue
   	
   if guess < secret:
   	speak('Its higher than that')
   elif guess > secret:
   	speak('Its lower than that')
   else:
   	break

print()
if guess is not None and guess == secret:
   speak('Took you long enough!')
   # Fix: Handle EOFError when input is piped/closed
   try:
   	input('Press enter to leave')
   except EOFError:
   	pass
else:
   speak('Hoho! fellow daoist :)')
   speak('Now I get to keep your soul!')
   # Fix: Handle EOFError when input is piped/closed
   try:
   	input('Press enter to forfeit the game and your soul')
   except EOFError:
   	pass