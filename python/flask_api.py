from flask_cors import CORS
from flask import Flask, jsonify
from utils.word_guesses_database import db_instance

app = Flask(__name__)
CORS(app)  # Apply CORS to your Flask app


@app.route('/api/get_random_word')
def index():
    random_word = db_instance.get_random_word()
    # Create some sample data
    response = {
        'topic': random_word[1],
        'hint': random_word[2],
        'answer': random_word[3],
    }
    # Return a JSON response
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
