import streamlit as sl
from datetime import datetime, timezone, timedelta
from detection import claories_detection, video_detc, summary
sl.title("Uploaad file")
sl.markdown("---")


gambar = sl.file_uploader(
    label="Upload Food Image",
    type=['png', 'jpg', 'webp'],
    accept_multiple_files=True
)

sl.markdown("---")
vi =  sl.file_uploader(
    "Upload Food Video (only one video)", 
    type='mp4', 
    accept_multiple_files=False)
      
if sl.button("Detect the food calories"):
    print(gambar)
    print(vi)
    if gambar != []:
        with sl.spinner("Picture detetction progress...", show_time=True):
            pic, label_pic = claories_detection(gambar)
            col = sl.columns(len(pic), gap="small")
            for i in range(len(pic)):
                with col[i]:
                    sl.image(pic[i], channels='BGR')
            sl.success("success detecting picture")
    else:
        label_pic = " "
    
    if vi is not None:
        placeholder = sl.empty()
        with sl.spinner("Video Detetection in progress....", show_time=True):
            label_vid = video_detc(vi, placeholder)
            sl.success("Success detecting video")
            
    else:
        label_vid = " "
    
    food = label_pic + label_vid
    time_zone = timezone(timedelta(hours=7))
    time = datetime.now(time_zone)
    waktu = time.strftime("%H:%M")
    
    with sl.spinner("Summarize results...", show_time=True):
        summ = summary(food, waktu)
    sl.text(f"Time: {waktu} WIB")
    sl.markdown(summ)