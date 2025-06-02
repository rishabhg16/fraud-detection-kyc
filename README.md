# Fraud Detection KYC 🔍

A production-ready fraud detection system using a Random Forest Classifier. It analyzes transaction patterns and document metadata to flag potentially fraudulent KYC activity.

---

## 🧠 Features

* Random Forest Classifier for fraud detection
* Handles document metadata and transaction features
* Flask API for real-time predictions
* Dockerized for seamless deployment
* GitHub Actions for automated testing & deployment

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/fraud-detection-kyc.git
cd fraud-detection-kyc
pip install -r requirements.txt
```

---

## 🚀 Usage

### Train the model:

```bash
python fraud_detection_kyc.py
```

### Run the Flask API:

```bash
python app.py
```

### API Endpoint

```
POST /predict
Content-Type: application/json

{
  "transaction_amount": 5000,
  "transaction_frequency": 12,
  "document_issue_date_diff": 365,
  "geo_distance": 8.2,
  "time_since_last_transaction": 3,
  "document_type_passport": 1,
  "channel_type_mobile": 1
}
```

Response:

```json
{"fraud_prediction": 0}
```

---

## 🐳 Docker

```bash
docker build -t fraud-detector .
docker run -p 5000:5000 fraud-detector
```

---

## ⚙️ GitHub Actions

CI/CD pipeline runs tests on push to `main` and builds the Docker container.

---

## 📁 Project Structure

```
fraud-detection-kyc/
│
├── fraud_detection_kyc.py
├── app.py
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## 📜 License

MIT
