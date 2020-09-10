import os
import random
import requests
import operator
import re
import sys
import awsgi
from flask import Flask, render_template, request, session, redirect, url_for
from bs4 import BeautifulSoup

import logging
logging.getLogger().setLevel(logging.INFO)
logging.info("Hello World!")


app = Flask(__name__)
app.config.update(
    #Set the secret key to a sufficiently random value
    SECRET_KEY=os.urandom(24),
    #Set the session cookie to be secure
    SESSION_COOKIE_SECURE=True,
    #Set the session cookie for our app to a unique name
    SESSION_COOKIE_NAME='SightWOrds-WebSession',
    #Set CSRF tokens to be valid for the duration of the session. This assumes you’re using WTF-CSRF protection
    WTF_CSRF_TIME_LIMIT=None
)


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

def random_word():
    dir = os.path.dirname(__file__)
    fname = os.path.join(dir, 'wordlists/simple-words.txt')
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
    if session.get('word_to_spell'):
    #if 'word_to_spell' in  session:
        # If we have a session. Use it. If not, make one and get a word.
        print("Session detected. Using data.", file=sys.stderr)
        word_to_spell = session['word_to_spell']
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
        if re.match(word_to_spell, theword, re.IGNORECASE):
            print("I am equal", file=sys.stderr)
            incorrect = []
            correct = "True" 
        else:
            incorrect = "True"
            correct = []
        # Return from within the post
        return render_template('index.html', word_to_spell=word_to_spell, errors=errors, theword=theword, correct=correct, incorrect=incorrect)

     
    return render_template('index.html', word_to_spell=word_to_spell, errors=errors)


