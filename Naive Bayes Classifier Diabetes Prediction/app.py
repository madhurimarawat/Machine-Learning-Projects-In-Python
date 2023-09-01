# Importing Required Libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Initializing Flask app
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Giving Path to app
# This will redirect to index.html which is our homepage
@app.route('/')

# Function for homepage
# This the base function
# render_template is used to access html template
def home():
    return render_template('/index.html')

# Sending Input to Predict i.e Model to give Result
@app.route('/predict',methods=['POST'])

# Function for predicting output
def predict():

    '''
    For rendering results on HTML GUI
    '''
   
    # Storing Input from HTML form/User Input
    glucose=int(request.form.get('glucose'))
    bloodpressure=int(request.form.get('bloodpressure'))

    # Sending to model for prediction
    output = model.predict([[glucose,bloodpressure]])

    # Since Output values will be 0 for not diabetic and 1 for diabetic we have to print according to that
    if output==0:
        res="Not Diabetic"
    else:
        res="Diabetic"
    
    # Returning Argument from function
    # We need to convert output to float else it will show output as numpy array
    return render_template('/index.html', prediction_text='Diabetes Prediction is: {}'.format(res))

# Main function
# This is where the execution begins
if __name__ == "__main__":

    # When we call this, it runs the base function or home function
    # Debuging is checking for errors in program
    # When we give debug argument as True, it directly debugs the programs and show errors or exceptions if occured
    app.run(debug=True)