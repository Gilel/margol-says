from flask import Flask, request, jsonify, send_from_directory
import openai
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        user_text = data.get('text', '')

        # Create the prompt for OpenAI
        prompt = f"""
        בתור מרגול, נתבקשת לתת עצה או תגובה לאדם שכתב:
        "{user_text}"
        
        אנא תני תשובה בסגנון של מרגול - חכמה, אמפתית, ועם נגיעה של הומור עדין.
        התשובה צריכה להיות בעברית ובטון חם ותומך.
        """

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "את מרגול, דמות חכמה ואמפתית שנותנת עצות חיים בסגנון ייחודי"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        # Extract the response
        ai_response = response.choices[0].message.content

        return jsonify({"response": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
