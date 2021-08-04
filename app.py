import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import mysql.connector
from mysql.connector import errorcode
from flask_mysqldb import MySQL



app = Flask(__name__)
app.config['MYSSQL_HOST']='localhost'
app.config['MYSSQL_USER']='root'
app.config['MYSSQL_PASSWORD']=''
app.config['MYSSQL_DB']='banque_bd'

mysql=MySQL(app)


model = pickle.load(open('model4.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index1.html', prediction_text='La Prédiction est : $ {}'.format(output))

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)