# Machine-Learning-Projects-In-Python
This repository contains machine learning projects in the Python programming language.<br><br>
<img width="916" height="430" src="https://github.com/madhurimarawat/Machine-Learning-Projects-In-Python/assets/105432776/ed1f6973-69bc-4909-9747-6ac98080d775">

---
# Mode of Execution Used <img src="https://th.bing.com/th/id/R.c936445e15a65dfdba20a63e14e7df39?rik=fqWqO9kKIVlK7g&riu=http%3a%2f%2fassets.stickpng.com%2fimages%2f58481537cef1014c0b5e4968.png&ehk=dtrTKn1QsJ3%2b2TFlSfLR%2fxHdNYHdrqqCUUs8voipcI8%3d&risl=&pid=ImgRaw&r=0" title="PyCharm" alt="PyCharm" width="40" height="40"> <img src="https://www.pngfind.com/pngs/m/128-1286693_flask-framework-logo-svg-hd-png-download.png" title="Flask API" alt="Flask API" width="40" height="40">

## Pycharm
--> Visit the official website of pycharm: <a href="https://www.jetbrains.com/pycharm/"><img src="https://th.bing.com/th/id/R.c936445e15a65dfdba20a63e14e7df39?rik=fqWqO9kKIVlK7g&riu=http%3a%2f%2fassets.stickpng.com%2fimages%2f58481537cef1014c0b5e4968.png&ehk=dtrTKn1QsJ3%2b2TFlSfLR%2fxHdNYHdrqqCUUs8voipcI8%3d&risl=&pid=ImgRaw&r=0" title="PyCharm" alt="PyCharm" width="40" height="40"></a><br><br>
--> Download according to the platform that will be used like Linux, Macos or Windows.<br><br>
--> Follow the setup wizard and sign up for the free version (trial version) or else continue with the premium or paid version.<br><br>
--> First, in pycharm we have the concept of virtual environment. In virtual environment we can install all the required libraries or frameworks.<br><br>
--> Each project has its own virtual environment, so thath we can install requirements like Libraries or Framworks for that project only.<br><br>
--> After this we can create a new file, various file types are available in pycharm like script files, text files and also Jupyter Notebooks.<br><br>
--> After selecting the required file type, we can continue the execution of that file by saving it and using this shortcut shift+F10 (In Windows).<br><br>
--> Output is given in Console while installation happens in terminal in Pycharm.<br>

## Flask Server

--> Flask is a micro web framework written in Python.<br><br>
--> It is classified as a microframework because it does not require particular tools or libraries.<br><br>
--> Flask supports extensions that can add application features as if they were implemented in Flask itself.
--> To install flask in your system, just run this command-

```
pip install flask
```

## Running Project in Flask Server
<p>Make Sure all depencies are already satisfied before running the app.</p>

1. Ensure that you are in the project home directory.Create the machine learning model by running below command - <br><br>
--> This machine_learning_model.py file contains the code for the amachine learning model.

```
python machine_learning_model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API  <br><br>
--> This app.py file contains the code for the flask app
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :

<img width="916" height="430" title="Homepage" alt="Homepage" src="https://github.com/madhurimarawat/Machine-Learning-Python-Projects/assets/105432776/cae7ee43-1fee-42ba-a746-b7c9df04b496">
<br>
Enter valid numerical values in all the input boxes and hit Predict. Here I have entered 8.<br><br>

If everything goes well, Predicted Value will be shown on the HTML page! <br>

<img width="916" height="430"  alt="Screenshot 2023-08-26 133516" src="https://github.com/madhurimarawat/Machine-Learning-Python-Projects/assets/105432776/5f3d7615-2972-4786-8681-7d1f0e280b2f"><br>

🌟 Project and Models will change but this process will remain the same for all flask projects.

---
# About Projects 📑
<p>Complete Description about the project and resources used.</p>

## Project Structure
Each project has four major parts :
1. machine_learning_mode.py - This contains code for Machine Learning model to predict output based on input from a dataset file.
2. app.py - This contains Flask APIs that receives details through GUI or API calls, computes the precited value based on our model and returns it.
3. templates - This folder contains the HTML template to allow user to enter details and displays the predicted value.
4. static- This folder contains the css for the HTML file.

# Linear Regression Salary Prediction

--> First ML model is constructed using linear regression for the dataset.<br><br>
--> Then this model is saved using pickle in disk with the extention .pkl(Pickle File).<br><br>
--> The Homepage is designed for flask app.<br><br>
--> After this the flask app code is written.<br><br>
--> Finally we can run this app in the flask Server.<br>

## Dataset Used

### Salary Dataset
--> Dataset is taken from: <a href="https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression
"><img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-1024.png" height =40 width=40 title="Salary Dataset" alt="Salary Dataset"> </a><br><br>
--> Contains Salary data for Regression.<br><br>
--> The dataset has 2 columns-Years of Experience and Salary and 30 entries.<br><br>
--> Column Years of Experience is used to find regression for Salary.<br><br>
--> Dataset is already cleaned,no preprocessing required.<br>

## Algorithm Used
<h3>Linear Regression</h3>
--> Regression: It predicts the continuous output variables based on the independent input variable. like the prediction of house prices based on different parameters like house age, distance from the main road, location, area, etc.<br><br>
--> It computes the linear relationship between a dependent variable and one or more independent features. <br><br>
--> The goal of the algorithm is to find the best linear equation that can predict the value of the dependent variable based on the independent variables.<br>

# Naive Bayes Classifier Diabetes Prediction

--> First ML model is constructed using Naive Bayes Classifier for the dataset.<br><br>
--> Then this model is saved using pickle in disk with the extention .pkl(Pickle File).<br><br>
--> The Homepage is designed for flask app.<br><br>
--> After this the flask app code is written.<br><br>
--> Finally we can run this app in the flask Server.<br>

## Dataset Used

### Naive bayes classification data
--> Dataset is taken from: <a href="https://www.kaggle.com/datasets/himanshunakrani/naive-bayes-classification-data"><img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-1024.png" height =40 width=40 title="Naive bayes classification data"> </a><br><br>
--> Contains diabetes data for classification.<br><br>
--> The dataset has 3 columns-glucose, blood pressure and diabetes and 995 entries.<br><br>
--> Column glucose and blood pressure data is to classify whether the patient has diabetes or not.<br><br>
--> Dataset is already cleaned,no preprocessing required.<br>

## Algorithm Used

<h3>Naive Bayes Classifiers</h3>
--> Naive Bayes classifiers are a collection of classification algorithms based on Bayes’ Theorem. <br><br>
--> It is not a single algorithm but a family of algorithms where all of them share a common principle, i.e. every pair of features being classified is independent of each other.<br><br>
--> The fundamental Naive Bayes assumption is that each feature makes an independent and equal contribution to the outcome.

# Random Forest Car Evaluation

--> First ML model is constructed using Naive Bayes Classifier for the dataset.<br><br>
--> Then this model is saved using joblib in disk with the extention .pkl(Pickle File).<br><br>
--> The Homepage is designed for flask app.<br><br>
--> After this the flask app code is written.<br><br>
--> Finally we can run this app in the flask Server.<br>

## Dataset Used
### Cars Evaluation Dataset
--> Dataset is taken from: <a href="https://www.kaggle.com/datasets/elikplim/car-evaluation-data-set"><img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-1024.png" height =40 width=40 title="Cars Evaluation Dataset" alt="Cars Evaluation Dataset"> </a><br><br>
--> Contains information about cars with respect to features like Attribute Values:<br><br>
<table>
<td>1. buying v-high, high, med, low </td>
<td>2.maint v-high, high, med, low </td>
<td>3.doors 2, 3, 4, 5-more </td>
<td>4. persons 2, 4, more </td>
<td>5. lug_boot small, med, big</td>  
<td>6.safety low, med, high</td>  </table>
--> Target categories are:<br><br>
<table>
  <td>1. unacc 1210 (70.023 %)</td>
  <td>2. acc 384 (22.222 %)</td>
  <td>3. good 69 ( 3.993 %)</td>
  <td>4. v-good 65 ( 3.762 %)</td></table>
--> Contains Values in string format.<br><br>
--> Dataset is not cleaned, preprocessing is required.<br>

## Algorithm Used

<h3>Random Forest</h3>
--> It is based on the concept of ensemble learning, which is a process of combining multiple classifiers to solve a complex problem and to improve the performance of the model.<br><br>
--> Instead of relying on one decision tree, the random forest takes the prediction from each tree and based on the majority votes of predictions, and it predicts the final output.<br><br>
--> The greater number of trees in the forest leads to higher accuracy and prevents the problem of overfitting.

---
## Libraries Used 📚
<p>Short Description about all libraries used in Project.</p>
To install python library this command is used-<br><br>

```
pip install library_name
```
<ul>
  <li>NumPy (Numerical Python) – Enables with collection of mathematical functions
to operate on array and matrices. </li>
  <li>Pandas (Panel Data/ Python Data Analysis) - This library is mostly used for analyzing,
cleaning, exploring, and manipulating data.</li>
  <li>Matplotlib - It is a data visualization and graphical plotting library.</li>
<li>Scikit-learn - It is a machine learning library that enables tools for used for many other
machine learning algorithms such as classification, prediction, etc.</li>
  <li>Pickle- The pickle module is used for implementing binary protocols for serializing and de-serializing a Python object structure.</li>
  <li>Joblib- Joblib is a set of tools to provide lightweight pipelining in Python. In particular transparent disk-caching of functions and lazy re-evaluation (memoize pattern) and easy simple parallel computing.</li>
</ul>

---
### Additional Resources 🧮📚📓🌐

<p> To see more of my machine learning models, visit my repository: https://github.com/madhurimarawat/Machine-Learning-Using-Python </p>

---

## Thanks for Visiting 😄

- Drop a 🌟 if you find this repository useful.<br><br>
- If you have any doubts or suggestions, feel free to reach me.<br><br>
📫 How to reach me:  &nbsp; [![Linkedin Badge](https://img.shields.io/badge/-madhurima-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/madhurima-rawat/) &nbsp; &nbsp;
<a href ="mailto:rawatmadhurima@gmail.com"><img src="https://github.com/madhurimarawat/Machine-Learning-Using-Python/assets/105432776/b6a0873a-e961-42c0-8fbf-ab65828c961a" height=35 width=30 title="Mail Illustration" alt="Mail Illustration📫" > </a><br><br>
- **Contribute and Discuss:** Feel free to open <a href= "https://github.com/madhurimarawat/Machine-Learning-Projects-In-Python/issues">issues 🐛</a>, submit <a href = "https://github.com/madhurimarawat/Machine-Learning-Projects-In-Python/pulls">pull requests 🛠️</a>, or start <a href = "https://github.com/madhurimarawat/Machine-Learning-Projects-In-Python/discussions">discussions 💬</a> to help improve this repository!
