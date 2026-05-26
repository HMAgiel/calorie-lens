import streamlit as sl
from detection import claories_detection
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
        col = sl.columns(len(pic), gap="small")
        for i in range(len(pic)):
            with col[i]:
                sl.image(pic[i], channels='BGR')
        # sl.image(pic, channels="BGR", use_column_width=True)
        # print(pic)
        sl.text("JumaH kalori yang terdeteksi adalah:")
        # print(label)
        sl.text(label)