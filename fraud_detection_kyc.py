# fraud_detection_kyc.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Load your dataset (assuming CSV format)
data = pd.read_csv('kyc_transactions.csv')

# Basic preprocessing
data = data.dropna()

# Feature selection - assuming these columns exist
features = [
    'transaction_amount',
    'transaction_frequency',
    'document_issue_date_diff',
    'document_type',
    'geo_distance',
    'time_since_last_transaction',
    'channel_type'
]

# Convert categorical features if any
data = pd.get_dummies(data, columns=['document_type', 'channel_type'], drop_first=True)

X = data[features + [col for col in data.columns if col.startswith('document_type_') or col.startswith('channel_type_')]]
y = data['is_fraud']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(clf, 'fraud_rf_model.pkl')

# Example prediction function
def predict_fraud(input_dict):
    input_df = pd.DataFrame([input_dict])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=X.columns, fill_value=0)
    model = joblib.load('fraud_rf_model.pkl')
    return model.predict(input_df)[0]

# Sample usage
if __name__ == '__main__':
    sample_input = {
        'transaction_amount': 5000,
        'transaction_frequency': 12,
        'document_issue_date_diff': 365,
        'geo_distance': 8.2,
        'time_since_last_transaction': 3,
        'document_type_passport': 1,
        'channel_type_mobile': 1
    }
    print(f"Fraud Prediction: {predict_fraud(sample_input)}")
