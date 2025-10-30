from ultralytics import YOLO

# Load the yolo model
model = YOLO("yolo11n.pt")

# Detect objects and label them based on the confidence of each
def detect_objects(image_path: str):
    results = model(image_path)
    detections = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls.item())
            label = model.names[cls_id]
            conf = float(box.conf.item())
            detections.append({"label": label, "confidence": round(conf, 3)})
    return detections
