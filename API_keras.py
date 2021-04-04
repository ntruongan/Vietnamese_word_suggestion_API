# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:09:06 2021

@author: ntruo
"""

# USAGE
# Start the server:
# 	python run_keras_server.py
# Submit a request via cURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
# Submita a request via Python:
#	python simple_request.py

# import the necessary packages


import tensorflow as tf
import flask
import pandas as pd
from keras.preprocessing.sequence import pad_sequences


# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None
max_seq_len = None
tokenizer = None
num_word = None 

def load_model():
	# load the pre-trained Keras model (here we are using a model
	# pre-trained on ImageNet and provided by Keras, but you can
	# substitute in your own networks just as easily)
    global model
    global tokenizer
    global max_seq_len
    global num_word
    global word2id
    model = tf.keras.models.load_model('word_pre_74.h5')
    tokenizer = pd.read_pickle("tokenizer.t")
    max_seq_len = pd.read_pickle("max_seq_len.pad")
    num_word = pd.read_pickle("num_word.pad")
    word2id = pd.read_pickle("word2idx.t")
#%%

def prepare_input(input_):
    
    input_ = input_.strip().lower()
    input_ = tokenizer.texts_to_sequences([input_])
    input_  = pad_sequences(input_, max_seq_len, padding = 'post')
    print(input_)
    return input_

@app.route("/predict", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
    data = {"success": False}

	# ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("input_"):
            input_ = flask.request.files["input_"].read().decode("utf-8")
            # input_ =  flask.request.data('input_')
            print(type(input_))
            input_ = prepare_input(input_)

            preds = model.predict(input_).argmax()
            pred_word = tokenizer.index_word[preds]
            data["predictions"] = [pred_word]

            data["success"] = True

	# return the data dictionary as a JSON response
    return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading Keras model and Flask starting server..."
		"please wait until server has fully started"))
	load_model()
	app.run(debug=True)