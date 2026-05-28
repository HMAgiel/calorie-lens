from ultralytics import YOLO
import cv2
import tempfile
import os
import numpy as np
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
model = YOLO("model/best_calories.pt")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    
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


def video_detc(vid, pengganti):
    temp_vid = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_vid.write(vid.read())
    temp_vid.close()
    video = cv2.VideoCapture(temp_vid.name)
    confidence = 0
    labels = None
    foods = None
    while video.isOpened():
        berhasil, frame = video.read()
        if berhasil:
            results = model(frame)
            confs = results[0].boxes.conf.cpu().numpy()
            label = results[0].boxes.cls.cpu().numpy().astype(int)
            box = results[0].plot()
            
            if confs.size > 0 and np.max(confs) > confidence:
                index_label = np.argmax(confs)
                labels = label[int(index_label)]
                foods = model.names[labels]
                confidence = np.max(confs)
            
            frame_rgb = cv2.cvtColor(box, cv2.COLOR_BGR2RGB)

            pengganti.image(frame_rgb, channels="RGB", use_container_width=True)
        else:
            break
    
    video.release()
    os.unlink(temp_vid.name)
    return foods


def summary(makanan, waktu):
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="""
        Kamu adalah ahli gizi yang membantu user dalam hal pemenuhan kalori dari makanan-makanan user.
        Taruh jumlah kalori paling atas dari gabungan makanan user.
        klasifikasikan apakah itu untuk makan pagi, siang atau malam berdasarkan waktu.
        beri ringkasan singkat maksimal 3 paragraf.
        Ringkasan tidak perlu satu maknana 1 paragraf bisa digabungkan.
        Gunakan emoji agar terlihat kebih friendly
        """,
        input=f"""Berikut adalah makanan yang saya makan di jam {waktu} adalah: {makanan}""",
    )
    return response.output_text