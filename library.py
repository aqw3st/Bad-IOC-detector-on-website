import flask
from flask import Flask, render_template, request, redirect
from model import malware_ner
from flaskext.markdown import Markdown

import urllib.request
from bs4 import BeautifulSoup
import PyPDF2
from io import open 
import re
import requests

####################NLP###########################
import spacy
from spacy import displacy
from spacy.tokenizer import Tokenizer