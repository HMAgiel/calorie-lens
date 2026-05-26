import streamlit as sl
from detection import claories_detection, summary
sl.title("Uploaad file")
sl.markdown("---")

gambar = sl.file_uploader(
    label="Upload Gambar makanan",
    type=['png', 'jpg'],
    accept_multiple_files=True
)

# if sl.button("coba"):
#      print(gambar[0].name)

if sl.button("Detect"):
        pic, label= claories_detection(gambar)
        summ = summary(label)
        col = sl.columns(len(pic), gap="small")
        for i in range(len(pic)):
            with col[i]:
                sl.image(pic[i], channels='BGR')
        sl.text("Summary")
        sl.text(summ)