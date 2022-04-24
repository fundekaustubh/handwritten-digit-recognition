from distutils.log import debug
from flask import Flask, render_template, request, redirect, url_for
import keras
from keras.models import load_model

model = load_model('digitClassifier.h5')
app = Flask(__name__)
@app.route('/', methods=["GET"])
def home():
    if request.method == 'GET':
        return render_template('index.html', text="hello")

@app.route('/classifier', methods=["POST"])
def classifier():
    if request.method == 'POST':
        print('Hit the classifier POST route!')
        return redirect('http://localhost:5000/')

app.run(debug=True)
