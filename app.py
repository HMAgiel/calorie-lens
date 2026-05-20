import streamlit as sl
from detection import claories_detection
sl.title("Uploaad file")
sl.markdown("---")

gambar = sl.file_uploader(
    label="Upload Gambar makanan",
    type=['png', 'jpg'],
    accept_multiple_files=False
)

if sl.button("Detect"):
        detect = claories_detection(gambar)
        index = detect[0].boxes.cls
        sl.image(detect[0].plot(), channels="BGR")
        sl.text("JumaH kalori yang terdeteksi adalah:")
        sl.text(detect[0].names[int(index)])