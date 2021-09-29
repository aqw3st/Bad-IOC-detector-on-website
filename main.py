#FLASK
import library
from library import *
import flask
from flask import Flask, render_template, request, redirect
from model import malware_ner
from flaskext.markdown import Markdown

# PARSING
import urllib.request
from bs4 import BeautifulSoup
import PyPDF2
import re
import requests
from spacypdfreader import pdf_reader
import pdftotree

#NLP
import spacy
# from spacy import displacy
# from spacy.tokenizer import Tokenizer
nlp = spacy.load('model/Spacy Model v.777 02.09') #nlp model for detecting malware v.1

#ANOTHER
import os
import sys
# upgrade = '''<span id="7d1074629" class="_1Ivbd_21aL6" name="{}" style="pointer-events: all; cursor: pointer; z-index: 1; line-height: inherit; font-style: inherit; font-size: inherit; color: inherit; font-family: inherit; text-indent: initial; display: inline-block; word-break: break-word; vertical-align: middle; min-width: auto; position: relative; right: 6px; height: inherit; border-radius: 4px; border: 2px solid rgb(245, 166, 35); background-color: transparent;">{}</span>'''

#OTHERS
from io import open 

# header for correct parsing html
headers = {'User-Agent': 
		   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)' 
           'AppleWebKit/537.36 (KHTML, like Gecko)' # 
		   'Chrome/ 93.0.4577.63 Safari/537.36'  # 93.0.4577.63 - chrome version
		   }


app = Flask(__name__)
Markdown(app)


#MAIN PAGE
@app.route('/', methods=['POST','GET'])

def hello():
	return render_template('index.html')


#RENDER WEB PAGE AND DETECT ENTYTIES IN BROWSER LOCALLY
@app.route('/page', methods=['POST','GET'])

def render_url():
	# mark = '<mark>{}</mark>'
	if request.method == 'POST':
		url = request.form['get_url_please'] #get url
		raw_html = requests.get(url, headers = headers,verify=False).text # get raw html code
		soup = BeautifulSoup(raw_html,features='html.parser') # get content from raw html
		text_data = str(soup) 
		doc = nlp(soup.text)	

		#FIND IOCs
		domain_find = find_DOMAIN(text_data)
		cve_find = find_CVE(text_data)
		apt_find = find_APT(text_data)
		hash_find = find_HASH(text_data)
		url_find = find_URL(text_data)
		ips = find_IP(text_data)
		malwares = find_MALWARE(doc)


		#Highlights found iocs on html page
		data = highlight_html(cve_find, hash_find, malwares, domain_find, ips, apt_find, text_data)
		html_text = BeautifulSoup(data,features='html.parser')
		
	return render_template('webpage.html',html_text = html_text)




@app.route('/try_render')
def render_try():
	return render_template('try_render.html')












