# Text Summarizer Chatbot

A web-based chatbot that summarizes text using the Hugging Face Transformers library. Built with Flask (Python), Bootstrap (HTML/CSS), and the T5 model for text summarization.

**Note**: This project is for **practice purposes only** and is not intended for production use. It was created to improve my skills in web development, NLP, and working with APIs.

## Features
- **Text Summarization**: Summarizes up to 800 words of input text.
- **User-Friendly Interface**: Clean and responsive UI built with Bootstrap.
- **Real-Time Interaction**: Users can interact with the chatbot in real-time.
- **Customizable**: Easily extendable to support other NLP tasks or models.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **NLP Model**: Hugging Face Transformers (`t5-base`)
- **JavaScript**: jQuery for AJAX requests

## Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/text-summarizer-chatbot.git
   cd text-summarizer-chatbot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .env
   source .env/bin/activate  # On Windows, use `.env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000`.

## Usage
1. Enter your text in the input box and click "Submit".
2. The chatbot will process the text and display the summarized version.

## Project Structure
```
text-summarizer-chatbot/
├── app.py               # Flask application
├── static/              # Static files (CSS, JS, images)
│   └── style.css        # Custom CSS for the chatbot
├── templates/           # HTML templates
│   └── chat.html        # Chatbot interface
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the pre-trained T5 model.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Bootstrap](https://getbootstrap.com/) for the frontend design.

