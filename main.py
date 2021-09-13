import library
# import flask
# from flask import Flask, render_template, request, redirect
# from model import malware_ner
# from flaskext.markdown import Markdown

# import urllib.request
# from bs4 import BeautifulSoup
# import PyPDF2
# from io import open 
# import re
# import requests

# ####################NLP###########################
# import spacy
# from spacy import displacy
# from spacy.tokenizer import Tokenizer
nlp = spacy.load('model/malware_ner') #nlp model for detecting malware v.1




# header for correct parsing html
headers = {'User-Agent': 
		   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)' 
           'AppleWebKit/537.36 (KHTML, like Gecko)' # 
		   'Chrome/ 93.0.4577.63 Safari/537.36'  # 93.0.4577.63 - chrome version
		   }


app = Flask(__name__)
Markdown(app)

@app.route('/', methods=['POST','GET'])

def hello():
	return render_template('index.html')


@app.route('/result', methods=['POST','GET'])

def extract():
	if request.method == 'POST':
		rawtext = request.form['text_ner']	
		doc = nlp(rawtext)
		html = displacy.render(doc,style='ent')
		result = html
	return render_template('result.html', rawtext=rawtext, result = result)


@app.route('/page', methods=['POST','GET'])
def render_url():

	mark = '<mark>{}</mark>' # how highlights words in html page

	if request.method == 'POST':
		url = request.form['get_url'] #get url
		text_data = requests.get(url, headers = headers).text # get raw html code
		soup = BeautifulSoup(text_data,'html') # get content from raw html
		text_data = str(soup) # 
		doc = nlp(soup.text)
		for entity in list(doc.ents):
			if str(entity) in text_data.split():
				text_data = text_data.replace(str(entity), mark.format(entity))
		html_code = BeautifulSoup(text_data,'html')

	return render_template('webpage.html',html_code = html_code)


@app.route('/try_render')
def render_try():
	return render_template('try_render.html')





@app.route('/pdf', methods=['POST','GET'])
def render_pdf():
	if request.method == 'POST':
		pdf = request.files['file']

		# pdf = pdf.read()
		# pdfFileObj = open(pdf, 'rb',encoding='latin1') 
		# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
		# pageObj = pdfReader.getPage(0) 
		# result = pageObj.extractText()
	return render_template('pdf_open.html',result = result)




