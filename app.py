import streamlit as sl
from detection import claories_detection, summary, video_detc
sl.title("Uploaad file")
sl.markdown("---")


gambar = sl.file_uploader(
    label="Upload Gambar makanan",
    type=['png', 'jpg', 'webp'],
    accept_multiple_files=True
)

vi =  sl.file_uploader(
    "Upload Video (only one video)", 
    type='mp4', 
    accept_multiple_files=False)

        
if sl.button("Detect"):
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
    with sl.spinner("Summarize results...", show_time=True):
        summ = summary(food)
    sl.markdown(summ)