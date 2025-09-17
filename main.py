import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

# Get the NASA API key
# Check if running in Streamlit Cloud
if os.environ.get("STREAMLIT_SERVER_RUNNING_IN_CLOUD") == "true":
    # Use Streamlit's secrets management
    API_KEY = st.secrets.get("NASA_API_KEY")
else:
    # Use local .env file for local development
    API_KEY = os.getenv("NASA_API_KEY")


# Check if the API key is available
if not API_KEY:
    st.error("NASA_API_KEY is not set. Please add it to your Streamlit secrets or your .env file.")
else:
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()

        if "url" in data and "explanation" in data:
            title = data.get("title", "NASA APOD")
            image_url = data["url"]
            explanation = data["explanation"]

            # Download the image
            image_filepath = "image.png"
            response_img = requests.get(image_url)
            response_img.raise_for_status()
            with open(image_filepath, "wb") as file:
                file.write(response_img.content)

            st.title(title)
            st.image(image_filepath, caption=explanation)
        else:
            st.error("Unexpected response from NASA API. 'url' or 'explanation' not found.")
            st.write(data)

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching data from the NASA API: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
