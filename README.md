# NASA Image Viewer

This is a Streamlit web application that displays NASA's "Picture of the Day" (APOD). It fetches the latest image and its explanation from the NASA API and presents it in a user-friendly interface.

## Features

*   Fetches and displays the latest "Picture of the Day" from NASA's APOD API.
*   Shows the image title and a detailed explanation.
*   Simple and intuitive user interface built with Streamlit.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your system. This project uses the following Python libraries:

*   `streamlit`
*   `requests`
*   `python-dotenv`

You will also need a NASA API key. You can get one for free from the [NASA API website](https://api.nasa.gov/).

### Installation

1.  Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/nasa-image-viewer.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd nasa-image-viewer
    ```

3.  Install the required libraries. It is recommended to use a virtual environment:

    ```bash
    pip install -r requirements.txt
    ```

    You can create a `requirements.txt` file with the following content:

    ```
    streamlit
    requests
    python-dotenv
    ```

4.  Create a `.env` file in the root of the project and add your NASA API key:

    ```
    NASA_API_KEY=your_api_key
    ```

### Running the App

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run main.py
```

## Usage

Once the app is running, open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`). The app will display the latest NASA "Picture of the Day" along with its title and explanation.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
