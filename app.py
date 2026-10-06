import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import requests
from pydantic import BaseModel
import os

# Load environment variables
load_dotenv()

# Pydantic model
class UserRequest(BaseModel):
    prompt: str

# Streamlit page
st.set_page_config(
    page_title="Generative Multimodal AI",
    page_icon="🤖"
)

st.title("🤖 Generative Multimodal AI")
st.write("Upload an image and enter a prompt.")

# Image upload
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

# Text prompt
prompt = st.text_input(
    "Enter your prompt",
    placeholder="Describe this image..."
)

# Generate button
if st.button("Generate"):

    if uploaded_file is None:
        st.error("Please upload an image.")

    elif not prompt.strip():
        st.error("Please enter a prompt.")

    else:
        # Open image
        image = Image.open(uploaded_file)

        # Display image
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Validate prompt using Pydantic
        user_request = UserRequest(prompt=prompt)

        st.success("Image and prompt received successfully!")

        st.subheader("Your Prompt")
        st.write(user_request.prompt)
        st.subheader("AI Response")

        # Demo response
        st.write(
            "The multimodal AI received your image and text prompt. "
            "You can connect an AI vision API here to generate the actual response."
        )