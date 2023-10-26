# Main Flask application
from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Configure the OpenAI API with your API key
openai.api_key = "https://api.openai.com/v1/chat/completions"

# Define a function to get code suggestions
def get_code_suggestions(code):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=code,
        max_tokens=50  # Adjust this as needed
    )
    return response.choices[0].text



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_suggestions', methods=['POST'])
def get_suggestions():
    code = request.form['code']
    suggestions = get_code_suggestions(code)
    return suggestions

if __name__ == '__main__':
    app.run(debug=True)
