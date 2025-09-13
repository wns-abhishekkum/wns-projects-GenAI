import os
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import pandas as pd

MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, 'sentiment_model.joblib')

LABEL_MAP = {0: 'negative', 1: 'neutral', 2: 'positive'}

def build_pipeline(algorithm: str = 'nb'):
    """
    Build a text classification pipeline with TF-IDF and classifier.

    Args:
        algorithm (str): 'svm' (SVM). Default: 'nb'.

    Returns:
        sklearn.pipeline.Pipeline
    """
    vect = TfidfVectorizer(strip_accents='unicode', lowercase=True, ngram_range=(1,2), max_df=0.9)
    if algorithm == 'svm':
        base = LinearSVC(max_iter=2000)
        clf = CalibratedClassifierCV(base)
    else:
        clf = MultinomialNB()
    pipeline = make_pipeline(vect, clf)
    return pipeline

def train_from_dataframe(df: pd.DataFrame, algorithm: str = 'nb'):
    """
    Train sentiment model from DataFrame and save it.

    Args:
        df (pd.DataFrame): Must have 'text' and 'label' columns.
        algorithm (str):'svm'. Default: 'nb'.

    Returns:
        dict: Classification report.
    """
    label_map_inv = {'negative': 0, 'neutral': 1, 'positive': 2}
    def normalize_label(x):
        if isinstance(x, str):
            return label_map_inv[x.lower()]
        else:
            return int(x)

    df = df.dropna(subset=['text', 'label'])
    df['label'] = df['label'].apply(normalize_label)

    X = df['text'].astype(str)
    y = df['label'].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    pipeline = build_pipeline(algorithm)
    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)
    report = classification_report(y_test, preds, target_names=['negative','neutral','positive'], output_dict=True)

    joblib.dump({'pipeline': pipeline, 'label_map': LABEL_MAP, 'algorithm': algorithm}, MODEL_PATH)
    return report

def load_model():
    """
    Load trained sentiment model from disk.

    Returns:
        dict or None: Model data if exists, else None.
    """
    if not os.path.exists(MODEL_PATH):
        return None
    data = joblib.load(MODEL_PATH)
    return data

def predict_text(text: str):
    """
    Predict sentiment for given text.

    Args:
        text (str): Input text.

    Returns:
        dict: Predicted label and optional scores.

    Raises:
        RuntimeError: If no trained model is found.
    """
    model_pkg = load_model()
    if model_pkg is None:
        raise RuntimeError("Model not found. Train first.")
    pipeline = model_pkg['pipeline']
    label_map = model_pkg['label_map']

    pred_label = pipeline.predict([text])[0]
    result = {'label': label_map[int(pred_label)]}

    try:
        probs = pipeline.predict_proba([text])[0]
        score_map = {label_map[i]: float(probs[i]) for i in range(len(probs))}
        result['scores'] = score_map
    except Exception:
        result['scores'] = None

    return result
