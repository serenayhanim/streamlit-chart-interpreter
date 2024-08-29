# Streamlit Chart Interpreter

## Overview

**Streamlit Chart Interpreter** is a web application built using Streamlit that allows users to generate different types of charts and get detailed interpretations of those charts by leveraging OpenAI's powerful language models. This tool is particularly useful for data analysts and stakeholders who want to quickly understand the insights presented by various charts.

## Features

- **Chart Generation**: Users can generate different types of charts (Bar, Scatter, Pie) using Plotly.
- **Chart Interpretation**: The app sends the generated chart to OpenAI's API, which returns an interpretation of the chart, explaining what it represents.
- **Interactive Dashboard**: The application provides an easy-to-use interface where users can select and generate charts, and then get interpretations with a single click.

## Project Structure

```markdown
streamlit-chart-interpreter/
├── app.py                    # Main Streamlit app script
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not included in version control)
├── .streamlit/
│   └── secrets.toml          # Streamlit secrets management for API keys
└── README.md                 # Project overview and instructions
```

## Technology Stack

This project utilizes the following technologies:

- **Python 3.7+**: The programming language used for backend logic and data processing.
- **Streamlit**: A Python library used for creating the interactive web application.
- **Plotly**: A graphing library used for creating the charts displayed in the application.
- **OpenAI API**: The core API used to interpret the generated charts.
- **PIL (Python Imaging Library)**: Used to handle image processing when converting charts to a format suitable for API requests.
- **Requests**: A Python library used for making HTTP requests to the OpenAI API.
- **dotenv**: Used for managing environment variables, such as the OpenAI API key.

## How Image Interpretation Works

1. **Chart Creation**: The user selects and generates a chart using Plotly, displayed in the Streamlit interface.
2. **Image Processing**: The generated chart is converted into an image format using Plotly's image exporting capabilities.
3. **Sending to OpenAI API**: The image is encoded and sent to the OpenAI API with a prompt asking for an interpretation of the chart.
4. **AI Analysis**: OpenAI’s model analyzes the chart, interpreting the visual data, and provides a human-readable summary of what the chart represents.
5. **Displaying Results**: The interpretation is displayed on the dashboard in a formatted card, giving the user insights into the chart's content.

## Running Locally

To run the Streamlit Chart Interpreter app locally, follow these steps:

### Prerequisites

Ensure that you have the following installed on your machine:

- **Python 3.7+**
- **pip** (Python package installer)

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/streamlit-chart-interpreter.git
cd streamlit-chart-interpreter
```


### Create a Virtual Environment
It's recommended to create a virtual environment to manage the dependencies for this project. You can create and activate a virtual environment using the following commands:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies
Once the virtual environment is activated, install the necessary dependencies:

```bash
pip install -r requirements.txt
```
### Set Up OpenAI API Key

To use the OpenAI API, you need to set up your API key. You can do this by:

Creating a .env file in the root directory of your project.

Adding your API key to the .env file:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```
Alternatively, you can use Streamlit's secrets management by creating a secrets.toml file in the .streamlit/ directory and adding your API key:

```bash
[openai]
api_key = "your_openai_api_key_here"
```

### Run the Application
With everything set up, you can now run the Streamlit application:

```bash
streamlit run app.py
```

This command will start a local web server, and the app will open in your default web browser at http://localhost:8501.

### Deployment on Streamlit Cloud
I have also deployed this app on Streamlit Cloud, making it easy to access without running it locally. You can visit the deployed app using the following link:

[Streamlit Chart Interpreter](https://p3cprzdswldemunxtrnduz.streamlit.app/)