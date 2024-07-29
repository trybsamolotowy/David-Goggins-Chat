import openai
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='static')

openai.api_key = ''

def generate_response(prompt):
    goggins_prompt = f"David Goggins style motivational speaker: {prompt}\nGoggins: "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are David Goggins, a motivational speaker known for your tough and direct speech."},
            {"role": "user", "content": goggins_prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

@app.route('/api/askGoggins', methods=['POST'])
def ask_goggins():
    data = request.json
    prompt = data.get('prompt')
    response = generate_response(prompt)
    return jsonify({"response": response})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
