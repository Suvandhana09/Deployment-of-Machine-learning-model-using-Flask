from flask import Flask, render_template,request
import joblib

app = Flask(__name__)
model = joblib.load(open('joblib1.pkl','rb'))

@app.route('/home')
def home():
    return render_template('index.html');

@app.route('/classify',methods=['GET'])
def classify_type():
        sepal_len = request.args.get('slen') # Get parameters for sepal length
        sepal_wid = request.args.get('swid') # Get parameters for sepal width
        petal_len = request.args.get('plen') # Get parameters for petal length
        petal_wid = request.args.get('pwid') # Get parameters for petal width


        # Get the output from the classification model
        variety = model.predict([[sepal_len, sepal_wid, petal_len, petal_wid]])

        # Render the output in new HTML page
        return render_template('output.html', variety=variety)

if(__name__=='__main__'):
    app.run(debug=True)









