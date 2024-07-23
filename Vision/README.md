# Google Vision

A web application that use Gemini model to generate responses based on text inputs and uploaded images.

## Features

- Text Input:
  - Enter a text prompt in the input field to guide the model in generating a response.
- Image Upload:
  - Upload an image in JPG, JPEG, or PNG format.
  - The application supports various image types and sizes.
- Combined Analysis:
  - The model can generate content based on both text and image inputs, providing comprehensive responses.
- Image Display:
  - Uploaded images are displayed within the application for easy reference.
- Google's Gemini Model:
  - Leverages the power of the gemini-1.5-flash model for advanced content generation capabilities.

## Requirements

- Python 3.7 or higher
- Streamlit
- python-dotenv
- google-generativeai

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/priyxnshuuu/Google-Gemini.git
   cd Google-Gemini

   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt

   ```

4. Create a .env file in the root directory and add your Google API key::
   ```bash
   GOOGLE_API_KEY=your_google_api_key
   ```

## Usage

1. Run the Streamlit application::

   ```bash
   streamlit run ' .\Vision\app.py'

   ```

2. Open your browser and go to `http://localhost:8501`.

3. Interact with the application:

- Enter a text prompt in the input field.
- Upload an image in JPG, JPEG, or PNG format.
- Click the "Tell me about the image" button to generate a response.

## Project Structure

```bash

Google-Gemini/
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── LICENSE             # License file
├── README.md           # Project documentation
├── requirements.txt    # Required Python packages
└── Vision/             # Directory containing the application
   ├── Vision.py        # Script containing the generate response functions
   ├── app.py           # Main Streamlit application
   └── README.md        # Detailed documentation for the application
```
