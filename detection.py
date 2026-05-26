from ultralytics import YOLO
import cv2
import tempfile

model = YOLO("/home/hasyim/projects-ai-engineer/Capston4/best_calories.pt")


def claories_detection(img):
    food = []
    food_det = []
    for imgs in img:
        #Read image and make temporary file for open cv input
        temp_pic = tempfile.NamedTemporaryFile(delete=False)
        temp_pic.write(imgs.read())
        picture_food=cv2.imread(temp_pic.name)
        result = model.predict([picture_food])
        
        #create the bounding box and label image
        boxes = result[0].boxes.xyxy.cpu().numpy()
        confidence = result[0].boxes.conf.cpu().numpy()
        labels = result[0].boxes.cls.cpu().numpy().astype(int)
        
        #box and label maker
        for box_detect, conf_detetction, label_detection in zip(boxes, confidence, labels):
            if conf_detetction >= 0.2:
                x1, y1, x2, y2 = map(int, box_detect)
                name_label = model.names[label_detection]
                food.append(name_label)
                cv2.rectangle(picture_food, (x1,y1), (x2,y2), (0, 255, 0), 3) #make bounding box
                cv2.putText(picture_food, 
                            f'{name_label} {conf_detetction:.2f}',
                            (x1, y1 - 3),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.9,
                            (255, 0, 0),
                            2)
        food_det.append(picture_food)
    return food_det, ", ".join(food)

