import requests

# URL of your FastAPI endpoint
url = "http://127.0.0.1:8000/process_file"

# Open the PDF file in binary mode
with open("ngvcapamt.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

# Print JSON response from server
print(response.json())
