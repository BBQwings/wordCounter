import requests 
import re 
from bs4 import BeautifulSoup 

# Target url
PAGE_URL = "https://www.wikipedia.org"

def get_html_of(url): 
	resp = requests.get(url) 
# if status code 200 is not returned, return an error
	if resp.status_code != 200: 
		print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
		exit(1)
# return the content of the website
	return resp.content.decode()

def get_all_words_from(url):
	html = get_html_of(PAGE_URL) 
	soup = BeautifulSoup(html, 'html.parser')
	raw_text = soup.get_text() 
	# r'\w' = interprets it as individual characters, instead of an escaped character
	return re.findall(r'\w+', raw_text)

def count_occurences_in(word_list):
	word_list = {}
	for word in all_words: 
		word_count[word] = word_count.setdefault(word, 0) + 1
	return word_count
# Sort the words in a list
def get_top_words_from(all_words): 
	occurrences = count_occurences_in(all_words)
	return sorted(word_count.items(), key=lambda item: item[1], reverse=True)

all_words = get_all_words_from(PAGE_URL)
top_words = get_top_words

# Print the top 10 words 
for i in range(10): 
	print(top_words[i][0])
