# Review: this module implements a FastAPI application that provides an endpoint for analyzing images. It works by accepting an uploaded image file, saving it temporarily, and then using two services: one for object detection (YOLO) and another for scene summarization (BitNet). The results from both services are returned in the response. Please, use proper documentation standards for the code. Also, you will need to add more endpoints later.
from fastapi import FastAPI, UploadFile, File
import tempfile, shutil, os
from app.services.yolo_service import detect_objects
from app.services.bitnet_service import summarize_scene

app = FastAPI(title="Smart Security Camera SaaS")

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    # Keep the file extension so I don't get an error 
    suffix = os.path.splitext(file.filename)[1]

    # Create a temp file with the same extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    # Run yolo detection
    detections = detect_objects(tmp_path)

    # Run bitnet to get the summary
    summary = summarize_scene(detections)

    return {"detections": detections, "summary": summary}
