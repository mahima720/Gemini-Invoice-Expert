from dotenv import load_dotenv

load_dotenv() #load all the environment variables from .env

import streamlit as st
import os
from PIL import Image
from google import genai

# Initialize Client (New SDK automatically finds GOOGLE_API_KEY in .env)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(system_prompt, image_obj, user_question):
    model_id = "gemini-2.5-flash" 
    response = client.models.generate_content(
        model=model_id,
        contents=[system_prompt, image_obj, user_question]
    )
    return response.text

## --- Streamlit UI ---
st.set_page_config(page_title="Gemini Invoice Expert")
st.header("Invoice Information Extractor")

user_query = st.text_input("Ask a question about the invoice: ", key="input")
uploaded_file = st.file_uploader("Upload invoice image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open image with PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", width=750)

submit = st.button("Extract Info")

# System Prompt
system_behavior_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image.
               """

if submit:
    if uploaded_file is not None:
        with st.spinner("Analyzing invoice..."):
            # We pass the PIL 'image' object directly to our function
            response_text = get_gemini_response(system_behavior_prompt, image, user_query)
            
        st.subheader("Results:")
        st.write(response_text)
    else:
        st.error("Please upload an invoice image first.")