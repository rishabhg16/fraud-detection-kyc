# tests/test_app_extreme.py

import unittest
import json
from app import app

class FraudDetectionExtremeValuesTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.base_input = {
            "transaction_amount": 5000,
            "transaction_frequency": 12,
            "document_issue_date_diff": 365,
            "geo_distance": 8.2,
            "time_since_last_transaction": 3,
            "document_type_passport": 1,
            "channel_type_mobile": 1
        }

    def test_negative_transaction_amount(self):
        input_data = self.base_input.copy()
        input_data["transaction_amount"] = -1000
        response = self.client.post('/predict', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fraud_prediction', json.loads(response.data))

    def test_extremely_large_geo_distance(self):
        input_data = self.base_input.copy()
        input_data["geo_distance"] = 1000000
        response = self.client.post('/predict', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fraud_prediction', json.loads(response.data))

    def test_zero_frequency(self):
        input_data = self.base_input.copy()
        input_data["transaction_frequency"] = 0
        response = self.client.post('/predict', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fraud_prediction', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()
