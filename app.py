import streamlit as st
import os
from google import genai
from google.genai import types
from PIL import Image
import io
import base64 # Needed for decoding inline_data

st.set_page_config(page_title="🌟Envision Your Future Profession with AI! 🚀", page_icon="🥳")

# --- Configuration ---
# Google GenAI Client Setup
# NOTE: It is best practice to store the API key in environment variables 
# or Streamlit Secrets, NOT directly in the code.
# The key provided is a placeholder and should be replaced with a valid key.
# api_key = os.environ.get("GEMINI_API_KEY") 
api_key = "AIzaSyAHAcIkepcaNo9BGh1RMU7AohVkOsWgdHQ" # Placeholder
client = genai.Client(api_key=api_key)

# 🛑 CRITICAL FIX: Use a stable and supported model ID.
# 'gemini-2.0-flash-exp' is deprecated/unsupported.
# Using 'gemini-2.5-flash' which is the recommended model for multimodal tasks.
MODEL_ID = "gemini-2.5-flash" 

st.title("Future Profession Visualization App")
st.subheader("Visualize your future career with AI-powered transformation!")

# --- Input Section ---
uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])
profession = st.selectbox("Select your future profession",[
    "Doctor", "Engineer", "Teacher", "Pilot", "Scientist", 
    "Lawyer", "Artist", "Athlete", "Chef", "Entrepreneur",
    "IAS Officer", "IPS Officer", "Software Developer", "Banker",
    "Farmer", "Ayurvedic Doctor", "Yoga Instructor", "Classical Dancer",
    "Folk Musician", "Handloom Weaver", "Social Worker", "Army Officer",
    "Cricketer", "Actor", "Politician", "Journalist", "Chartered Accountant"
])
description = st.text_area("Describe your dream job in detail, including your role, responsibilities, and unique skills.")

# --- Functions ---

def display_response(response):
    """
    Displays the text content and decoded image from the Gemini API response.
    """
    if not response.candidates:
        st.error("The API returned an empty response. This might be due to safety filters or a server error.")
        return

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            # Display text (roadmap)
            st.markdown(part.text)
        elif part.inline_data is not None:
            # Handle image data
            try:
                # The data is base64 encoded by the API when returned as inline_data
                decoded_data = base64.b64decode(part.inline_data.data)
                image = Image.open(io.BytesIO(decoded_data))
                
                # Use 'use_container_width=True' instead of deprecated 'use_column_width'
                st.image(image, caption="Generated Future Profession Image", use_container_width=True)
            except Exception as e:
                st.error(f"Error processing image data: {e}")
                st.warning("The model may have tried to return image data in an unexpected format.")


# --- Main Application Logic ---
if st.button("Generate Image"):
    if uploaded_file is None:
        st.warning("Please upload a photo before generating.")
    else:
        # Load the uploaded image
        image = Image.open(uploaded_file)
        
        # FIX Streamlit deprecation: use_container_width=True
        st.image(image, caption="Uploaded Photo", use_container_width=True)

        with st.spinner("Generating your future profession visualization and roadmap..."):
            try:
                # AI Image Generation with Roadmap
                # The prompt is complex and should ideally use a multi-modal model like gemini-2.5-flash
                # Note: The success of face preservation depends heavily on the model's current capability 
                # and adherence to safety guidelines.
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=[
                        image, # Place the image first for best interpretation
                        f"""Regenerate this image using the **face from the uploaded image**, create a realistic and highly similar image of a **{profession}**. Ensure the face closely and accurately matches the uploaded image, preserving unique facial characteristics.
                        This person is passionate about {description}. Depict them in a professional environment with appropriate attire, tools, and realistic surroundings.
                        Additionally, provide a short, crisp educational **roadmap for an Indian student** to become a {profession} in both **English and Odia**:
                        
                        **English Roadmap:**
                        * **Foundation Stage:** Key subjects and skills to focus on in school.
                        * **Higher Education:** Essential degrees, certifications, and specialized courses.
                        * **Competitive Exams:** Notable entrance exams (e.g., JEE, NEET, UPSC, etc.).
                        * **Career Path:** Entry-level roles, growth opportunities, and long-term success.
                        
                        **ଓଡ଼ିଆରେ ରୋଡମ୍ୟାପ୍ (Odia Roadmap):**
                        
                        Ensure the roadmap is formatted with bullet points, concise, and easy to understand."""
                    ],
                    config=types.GenerateContentConfig(
                        # This config tells the model we expect both Text and Image back
                        response_mime_types=["text/markdown", "image/png"]
                    )
                )

                display_response(response)

            except genai.errors.ResourceExhaustedError:
                st.error("Quota Exceeded (Error 429): You've run out of requests or tokens for your current quota. Please try again in a few minutes or check your usage dashboard.")
            except genai.errors.NotFoundError:
                 st.error(f"Model Not Found (Error 404): The model ID '{MODEL_ID}' is incorrect or deprecated. Please verify the model name.")
            except genai.errors.APIError as e:
                # Catch other API errors
                st.error(f"An API Error occurred: {e}. Check your API key and network connection.")
            except Exception as e:
                st.exception(f"An unexpected error occurred: {e}")
