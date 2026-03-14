from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from PIL import Image
import io
import base64
import os

app = Flask(__name__)
CORS(app)

# Configure Gemini from environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    raise RuntimeError('GEMINI_API_KEY environment variable is not set')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/identify', methods=['POST'])
def identify_movie():
    try:
        # Get image from request
        data = request.json
        image_data = data['image'].split(',')[1]  # Remove data:image/jpeg;base64,
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Optional: Compress image to save tokens
        max_size = 800
        image.thumbnail((max_size, max_size))
        
        # Analyze with Gemini
        prompt = """
        Analyze this screenshot and identify the movie or TV show.
        
        Provide your answer in this EXACT format:
        TITLE: [Movie/Show name]
        YEAR: [Release year]
        CONFIDENCE: [High/Medium/Low]
        SCENE: [Brief scene description]
        ACTORS: [Visible actors, if recognizable]
        
        If you cannot identify it, say:
        TITLE: Unknown
        CONFIDENCE: Unable to identify
        SCENE: [Describe what you see]
        """
        
        response = model.generate_content([prompt, image])
        
        return jsonify({
            'success': True,
            'result': response.text
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy', 
        'message': 'Movie Identifier API is running'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
