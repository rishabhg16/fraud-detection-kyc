# app.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load('fraud_rf_model.pkl')

# Define feature list (must match training)
expected_features = [
    'transaction_amount',
    'transaction_frequency',
    'document_issue_date_diff',
    'geo_distance',
    'time_since_last_transaction',
    'document_type_passport',
    'channel_type_mobile'
]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    df = df.reindex(columns=expected_features, fill_value=0)
    prediction = model.predict(df)[0]
    return jsonify({'fraud_prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
