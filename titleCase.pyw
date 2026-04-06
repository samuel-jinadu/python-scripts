import pyperclip, winsound
from time import sleep

def smart_title_case(text):
		text = text.title()
		"""Convert to title case while preserving certain words."""
		# Words to keep lowercase (except at start of string)
		lowercase_words = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 
						  'in', 'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet'}
		
		# Words to keep uppercase
		uppercase_words = {'api', 'url', 'http', 'https', 'www', 'id', 'pdf', 
						  'csv', 'json', 'xml', 'html', 'sql', 'ui', 'ux'}
		
		words = text.split()
		result_words = []
		
		for i, word in enumerate(words):
			# Check if entire word is uppercase (acronym)
			if word.isupper():
				result_words.append(word)
			# Check if word should remain uppercase
			elif word.lower() in uppercase_words:
				result_words.append(word.upper())
			# Check if word should remain lowercase (not first word)
			elif word.lower() in lowercase_words and i > 0:
				result_words.append(word.lower())
			# Otherwise, apply title case
			else:
				# Handle hyphenated words
				if '-' in word:
					parts = word.split('-')
					formatted_parts = []
					for j, part in enumerate(parts):
						if part.lower() in lowercase_words and j > 0:
							formatted_parts.append(part.lower())
						elif part.lower() in uppercase_words:
							formatted_parts.append(part.upper())
						else:
							formatted_parts.append(part.capitalize())
					result_words.append('-'.join(formatted_parts))
				else:
					result_words.append(word.capitalize())
		
		return ' '.join(result_words)

try:
	text = pyperclip.paste()
	text = smart_title_case(text)
	pyperclip.copy(text)
	winsound.MessageBeep()
	sleep(5)
except:
	winsound.MessageBeep(winsound.MB_ICONHAND)
	