# Deployment-of-Machine-learning-model-using-Flask

## Requirements 

1. Iris dataset
2. Python notebook or python environment
3. Numpy,pandas,scikit-learn and joblib libraries
4. Flask server

  In this project Iris dataset was choosen to build the model by using logistic regression. Here Joblib library was used to export(dump) the model from python notebook and import(load) that file to flask code.Need to create Virtual environment to run the flask
#### Why do we need virtual environment
  For example, you are working on project A which requires Python’s library A(site package) version 1.0 while another project B requires the same library A but newer version 1.3. In such situations, a virtual environment can be really useful to maintain the dependencies of both projects.
  
 ## Procedure for project 
  
  1. Choose a seperate folder where flask server will run for the project.
  2. Go to command prompt -> change directory to that folder where flask will run
  3. Install Virtual environment "pip install virtualenv"
  4. create a virtual environment for the folder by using following command 'python -m venv <name of environment>'
  5. Activate the environment by using following command '<name of environment>\Scripts\activate'
  6. Now Install flask by using following command 'pip install flask' (Flask will be installed for that environment)
  7. Write the code in python file by initialising flask
  8. Now use the command to set the flask app with python file 'set FLASK_APP=app.py'
  9. Type the command "flask run". If there are any errors in the code error will be displayed or server will start and give us following url to check the output- http://127.0.0.1:5000/
  10. click or copy paste the url in the browser by using following path which was declared in python file . In my code i have given my function declaration as '/home' so i will use following url 'http://127.0.0.1:5000/home'.
  11. check the output by giving values in html page.
