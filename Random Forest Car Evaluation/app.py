# This model was made in scikit learn version 1.0.2
# If while running this model any error is encountered first execute pip install scikit-learn==1.0.2 this command to resort to scikit-learn previous version
# Instead of this the model can be remade in scikit-learn 1.0.3 and after that execute this, it will work
# Instead of joblib pickle can be used as well
# joblib is used because it is compatible with most versions of scikit-learn
# After predicting output it displays the text till next input is given

# Importing Required Libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
# joblib can also be used for model
import joblib

# Initializing Flask app
app = Flask(__name__)
model = joblib.load('model.pkl')

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
    # For Geting Input from HTML Form
    int_features = [int(x) for x in request.form.values()]

    # Converting Values to numpy array
    final_features = [np.array(int_features)]

    # Sending to model for prediction
    prediction = model.predict(final_features)

    if prediction==0:
        res="Unacceptable Condition"
    elif prediction==1:
        res='Acceptable Condition'
    elif prediction==2:
        res='Good Condition'
    else:
        res='Very Good Condition'


    return render_template('index.html', prediction_text='Car Evaluation is: {}'.format(res))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)