import os
import random
import requests
import operator
import re
import sys
from flask import Flask, render_template, request, session, redirect, url_for
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-sdfasdf2324'

def random_word():
    fname = "/app/app/simple-words.txt"
    lines = open(fname).read().splitlines()
    return random.choice(lines)

@app.route('/new', methods=['GET', 'POST'])
def new():
    errors = []
    typedword = []
    theword = []
    incorrect = []
    word_to_spell = random_word()
    print("New Word Requested", file=sys.stderr)
    print(word_to_spell, file=sys.stderr)
    session['word_to_spell'] = word_to_spell
    session['my_typed_word'] = []
    return render_template('new-word.html', word_to_spell=word_to_spell, errors=errors)



@app.route('/', methods=['GET', 'POST'])
def index():
    global word_to_spell
    errors = []
    typedword = []
    errors = []
    if 'word_to_spell' in  session:
        # If we have a session. Use it. If not, make one and get a word.
        print("Session detected. Using data.", file=sys.stderr)
        session['word_to_spell'] = word_to_spell
    else:
        word_to_spell = random_word()
        session['word_to_spell'] = word_to_spell

    if request.method == "POST":
        # get word that the person has entered
        try:
            typedword = request.form['myword']
        except:
            errors.append(
                "Unable to understand input. Please make sure it's valid and try again."
            )
        session['my_typed_word'] = typedword.rstrip()
        theword = typedword.rstrip()
        print("I know", file=sys.stderr)
        print(theword, file=sys.stderr)
        print(word_to_spell, file=sys.stderr)

    # I have result now. Check it. 
  
    theword = session.get('my_typed_word')
    word_to_spell = session.get('word_to_spell')
    if (  theword ) : 
        print("The Get THigns", file=sys.stderr)
        print(theword, file=sys.stderr)
        print(len(theword), file=sys.stderr)
        print(word_to_spell, file=sys.stderr)
        print(len(word_to_spell), file=sys.stderr)
        if str(word_to_spell) == str(theword):
            print("I am equal", file=sys.stderr)
            incorrect = []
            correct = "True" 
        else:
            incorrect = "True"
            correct = []
        # Return from within the post
        return render_template('index.html', word_to_spell=word_to_spell, errors=errors, theword=theword, correct=correct, incorrect=incorrect)

     
    return render_template('index.html', word_to_spell=word_to_spell, errors=errors)


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)



