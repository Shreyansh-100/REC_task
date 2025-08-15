#Run this script to perform inference on images using Streamlit,uploading images and entering queries through
#the web interface instead of CLI or harcode the image path and query

import streamlit as st
import tempfile
import os
import sys
import io
import time
import matplotlib.pyplot as plt
from inference import run_inference_streamlit

CHECKPOINT_PATH = "/home/shreyansh/mdetr/Checkpoint/refcoco_resnet101_checkpoint.pth"

st.set_page_config(page_title="MDETR based Referring Expression Model")
st.title("🔍 Referring Expression Detection")
st.write("")
st.markdown("Upload an image and type a natural language query to find objects.")

uploaded_file = st.file_uploader("📸 Upload Image", type=["jpg"])

query = st.text_input("🗣️ Enter Referring Expression", placeholder="e.g., the red backpack on the left")

if uploaded_file and query:
    st.image(uploaded_file, caption="🔼 Uploaded Image 🔼", use_column_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_img:
        tmp_img.write(uploaded_file.read())
        tmp_image_path = tmp_img.name

    st.write("🚀 Firing up....")
    time.sleep(2)
    st.write("")
    st.write("🧠 Running inference...")
  
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()

    try:
        run_inference_streamlit(tmp_image_path, query, CHECKPOINT_PATH)
        st.pyplot(plt.gcf())
        plt.clf()
        st.success("✅ Inference completed successfully!")
    except Exception as e:
        st.error(f"❌ Inference failed: {e}")
    finally:
        sys.stdout = old_stdout
        os.remove(tmp_image_path)
