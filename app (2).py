from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import csv
import gensim
from gensim.models import word2vec
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from predict_antonym import *
from predict_synonym import *
from predict_relation import *



app = Flask(__name__,template_folder='.')


w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
stopwords = stopwords.words('english')
stopwords.append('\n')

new_dataset=[]

def get_processed_text(text):
    """
    input: text -> an entire string of text
    output: tokens -> a list containing all filtered words
    """
    tags = re.compile(r'<.*?>')
    tags.sub('', text)                                 # to remove content in HTML tags
    text = re.sub(r'http\S+', ' ', text)               # to remove URLs
    text = re.sub(r'[^\w\s]',' ', text)                 # to remove punctuations
    text = re.sub(r'[^a-zA-Z]', ' ', text).lower()     # to remove anything other than characters
    tokens = [w for w in w_tokenizer.tokenize(text) if w not in stopwords and w[0] != '@'] # tokenizing across whitsepaces to extract words
    return tokens


with open('output.csv', 'r', encoding='utf-8') as f:
    read_data = f.read()
    #print(type(f))
f.close()


def myFunc(e):
	return e[1]





@app.route('/',methods=['GET'])
def main():
        return render_template("wordAffiliation.html")

@app.route('/', methods=['POST'])
def getcsv():

	if request.method == 'POST':

		file = request.files['data_file']
		if not file:
			return "no file"


		read_data = file.stream.read().decode("utf-8")
		#csv_input = csv.reader(file_contents)

		#implementation
		new_dataset=get_processed_text(read_data)

		new_dataset=list(set(new_dataset))



		return render_template("wordAffiliation.html",output = new_dataset)

@app.route('/synonyms', methods=['POST'])
def synonyms():

	if request.method == 'POST':

		new_dataset=get_processed_text(read_data)

		new_dataset=list(set(new_dataset))

		synonym_of = str(request.form['synonyms'])
		req_model = str(request.form['model'])

		#implementation
		current_model=pickle.load(open('model_nlp','rb'))
		if req_model == "GloVe":
			current_model = pickle.load(open('model_glove','rb'))
		if req_model == "FastText":
			current_model = pickle.load(open('model_fast','rb'))
		word=similar_one_out(new_dataset,synonym_of,current_model)
		word.sort(reverse=True,key=myFunc)
		word=word[:5]


		return render_template("wordAffiliation.html",synonyms=word)


@app.route('/antonyms', methods=['POST'])
def antonyms():

	if request.method == 'POST':

		new_dataset=get_processed_text(read_data)

		new_dataset=list(set(new_dataset))

		antonym_of = str(request.form['antonyms'])
		req_model = str(request.form['model'])

		#implementation
		current_model=pickle.load(open('model_nlp','rb'))
		if req_model == "GloVe":
			current_model = pickle.load(open('model_glove','rb'))
		if req_model == "FastText":
			current_model = pickle.load(open('model_fast','rb'))

		word=odd_one_out(new_dataset,antonym_of, current_model)

		word.sort(key=myFunc)

		word=word[:5]

		return render_template("wordAffiliation.html",antonyms=word)

@app.route('/wordrelations', methods=['POST'])
def wordrelations():

	if request.method == 'POST':

		new_dataset=get_processed_text(read_data)

		new_dataset=list(set(new_dataset))

		w1 = str(request.form['word1'])
		w2 = str(request.form['word2'])
		w3 = str(request.form['word3'])
		req_model = str(request.form['model'])

		#implementation
		current_model=pickle.load(open('model_nlp','rb'))
		if req_model == "GloVe":
			current_model = pickle.load(open('model_glove','rb'))
		if req_model == "FastText":
			current_model = pickle.load(open('model_fast','rb'))

		word=predict_word(w1,w2,w3,new_dataset, current_model)

		word.sort(reverse=True,key=myFunc)

		word=word[:5]

		return render_template("wordAffiliation.html",word4=word)

if __name__ == "__main__":
    app.run(debug=True)