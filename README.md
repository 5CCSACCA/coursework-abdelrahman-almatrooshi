# Cloud Computing Coursework – Phase 1
Abdelrahman Almatrooshi
Repo: https://github.com/5CCSACCA/coursework-abdelrahman-almatrooshi
---

# 1. Project Summary
This project converts an AI system into a SaaS application using FastAPI, Docker, and GitFlow.
My project is a Smart Security Camera, which analyzes uploaded images to detect objects/people such as people and cars and return a sentence saying what and how many objects/people it found.

It will use:
- YOLO11n for object detection
- BitNet for generating short scene summaries
---

# 2. Current Progress
- Created repository and linked to github
- Virtual environment set up
- Installed base dependencies:
  - fastapi
  - uvicorn[standard]
  - python-multipart
  - pydantic
- Project structure created
- FastAPI works and I can see this: {"message": "API is working"}
- Implemented and tested yolo and bitnet services
- Tested /analyze-image endpoint
