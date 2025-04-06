


import streamlit as st
import requests
import mimetypes
import base64
import os
from google import genai
from google.genai import types
from PIL import Image
import io
import pathlib

st.set_page_config(page_title="🌟 Quest Alliance: Envision Your Future Profession with AI! 🚀", page_icon="🟢")

# Google GenAI Client Setup
api_key = "AIzaSyAHAcIkepcaNo9BGh1RMU7AohVkOsWgdHQ"
client = genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.0-flash-exp"

st.title("Quest Alliance Future Profession Visualization App")
st.subheader("Visualize your future career with AI-powered transformation!")

# Input Section
uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])
profession = st.selectbox("Select your future profession", ["Doctor", "Engineer", "Teacher", "Pilot", "Scientist", "Lawyer", "Artist", "Athlete", "Chef", "Entrepreneur"])
# age = st.slider("Select your age", min_value=10, max_value=60, value=25)
description = st.text_area("Describe your dream job in detail, including your role, responsibilities, and unique skills.")

# Function to Display and Save Response
# def display_response(response):
#     for part in response.candidates[0].content.parts:
#         if part.text is not None:
#             st.markdown(part.text)
#         elif part.inline_data is not None:
#             mime = part.inline_data.mime_type
#             data = part.inline_data.data
#             # Decode base64 data and display image
#             decoded_data = base64.b64decode(data)
#             image = Image.open(io.BytesIO(decoded_data))
#             st.image(image, caption="Generated Image")
import streamlit as st
from PIL import Image

# Function to Display and Save Response
# Function to Display and Save Response
def display_response(response):
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            st.markdown(part.text)
        elif part.inline_data is not None:
            mime = part.inline_data.mime_type
            image_data = part.inline_data.data
            
            # Correctly handle the image data
            image_stream = io.BytesIO(image_data)  # Wrap in BytesIO
            image = Image.open(image_stream)       # Open image from stream
            
            st.image(image, caption="Generated Image", use_container_width=True)



# Generate Image
if st.button("Generate Image"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Photo", use_column_width=True)

        # AI Image Generation with Roadmap
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                 f"""Regenerate this image using the facial features from the uploaded image, create a realistic and highly similar image of a {profession}. Ensure the face closely matches the uploaded image, preserving unique facial characteristics.
                    This person is passionate about {description}. Depict them in a professional environment with appropriate attire, tools, and realistic surroundings
                    Additionally, provide a short, crisp educational roadmap for an Indian student to become a {profession} in both English and Odia:
                    Foundation Stage: Key subjects and skills to focus on in school.
                    Higher Education: Essential degrees, certifications, and specialized courses.
                    Competitive Exams: Notable entrance exams (e.g., JEE, NEET).
                    Career Path: Entry-level roles, growth opportunities, and long-term success.
                    Ensure the roadmap is formatted with bullet points, concise, and easy to understand.""",
                image
            ],
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image']
            )
        )

        display_response(response)
    else:
        st.warning("Please upload a photo before generating.")



# streamlit run "C:\Users\priya\Desktop\profession app\app.py"

# import streamlit as st
# import requests
# import mimetypes
# import base64
# import os
# from google import genai
# from google.genai import types
# from PIL import Image
# import io
# import pathlib

# st.set_page_config(page_title="🌟 Quest Alliance: Envision Your Future Profession with AI! 🚀", page_icon="🟢")

# # Google GenAI Client Setup
# api_key = "AIzaSyAHAcIkepcaNo9BGh1RMU7AohVkOsWgdHQ"
# client = genai.Client(api_key=api_key)
# MODEL_ID = "gemini-2.0-flash-exp"

# st.title("Quest Alliance Future Profession Visualization App")
# st.subheader("Visualize your future career with AI-powered transformation!")

# # Input Section
# uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])
# profession = st.selectbox("Select your future profession", ["Doctor", "Engineer", "Teacher", "Pilot", "Scientist", "Lawyer", "Artist", "Athlete", "Chef", "Entrepreneur"])
# age = st.slider("Select your age", min_value=10, max_value=60, value=25)
# description = st.text_area("Describe your dream job in detail, including your role, responsibilities, and unique skills.")

# # Function to Display and Save Response
# def display_response(response):
#     for part in response.candidates[0].content.parts:
#         if part.text is not None:
#             st.markdown(part.text)
#         elif part.inline_data is not None:
#             mime = part.inline_data.mime_type
#             data = part.inline_data.data
#             # Decode base64 data and display image
#             decoded_data = base64.b64decode(data)
#             image = Image.open(io.BytesIO(decoded_data))
#             st.image(image, caption="Generated Image")

# # Generate Image
# if st.button("Generate Image"):
#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Photo", use_container_width=True)

#         # AI Image Generation with Roadmap
#         response = client.models.generate_content(
#             model=MODEL_ID,
#             contents=[
#                 f"Create a realistic image of a {profession} at the age of {age} using the existing face of image. This person is passionate about {description}. Include details of the profession’s environment, attire, and tools used by professionals in this field. Also, provide a short crispy educational roadmap including key milestones and exams an Indian student needs to face to become a {profession}.and make this detail short crispy and try to add bulelt points",
#                 image
#             ],
#             config=types.GenerateContentConfig(
#                 response_modalities=['Text', 'Image']
#             )
#         )

#         display_response(response)
#     else:
#         st.warning("Please upload a photo before generating.")

# import streamlit as st
# import requests
# import mimetypes
# import base64
# import os
# from google import genai
# from google.genai import types
# from PIL import Image
# import io
# import pathlib

# st.set_page_config(page_title="Quest Alliance Future Profession Visualization App", page_icon="🟢")

# # Google GenAI Client Setup
# # client = genai.Client(api_key="AIzaSyAHAcIkepcaNo9BGh1RMU7AohVkOsWgdHQ")
# api_key = "AIzaSyAHAcIkepcaNo9BGh1RMU7AohVkOsWgdHQ"
# client = genai.Client(api_key=api_key)
# MODEL_ID = "gemini-2.0-flash-exp"

# st.title("Quest Alliance Future Profession Visualization App")
# st.subheader("Visualize your future career with AI-powered transformation!")

# # Input Section
# uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])
# profession = st.selectbox("Select your future profession", ["Doctor", "Engineer", "Teacher", "Pilot", "Scientist"])
# age = st.slider("Select your age", min_value=10, max_value=60, value=25)
# description = st.text_area("Describe your dream job in detail, including your role, responsibilities, and unique skills.")

# # Function to Display and Save Response
# def display_response(response):
#     for part in response.candidates[0].content.parts:
#         if part.text is not None:
#             st.markdown(part.text)
#         elif part.inline_data is not None:
#             mime = part.inline_data.mime_type
#             data = part.inline_data.data
#             # Decode base64 data and display image
#             decoded_data = base64.b64decode(data)
#             image = Image.open(io.BytesIO(decoded_data))
#             st.image(image, caption="Generated Image")

# def save_image(response, path):
#     for part in response.candidates[0].content.parts:
#         if part.inline_data is not None:
#             data = part.inline_data.data
#             decoded_data = base64.b64decode(data)
#             pathlib.Path(path).write_bytes(decoded_data)

# # Generate Image
# if st.button("Generate Image"):
#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Photo", use_column_width=True)

#         # AI Image Generation
#         response = client.models.generate_content(
#             model=MODEL_ID,
#             contents=[
#                 f"Create a realistic image of a {profession} at the age of {age}. This person is passionate about {description}.",
#                 image
#             ],
#             config=types.GenerateContentConfig(
#                 response_modalities=['Text', 'Image']
#             )
#         )

#         display_response(response)
#         save_image(response, f"{profession.lower()}.png")
#     else:
#         st.warning("Please upload a photo before generating.")

