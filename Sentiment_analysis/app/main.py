from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import io
from app import model_utils
from app.schemas import TextInput, PredictResponse

app = FastAPI(title="Sentiment Analysis API")

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API! Use /docs for API documentation."}


@app.get('/health')
def health():
    return {"status": "ok"}

@app.post('/train')
async def train(algorithm: str = Form('nb'), file: UploadFile = File(None)):
    """
    Train a sentiment model from an uploaded CSV file.

    Args:
        algorithm (str): Algorithm to use ('svm'). 
        file (UploadFile): CSV file with 'text' and 'label' columns.

    Returns:
        JSONResponse: Training status and classification report.

    Raises:
        HTTPException: If file is missing, invalid, or parsing fails.
    """
    if file is None:
        raise HTTPException(status_code=400, detail='CSV file required')

    contents = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Failed to parse CSV: {e}')

    if not {'text','label'}.issubset(df.columns):
        raise HTTPException(status_code=400, detail="CSV must contain 'text' and 'label' columns")

    report = model_utils.train_from_dataframe(df, algorithm=algorithm)
    return JSONResponse(content={"status": "trained", "report": report})

@app.post('/predict', response_model=PredictResponse)
async def predict(input: TextInput):
    """
    Predict sentiment for a given text.

    Args:
        input (TextInput): Request body with 'text'.

    Returns:
        PredictResponse: Input text, predicted sentiment, and optional scores.

    Raises:
        HTTPException: If no trained model is found.
    """
    try:
        out = model_utils.predict_text(input.text)
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return PredictResponse(text=input.text, sentiment=out['label'], scores=out.get('scores'))
