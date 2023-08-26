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
    int_features = [int(x) for x in request.form.values()]

    # Sending to model for prediction
    prediction = model.predict([np.array(int_features)])

    # Rounding off Output to 3 decimal values using the numpy round function (Since this is a numpy array we cannot use round function for integers)
    output = np.round(prediction[0],3)

    # Returning Argument from function
    # We need to convert output to float else it will show output as numpy array
    return render_template('/index.html', prediction_text='Employee Salary should be $ {}'.format(float(output)))

# Main function
# This is where the execution begins
if __name__ == "__main__":

    # When we call this, it runs the base function or home function
    # Debuging is checking for errors in program
    # When we give debug argument as True, it directly debugs the programs and show errors or exceptions if occured
    app.run(debug=True)