import streamlit as st
from PIL import Image
import io
import base64
import requests
from dotenv import load_dotenv
import os

# # Load environment variables from .env file
# load_dotenv()

# # Get your OpenAI API key from environment variables
# api_key = os.getenv('OPENAI_API_KEY')

# Load API key from Streamlit secrets
api_key = st.secrets["openai"]["api_key"]


def encode_image(image_bytes):
    """
    Encode image bytes to a base64 string.
    """
    return base64.b64encode(image_bytes).decode('utf-8')

def interpret_chart(image_bytes):
    """
    Send the chart image to OpenAI and get the interpretation.
    """
    base64_image = encode_image(image_bytes)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

def main():
    st.title("Chart Interpreter")

    uploaded_file = st.file_uploader("Upload a chart image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Chart.', use_column_width=True)

        # Convert the uploaded image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=image.format)
        img_bytes = img_byte_arr.getvalue()

        if st.button("Interpret Chart"):
            with st.spinner('Interpreting the chart...'):
                try:
                    interpretation = interpret_chart(img_bytes)
                    if 'choices' in interpretation:
                        message_content = interpretation['choices'][0]['message']['content']
                        st.markdown(
                            f"""
                            <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;">
                                <h4>Chart Interpretation:</h4>
                                <p>{message_content}</p>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.error("Failed to get interpretation.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
