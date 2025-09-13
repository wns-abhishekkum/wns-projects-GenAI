# Real-Time Object Detection — Flask + YOLOv8

This project implements a **Flask web application** for **real-time object detection** using **YOLOv8** from Ultralytics. The app streams webcam frames, performs detection, draws bounding boxes and labels, and serves the video to a web browser. It also supports **capturing frames** as images directly from the browser.

---

## 🚀 Features
- Real-time object detection with YOLOv8 (`yolov8n.pt` by default)
- Flask-based web server with MJPEG video stream (`/video_feed`)
- Homepage shows live video feed + 📸 Capture button
- Capture and download the latest processed frame with bounding boxes
- Works on CPU or GPU (if PyTorch with CUDA is available)
- Modular design with `utils.py` for detection logic

---

## 📂 Project Structure
```
flask_realtime_object_detection/
├─ app.py          # Flask server and routes
├─ utils.py        # Detection logic (YOLO inference + drawing boxes)
├─ requirements.txt
└─ README.md       # Documentation
```

---

## 🔧 Installation

### 1. Clone the repo (or copy files)
```bash
git clone https://github.com/your-username/flask-realtime-object-detection.git
cd flask-realtime-object-detection
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
# Activate it
venv\Scripts\activate     # Windows
source venv/bin/activate   # Linux / macOS
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

⚠️ Note: `ultralytics` will install PyTorch automatically. For GPU acceleration, install PyTorch separately with CUDA support from [pytorch.org](https://pytorch.org/get-started/locally/).

---

## ▶️ Usage

### 1. Run the Flask app
```bash
python app.py
```

If successful, Flask will start on:
```
http://127.0.0.1:5000
```

### 2. Open in browser
- Go to [http://localhost:5000](http://localhost:5000)
- You’ll see:
  - Live video feed
  - **📸 Capture Image** button

### 3. Capture frames
- Click the **📸 Capture Image** button
- The latest processed frame will be downloaded as:
  ```
  capture_YYYYMMDD_HHMMSS.jpg
  ```

---

## ⚙️ Configuration

- Change camera source in `app.py`:
  ```python
  VIDEO_SOURCE = 0  # default webcam
  cap = cv2.VideoCapture(VIDEO_SOURCE, cv2.CAP_DSHOW)
  ```
  Try `1`, `2`, etc. if you have multiple cameras.

- Force resolution:
  ```python
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  ```

- Use a different YOLO model (e.g., `yolov8s.pt` for higher accuracy):
  ```python
  MODEL_NAME = 'yolov8s.pt'
  ```

---

## 🛠 Troubleshooting

- **Black frames / errors like MSMF can’t grab frame** → Try using another backend:
  ```python
  cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  # or
  cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
  ```

- **No frame available** → Ensure the detection thread is started in `app.py`:
  ```python
  if __name__ == '__main__':
      t = threading.Thread(target=detect_and_stream, daemon=True)
      t.start()
      app.run(host='0.0.0.0', port=5000, debug=True)
  ```

- **GPU not used** → Install PyTorch with CUDA support separately.

---

## 📸 Example Output
When running, the app will:
- Detect objects in the webcam feed
- Draw bounding boxes + labels
- Allow you to capture and download frames

Example:
```
0: 480x640 1 person, 1 chair, 133.4ms
Speed: 3.2ms preprocess, 133.4ms inference, 2.6ms postprocess
```

---

## 📌 Future Improvements
- Add support for video file uploads
- Save captured frames to a server folder instead of only downloads
- Add configurable confidence threshold & detection toggle in the UI
- Dockerize the app for easy deployment

---

## 📜 License
This project is open-source. Use freely for learning or prototyping. For production deployments, check YOLOv8 license terms.

