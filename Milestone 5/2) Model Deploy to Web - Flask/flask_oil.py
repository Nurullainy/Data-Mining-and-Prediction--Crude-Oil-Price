#!/usr/bin/env python
# coding: utf-8

# ## WQD 7005 Data Mining
# ## Project Title: Crude Oil Price Prediction
#
# ### Milestone 5: Deployment in web (Flask)
#
#
# ##### Team member:
# 1) Nurullainy binti Mat Rashid 17036591

# In[3]:


from flask import Flask, render_template, request
from model import oil_predict

app = Flask(__name__)


# Render default webpage
# When the post method detect, then redirect to success function
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':  # Render a template when the route is triggered with GET method
        return render_template('index.html')
    if request.method == 'POST':  # Read form inputs and register a user if route is triggered with POST
        button = request.form.get('submitbutton')
        return render_template('index.html',
                               output=model.oil_predict(float(int)),
                               user_text=text)


# Get the data for the requested query
@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == "__main__":
    app.run()

