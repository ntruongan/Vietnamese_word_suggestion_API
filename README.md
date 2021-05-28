# Vietnamese typing suggestion 

## Overview

<p>Project provide a tool for typing suggestion in Vietnamese</p>

## API ##

  I had written the API with Flask library support. </br>
URL to predict API: http://localhost:5000/predict. </br>
Request to API: is detemined in json <code>{"input_": input_}</code> with value of key "input_" is string variable.
Reponse: json with 2 keys <code>"predictions"</code> and <code>"success"</code> are string and boolean respectively.
The brain of API is Deep Learning NLP model which built on keras.

## Model ## 
Simple Sequential Keras model. Consist of 1 embedding layers, 2 LSTM layers followed by fully connected network (2 dense layers).

## Dataset ##
Dataset is How I met your mother - vietnamese subtitle which preprocessed in how-i-met-your-mother-second-season_vietnamese directory(<a href="https://www.kaggle.com/annguyntrng/how-i-met-your-mother-vietnamese-sub">more detail about dataset</a>)

# How to use API #
<ol>
<li>Download project</li>
<li>Open terminal in project's directory <code>python API.py</code> to run API on localhost</li>
<li>Use other python IDE to compile WORD_PRED_WINDOWS.py file as client request to API</li>
<li>Type on a input field. The client will send a request whenever the input field changes and show suggestion at the bottom of window</li>
</ol>



