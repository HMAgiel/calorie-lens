import streamlit as sl
from detection import claories_detection
sl.title("Uploaad file")
sl.markdown("---")

gambar = sl.file_uploader(
    label="Upload Gambar makanan",
    type=['png', 'jpg'],
    accept_multiple_files=False
)


# if sl.button("coba"):
#     print(gambar.name)

if sl.button("Detect"):
        pic, label= claories_detection(gambar)
        sl.image(pic, channels="BGR")
        sl.text("JumaH kalori yang terdeteksi adalah:")
        # print(label)
        sl.text(label)