import cv2
import time
from ultralytics import YOLO


MODEL_NAME = 'yolov8n.pt' # lightweight and fast model
model = YOLO(MODEL_NAME)


def run_detection(frame):
    """
    Run YOLOv8 inference on a frame and return the frame with detections drawn.
    """
    results = model(frame, imgsz=640)[0]


    if results.boxes is not None and len(results.boxes) > 0:
        boxes = results.boxes.xyxy.cpu().numpy()
        scores = results.boxes.conf.cpu().numpy()
        cls = results.boxes.cls.cpu().numpy().astype(int)
        names = model.names


        for (x1, y1, x2, y2), score, c in zip(boxes, scores, cls):
            label = f"{names.get(c, str(c))}: {score:.2f}" if isinstance(names, dict) else f"{names[c]}: {score:.2f}"
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
            cv2.rectangle(frame, (x1, y1 - t_size[1] - 6), (x1 + t_size[0] + 6, y1), (0, 255, 0), -1)
            cv2.putText(frame, label, (x1 + 3, y1 - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)


    return frame