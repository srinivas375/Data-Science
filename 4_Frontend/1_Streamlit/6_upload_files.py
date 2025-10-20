import streamlit as st

st.title("Files uploading")

# uplading and displaying images
st.write("### Image Upload")
image = st.file_uploader("Upload an image here", type=["png", "jpg"])
if image is not None:
    st.image(image)

# audio upload and display
st.write("### Audio Upload")
audio = st.file_uploader("upload audio file here", type=['mp3'])
if audio:
    st.audio(audio)

# video upload and display
st.write("### Video Upload")
video = st.file_uploader("upload the video file here", type=["mp4"])
if video:
    st.video(video)

# pdf file upload
st.write("### Pdf Upload")
pdf = st.file_uploader("upload the pdf file", type=['pdf'])
if pdf:
    with open(pdf.name, 'wb') as f:
        f.write(pdf.getbuffer())
    
    with open(pdf.name, 'rb') as f:
        st.download_button(
            label="Download PDF",
            data=f,
            file_name=pdf.name
        )
# multiple pdfs upload
pdfs = st.file_uploader("Upload pdf files here", type=['pdf'], accept_multiple_files=True)
if pdfs:
    st.write("Uploaded files are")
    for pdf in pdfs:
        st.write(pdf.name)