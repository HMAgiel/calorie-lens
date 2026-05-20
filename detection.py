from ultralytics import YOLO
from PIL import Image
from io import BytesIO

model = YOLO("/home/hasyim/projects-ai-engineer/Capston4/best_calories.pt")

def claories_detection(img):
    picture = Image.open(img)
    result = model.predict([picture])
    return result
    