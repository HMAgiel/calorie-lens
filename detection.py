from ultralytics import YOLO
import cv2
from PIL import Image
from io import BytesIO
import numpy as np
import tempfile

model = YOLO("/home/hasyim/projects-ai-engineer/Capston4/best_calories.pt")

def claories_detection(img):
    temp_pic = tempfile.NamedTemporaryFile(delete=False)
    temp_pic.write(img.read())
    picture_food=cv2.imread(temp_pic.name)
    result = model.predict([picture_food])
    
    boxes = result[0].boxes.xyxy.cpu().numpy()
    confidence = result[0].boxes.conf.cpu().numpy()
    labels = result[0].boxes.cls.cpu().numpy().astype(int)
    food = []
    
    for box_detect, conf_detetction, label_detection in zip(boxes, confidence, labels):
        if conf_detetction >= 0.2:
            x1, y1, x2, y2 = map(int, box_detect)
            name_label = model.names[label_detection]
            food.append(name_label)
            cv2.rectangle(picture_food, (x1,y1), (x2,y2), (0, 255, 0), 3) #pembuatan kotak deteksi
            cv2.putText(picture_food, 
                        f'{name_label} {conf_detetction:.2f}',
                        (x1, y1 - 3),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (255, 0, 0),
                        2)
            
    return picture_food, name_label