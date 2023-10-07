from joblib import load
from flask import Flask, request, jsonify
import sqlite3

model = load('forecaster.joblib')
app = Flask(__name__)


@app.route('/get_student', methods=['GET'])
def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT feature1, feature2, feature3, feature4 FROM student LIMIT 1')
    data_row = cursor.fetchone()
    conn.close()

    data_dict = {'features': list(data_row)}

    return jsonify(data_dict)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features')
    features_list = list(features)
    result = model.predict(features_list)

    return jsonify({'prediction': result.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
