import time
start_time = time.process_time()
from urllib.request import urlopen
import bs4
import re
import requests
from bs4 import BeautifulSoup
import spacy
path = r'C:\Users\IAVasilev\Desktop\sm_1000ex_1000it'
nlp = spacy.load(path)

url = 'https://blogs.juniper.net/en-us/security/freshly-disclosed-vulnerability-cve-2021-20090-exploited-in-the-wild'

text = requests.get(url).text
soup = BeautifulSoup(text,'lxml')
# searched_words = ["Mirai","CVE-2021-20090", "CVE-2021-1498","27.22.80[.]19"]
mark = '<mark>{}</mark>'

arr = []
doc = nlp(soup.text)
for entity in doc.ents:
    arr.append(entity.text)

text_data = str(soup.prettify())
for entity in arr:
	for word in text_data.split():
		if word == entity:
			text_data = text_data.replace(word, mark.format(word,word))

'''-----------------------------------------------------'''
# text_data = str(soup.prettify())
# for searched_word in searched_words:
# 	for word in text_data.split():
# 		if word == searched_word:
# 			# text_data = text_data.replace(word, upgrade.format(word,word))
# 			text_data = text_data.replace(word, mark.format(word,word))


print(text_data)


# soup = bs4.BeautifulSoup(data, 'html.parser')
# # print(soup.prettify())
# 
# results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
# for content in results:
#     words = content.split()
#     for index, word in enumerate(words):
#         # If the content contains the search word twice or more this will fire for each occurence
#         if word == searched_word:
# 			word = upgrade
#             
# 


# print(time.process_time() - start_time, "seconds")

# upgrade = '''<span id="1a41062104" class="_1Ivbd_21aL6" name="{}" 
# style="pointer-events: all; cursor: pointer; position: relative; z-index: 1; 
# line-height: inherit; font-style: inherit; font-size: inherit; color: inherit; 
# font-family: inherit; text-indent: initial; display: inline-block; word-break: 
# break-word; vertical-align: middle; min-width: auto; border-radius: 4px; border: 
# 2px solid rgb(245, 166, 35);">{}</span>'''
# # print(upgrade.format("CVE","CVE"))
# string = '''Most organizations do not have policies to patch within a few days, 
# taking sometimes weeks to react. But in the case of IOT devices or home gateways, 
# the situation is much worse as most users are not tech saavy and even those who are 
# do not get informed about potential vulnerabilities and patches to apply.'''
# for word in string.split():
# 	if word == 'weeks':
# 		string = string.replace(word, upgrade.format(word,word))
# 	# word.replace(1)
# print(string)