import streamlit as sl
# from detection import claories_detection, summary, video_detc
from detection import video_detc
sl.title("Uploaad file")
sl.markdown("---")


vi =  sl.file_uploader("Upload Video", type='mp4', accept_multiple_files=False)
if sl.button("Upload Video (Only one)"):
    placeholder = sl.empty()
    with sl.spinner("Wait in progress....", show_time=True):
        hasil = video_detc(vi, placeholder)
        sl.success("Berhasil deteksi")
        sl.text(hasil)
        

# gambar = sl.file_uploader(
#     label="Upload Gambar makanan",
#     type=['png', 'jpg'],
#     accept_multiple_files=True
# )

# # if sl.button("coba"):
# #      print(gambar[0].name)

# if sl.button("Detect"):
#         pic, label= claories_detection(gambar)
#         summ = summary(label)
#         col = sl.columns(len(pic), gap="small")
#         for i in range(len(pic)):
#             with col[i]:
#                 sl.image(pic[i], channels='BGR')
#         sl.text("Summary")
#         sl.text(summ)