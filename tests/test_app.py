# tests/test_app.py

import unittest
import json
from app import app

class FraudDetectionTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.sample_input = {
            "transaction_amount": 5000,
            "transaction_frequency": 12,
            "document_issue_date_diff": 365,
            "geo_distance": 8.2,
            "time_since_last_transaction": 3,
            "document_type_passport": 1,
            "channel_type_mobile": 1
        }

    def test_prediction_endpoint(self):
        response = self.client.post('/predict', 
                                    data=json.dumps(self.sample_input), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('fraud_prediction', data)
        self.assertIn(data['fraud_prediction'], [0, 1])

    def test_missing_field(self):
        incomplete_input = self.sample_input.copy()
        incomplete_input.pop('transaction_amount')
        response = self.client.post('/predict',
                                    data=json.dumps(incomplete_input),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_invalid_data_type(self):
        invalid_input = self.sample_input.copy()
        invalid_input['transaction_amount'] = "not_a_number"
        response = self.client.post('/predict',
                                    data=json.dumps(invalid_input),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_extra_fields_ignored(self):
        extra_input = self.sample_input.copy()
        extra_input['unexpected_field'] = 999
        response = self.client.post('/predict',
                                    data=json.dumps(extra_input),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('fraud_prediction', data)

if __name__ == '__main__':
    unittest.main()
