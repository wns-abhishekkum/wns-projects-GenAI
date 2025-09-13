
from pydantic import BaseModel
from typing import List, Optional

class TextInput(BaseModel):
    """
    Input schema for sentiment prediction requests.

    Attributes:
        text (str): The input text for which the sentiment needs to be predicted.
    """
    text: str


class PredictResponse(BaseModel):
    """
    Response schema for sentiment prediction results.

    Attributes:
        text (str): The original input text.
        sentiment (str): The predicted sentiment label ("positive", "negative", "neutral").
        scores (Optional[dict]): A dictionary of sentiment class probabilities or confidence scores.
    """
    text: str
    sentiment: str
    scores: Optional[dict] = None


class TrainRequest(BaseModel):
    """
    Request schema for training a sentiment analysis model.

    Attributes:
        algorithm (Optional[str]): The algorithm to use for training.
                                   Default is "nb". Options: "nb" (Naive Bayes), "svm" (Support Vector Machine).
        overwrite (Optional[bool]): Whether to overwrite the existing model if one exists.
                                    Default is True.
    """
    algorithm: Optional[str] = "nb"  # 'nb' or 'svm'
    overwrite: Optional[bool] = True
