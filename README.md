# Google Gemini Projects

This Streamlit application allows users to interact with two projects:

1. **Youtube Summarizer**
2. **Chat with PDF using Google Gemini models**


## Features

- **Youtube Summarizer:**
  - Enter a YouTube video URL to summarize its transcript.
  - Display the video thumbnail and provide a detailed summary using Google Gemini.

- **Chat with PDF:**
  - Upload PDF files to extract text.
  - Process uploaded PDFs to generate embeddings using Google Generative AI.
  - Ask questions related to the PDF content and receive answers using a conversational AI model.

## Requirements

- Python 3.7 or higher
- pip (Python package installer)
- Streamlit
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/priyxnshuuu/Google-Gemini.git
   cd Google-Gemini

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Create a .env file in the root directory and add your Google API key::
   ```bash
   GOOGLE_API_KEY=your_google_api_key

## Running the Application

1. Run the Streamlit application::
   ```bash
   streamlit run 'app.py'

2. Open your browser and go to `http://localhost:8501`.

3. The application will open in your default web browser. Use the sidebar to navigate between "Youtube Summarizer" and "Chat with PDF".

## Usage

### Youtube Summarizer

1. **Enter a valid YouTube video URL:**
   - Navigate to the "Youtube Summarizer" section.
   - Enter a valid YouTube video URL in the provided text input field.

2. **Generate a summary:**
   - After entering the URL, click on the "Summarize" button.
   - The application will fetch the video's transcript and generate a summary using Google Gemini.

### Chat with PDF

1. **Upload PDF files:**
   - Navigate to the "Chat with PDF" section.
   - Use the file uploader to upload one or more PDF files containing text content.

2. **Process and extract text:**
   - After uploading the PDF files, click on the "Submit & Process" button.
   - The application will process the uploaded PDFs to extract text and generate embeddings using Google Generative AI.

3. **Ask a question:**
   - Enter a question related to the content of the uploaded PDF files in the text input field.
   - The application will use a conversational AI model to provide a response based on the question.



## Project Structure

   ```bash

   Google-Gemini/
   ├── .env                      # Environment variables
   ├── .gitignore                # Git ignore file
   ├── LICENSE                   # License file
   ├── app.py                    # main streamlit application
   ├── README.md                 # Project documentation
   ├── requirements.txt          # Required Python packages
   └── ChatWithPDF/              # Directory containing the application
      ├── chat_with_pdf.py       # Script containing the chat functions
      ├── app.py                 # chat Streamlit application
      └── README.md              # Detailed documentation for the application
   └── YoutubeSummarizer/        # Directory containing the application
      ├── youtube_summarizer.py  # Script containing the summarizer functions
      ├── app.py                 # YT summarizer Streamlit application
      └── README.md              # Detailed documentation for the application
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) - The app framework used.
- [Google Generative AI](https://ai.google/discover/generativeai/) - Models used for generating content and embeddings.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

Please ensure your pull request adheres to the code style of this project.

## Contact

For questions, feedback, or further assistance regarding the project, feel free to contact us at [priyanshushukla1217@gmail.com](mailto:priyanshushukla1217@gmail.com).
