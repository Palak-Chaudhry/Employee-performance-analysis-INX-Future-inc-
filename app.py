from matplotlib.cbook import ls_mapper
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import funcs as f

app = Flask(__name__)
model_pkl = pickle.load(open('model_gridrf.pkl', 'rb'))
sc_pkl = pickle.load(open('sc.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    X,Y = f.read_file()
    X1 = X.copy()
    mapping = f.map_cat_col(X1)
    int_features = [int(x) for x in request.form.values()]
    int_features[7] = f.get_key_EmpDepartment(int_features[7],mapping)
    int_features[8] = f.get_key_OverTime(int_features[8],mapping)
    int_features[9] = f.get_key_EmpJobRole(int_features[9],mapping)
    X.loc[len(X)] = int_features
    y = f.prep_input(X)
    y = y.loc[[len(X)-1]]
    y= sc_pkl.transform(y)
    output = model_pkl.predict(y)

    return render_template('index.html', prediction_text='Employee Performance rating should be {}'.format(output[0]))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model_pkl.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)