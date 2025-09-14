import requests

API_URL = "http://127.0.0.1:8000/extract"

def test_invoice(file_path: str, use_langchain: bool = False):
    with open(file_path, "rb") as f:
        files = {"file": f}
        data = {"use_langchain": str(use_langchain).lower()}  # Form field
        response = requests.post(API_URL, files=files, data=data)
    
    if response.status_code == 200:
        print("✅ Extracted Data:", response.json())
    else:
        print("❌ Error:", response.status_code, response.text)

if __name__ == "__main__":
    test_invoice("Accounts A13291.pdf", use_langchain=False)
    # test_invoice("sample_invoices/invoice1.png", use_langchain=True)
