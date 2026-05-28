from ultralytics import YOLO
import albumentations as A
import logging
import time
from datetime import timedelta

model = YOLO('yolo26n.pt')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("training_yolo.log"), # Menyimpan ke file
        logging.StreamHandler()                   # Menampilkan di output Notebook
    ]
)

# 2. Catat Waktu Mulai
logging.info("=========================================")
logging.info("Memulai proses training YOLO...")
start_time = time.time()

from datetime import timedelta
# 2. Catat Waktu Mulai
logging.info("=========================================")
logging.info("Memulai proses training YOLO...")
start_time = time.time()

try:
    # 3. Proses Training
    results = model.train(
        data='/kaggle/input/datasets/hasyimagiel/data-kalori', 
        epochs=300,
        device=[0,1],            
        batch=22,
        lr0=0.001,
        lrf=0.0001,
        warmup_epochs=10,
        imgsz=640,
        hsv_h=0.4,               
        hsv_s=0.6,
        hsv_v=0.5,
        bgr=0.0,                 
        mosaic=0.7,
        erasing=0.6,
        auto_augment='randaugment',
        exist_ok=True,
        patience=50,
        weight_decay=0.001,
        dropout=0.1,
        save_period=50,           
        val=True,                
        verbose=True,            
        flipud=0.0,              
    )
    logging.info("Training selesai dengan SUKSES!")

except Exception as e:
    # Jika terjadi error (misal OOM), akan tercatat di log
    logging.error(f"Training GAGAL karena error: {e}")

finally:
    # 4. Hitung dan Catat Total Waktu (Berhasil atau Gagal tetap dihitung)
    end_time = time.time()
    duration_seconds = end_time - start_time
    formatted_duration = str(timedelta(seconds=int(duration_seconds)))
    
    logging.info(f"Total waktu training (Jam:Menit:Detik) = {formatted_duration}")
    logging.info("=========================================\n")