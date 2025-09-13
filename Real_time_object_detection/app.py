from flask import Flask, Response
import cv2
import threading
import time
from utils import run_detection


app = Flask(__name__)

# Initialize video capture (0 = default webcam)
VIDEO_SOURCE = 0
# cap = cv2.VideoCapture(VIDEO_SOURCE)
# cap = cv2.VideoCapture(VIDEO_SOURCE, cv2.CAP_DSHOW)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
cap = cv2.VideoCapture(0, cv2.CAP_VFW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)   # range depends on driver
cap.set(cv2.CAP_PROP_CONTRAST, 50)
cap.set(cv2.CAP_PROP_EXPOSURE, -4)   


# Thread-safe frame sharing
lock = threading.Lock()
output_frame = None




def detect_and_stream():
    global output_frame, lock
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Could not grab frame from camera")
            time.sleep(0.1)
            continue

        processed = run_detection(frame)

        with lock:
            output_frame = processed.copy()

        time.sleep(0.01)





def generate_mjpeg():
    global output_frame, lock
    while True:
        with lock:
            if output_frame is None:
                continue
                (flag, encodedImage) = cv2.imencode('.jpg', output_frame)
                if not flag:
                    continue
                    frame_bytes = encodedImage.tobytes()
                    yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')



@app.route('/')
def index():
    # Homepage with video + capture button
    return Response("""
        <h2>Real-Time Object Detection</h2>
        <img src='/video_feed'>
        <br><br>
        <form action="/capture" method="get">
            <button type="submit">📸 Capture Image</button>
        </form>
    """, mimetype='text/html')


@app.route('/capture')
def capture():
    global output_frame, lock
    with lock:
        if output_frame is None:
            return "No frame available", 500

        # Encode frame as JPEG
        ret, jpeg = cv2.imencode(".jpg", output_frame)
        if not ret:
            return "Failed to encode frame", 500

    # Generate unique filename with timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"capture_{timestamp}.jpg"

    # Return downloadable image with unique filename
    return Response(
        jpeg.tobytes(),
        mimetype="image/jpeg",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )


@app.route('/video_feed')
def video_feed():
    return Response(generate_mjpeg(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    t = threading.Thread(target=detect_and_stream, daemon=True)
    t.start()
    app.run(host='0.0.0.0', port=5000, debug=True)