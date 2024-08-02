import streamlit as st
import plotly.graph_objects as go
import io
import base64
import requests
import json
from PIL import Image

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
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
    
    return response.json()

def save_plotly_figure(fig):
    """
    Save Plotly figure to a byte buffer.
    """
    img_bytes = fig.to_image(format="png")
    return img_bytes

def create_chart_1():
    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    return fig

def create_chart_2():
    fig = go.Figure(data=go.Scatter(y=[2, 1, 3]))
    return fig

def create_chart_3():
    fig = go.Figure(data=go.Pie(labels=['A', 'B', 'C'], values=[10, 20, 30]))
    return fig

def display_interpretation_card(interpretation):
    """
    Display the interpretation in a card format.
    """
    interpretation_text = json.dumps(interpretation, indent=2)
    message_content = interpretation['choices'][0]['message']['content']
    st.markdown(f"""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 10px 0;">
            <h4>Chart Interpretation</h4>
            <pre>{message_content}</pre>
        </div>
    """, unsafe_allow_html=True)

def main():
    st.title("Chart Interpretation Dashboard")

    charts = {
        "Chart 1": create_chart_1,
        "Chart 2": create_chart_2,
        "Chart 3": create_chart_3,
    }

    for chart_name, create_chart_func in charts.items():
        st.header(chart_name)

        # Create and display the chart
        fig = create_chart_func()
        st.plotly_chart(fig)

        # Convert the chart to bytes
        img_bytes = save_plotly_figure(fig)

        # Interpret chart button
        if st.button(f"Interpret {chart_name}"):
            with st.spinner(f'Interpreting {chart_name}...'):
                try:
                    interpretation = interpret_chart(img_bytes)
                    display_interpretation_card(interpretation)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
