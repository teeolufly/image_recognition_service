from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

@app.get("/")
def home():
    return {"message": "Image recognition service task"}

@app.get("/health") # for healthcheck purpose
def health_check():
    return {"status": "healthy"}

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):

    
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))  #Convert bytes to PIL img

    #Perform the detection
    results = model(image)

    #Detection found
    detections_found = []
    for result in results:
        for box in result.boxes:
            detections_found.append({
                "class": model.names[int(box.cls)],  
                "confidence": float(box.conf),      
                "bbox": box.xyxy.tolist()          
            })

    return {"detections": detections_found}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)