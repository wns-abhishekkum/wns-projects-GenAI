# FastAPI Sentiment Analysis API

This project implements a **Sentiment Analysis API** using **FastAPI** and **scikit-learn**. It allows training a machine learning model on text data (customer feedback, reviews, etc.) and predicting sentiment as **positive**, **negative**, or **neutral**.


---

## 🚀 Features

- Sentiment classification using:
  - **Naive Bayes (MultinomialNB)**
  - **Support Vector Machines (LinearSVC)**
- Text preprocessing with **TF-IDF vectorization**
- REST API built with **FastAPI**
- Endpoints:
  - `POST /train` → Train the model using uploaded dataset
  - `POST /predict` → Predict sentiment for input text
  - `GET /health` → Health check
- Model persistence with `joblib`

---

## 📂 Project Structure

```
fastapi-sentiment-analysis/
├── app/
│   ├── main.py                # FastAPI application
│   ├── model_utils.py         # Model training & prediction logic
│   └── schemas.py             # Request/response models
├── data/
│   └── sample.csv             # Example dataset
├── models/
│   └── sentiment_model.joblib # Saved trained model
├── train_model.py             # Standalone training script
├── requirements.txt           # Dependencies
├── Dockerfile                 # Container setup
└── README.md                  # Project documentation
```

---

## 🛠 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/fastapi-sentiment-analysis.git
cd fastapi-sentiment-analysis
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI app:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Open Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Example Usage

### Train the Model

Upload a CSV file (`text,label` format):

```bash
curl -X POST "http://127.0.0.1:8000/train" \
  -F "file=@data/sample.csv" \
  -F "algorithm=nb"
```

### Predict Sentiment

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product, works great!"}'
```

**Response:**

```json
{
  "text": "I love this product, works great!",
  "sentiment": "positive",
  "scores": {"negative": 0.02, "neutral": 0.10, "positive": 0.88}
}
```

---

## 🧪 Example Dataset

`data/sample.csv`:

```csv
text,label
"I loved the product, it worked great",positive
"Terrible service, will not return",negative
"It was ok, nothing special",neutral
```

---

## 🐳 Run with Docker

1. Build the image:

```bash
docker build -t fastapi-sentiment .
```

2. Run the container:

```bash
docker run -p 8000:8000 fastapi-sentiment
```

---

## ⚡ Future Improvements

- Add **transformer models** (e.g., BERT, DistilBERT)
- Deploy to **AWS / Azure / GCP**
- Add **unit tests & CI/CD pipelines**

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use and modify it for your needs.


## Output

run the test.py    ## to generate sentiments.
