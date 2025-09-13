import requests

# Send text to your API
resp = requests.post(
    "http://127.0.0.1:8000/predict",
    # json={"text": "The service was terrible, I am disappointed"}
    # json={"text": "I love the new design, it is fantastic!"}
    json={"text": "The product is okay, not too bad but could be better."}
)

data = resp.json()
print("Full response:", data)

# Extract just the sentiment
# print("Sentiment:", data["sentiment"])
