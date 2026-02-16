print("Importing required libraries...", "\n")
import ezgmail, webbrowser, re, time
from bs4 import BeautifulSoup
# intializing - where an error is likey to occur
try:
	ezgmail.init()

except Exception as e:
	print(e)
	input()
	exit()
print("Imported required libraries.", 2*"\n")


def extract_unsubscribe_link(text_body):
	"""
	Extract unsubscribe link from email body (plain text or HTML).
	Returns the URL string if found, None otherwise.
	"""
	if not text_body:
		return None
	
	# Check if content contains HTML tags
	is_html = bool(re.search(r'<html|<body|<a\s+href|<\/a>', text_body, re.IGNORECASE))
	
	if is_html:
		soup = BeautifulSoup(text_body, 'html.parser')
		
		# Strategy 1: Find links containing "unsubscribe" or similar text
		for link in soup.find_all('a'):
			link_text = link.get_text(strip=True).lower()
			if any(term in link_text for term in ['unsubscribe', 'opt-out', 'email preferences', 'manage notifications']):
				href = link.get('href')
				if href and href.startswith('http'):
					return href
		
		# Strategy 2: Find links where href contains "unsubscribe"
		for link in soup.find_all('a', href=re.compile(r'unsubscribe|opt-out', re.I)):
			href = link.get('href')
			if href and href.startswith('http'):
				return href
	
	# Plain text strategies
	# Pattern 1: "Unsubscribe:" or "Unsubscribe" followed by optional punctuation/colon and URL
	# Matches: "Unsubscribe: https://..." or "Unsubscribe (https://...)" or "Unsubscribe https://..."
	pattern1 = r'(?i)unsubscribe\s*:?\s*\(?(https?://[^\s\)]+)'
	match = re.search(pattern1, text_body)
	if match:
		return match.group(1).rstrip(').,;')
	
	# Pattern 2: URLs containing "unsubscribe" in the path
	pattern2 = r'(?i)(https?://[^\s]*unsubscribe[^\s\)]*)'
	match = re.search(pattern2, text_body)
	if match:
		return match.group(1).rstrip(').,;')
	
	# Pattern 3: Footer style "To unsubscribe, click here: <url>"
	pattern3 = r'(?i)to\s+unsubscribe[,\s]+(?:click\s+(?:here|to))?[:+]?\s*(https?://[^\s]+)'
	match = re.search(pattern3, text_body)
	if match:
		return match.group(1).rstrip(').,;')
	
	return None



try:
	search_queries = ['unsubscribe', 'newsletter', 'promotion', 'marketing']
	all_threads = []
	for query in search_queries:
		threads = ezgmail.search(query)
		all_threads.extend(threads)
	
	all_threads = set(all_threads)

	seen_senders = set()
	unique_threads = [ thread for thread in all_threads if thread.messages and not (thread.messages[0].sender in seen_senders or seen_senders.add(thread.messages[0].sender))]
	print(f"Found {len(unique_threads)} unique email senders to process", "\n")
	input("Press enter to contitue!")
except Exception as e:
	print(e)
	input()
	exit()


try:
	for thread in unique_threads:
		message = thread.messages[0]
		print(f"Processing email from: {message.sender}")
		link = extract_unsubscribe_link(message.body)
		if link:
			webbrowser.open(link)
			time.sleep(1)
		else:
			print(f"Couldn't get link for {message.sender}")
except Exception as e:
	print(e)
	input()
	exit()

