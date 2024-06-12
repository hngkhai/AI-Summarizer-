##python -m venv .env
#.env/Scripts/activate
# render_template is used to render HTML templates
from flask import Flask,  request,render_template
from flask_restful import Api, Resource
model_name = "t5-base"
from transformers import pipeline
summarization = pipeline("summarization", model = model_name)
from transformers import T5ForConditionalGeneration, T5Tokenizer, AutoTokenizer


# initialize the model architecture and weights
model = T5ForConditionalGeneration.from_pretrained(model_name)
# initialize the model tokenizer
tokenizer =  AutoTokenizer.from_pretrained(model_name, legacy=False)
#initialize the Flask app
app = Flask(__name__)


# Define route for the home page
@app.route("/")
def index():
    # Render the chat.html template
    return render_template('chat.html')

# Define route for handling chat messages
@app.route("/get", methods=["GET", "POST"])
def chat():
    # Get the user input message from the form
    msg = request.form["msg"]
    # Call the function to get the response and return it
    return summarizer(msg)


def reduce_words(text, max_words):
    words = text.split()
    reduced_text = ' '.join(words[:max_words])
    return reduced_text



def summarizer(original_text):
    reduced_words= reduce_words(original_text, 800)
    summary_text = summarization(reduced_words)[0]['summary_text']

    # encode the text into tensor of integers using the appropriate tokenizer

    inputs = tokenizer.encode("summarize: " + summary_text, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(
    inputs, 
    max_length=150, 
    min_length=40, 
    length_penalty=2.0, 
    num_beams=4, 
    early_stopping=True)

    return tokenizer.decode(outputs[0])
if __name__ == '__main__':
    app.run()

