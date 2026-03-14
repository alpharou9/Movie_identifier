# 🎬 Movie Identifier from Screenshots - Complete Project Guide

## Overview

An AI-powered web app that identifies movies from screenshots. Upload images from TikTok, YouTube, or Instagram, and get instant movie identification with details.

---

## Table of Contents

1. [Technical Analysis](#technical-analysis)
2. [Recommended Approach](#recommended-approach)
3. [Setup Instructions](#setup-instructions)
4. [Complete Code](#complete-code)
5. [Deployment Guide](#deployment-guide)
6. [Cost Analysis](#cost-analysis)
7. [Future Improvements](#future-improvements)

---

## Technical Analysis

### Do You Need AI?
**YES!** This is a perfect use case for vision AI.

### Should You Convert Image to Text First?
**NO!** Here's why:
- Modern vision models can directly identify movies from screenshots
- Converting to text loses visual context (actors' faces, cinematography, colors)
- Direct image analysis is actually MORE accurate for this use case

### Is It Token Expensive?
**Not as bad as you think:**
- Image analysis ≈ 85-170 tokens per image (cheap!)
- Text generation costs more than image input
- GPT-4 Vision: ~$0.01 per image
- **FREE alternatives available!** ✅

---

## Recommended Approach

### Option 1: FREE - Google Gemini Vision (RECOMMENDED)

**Why this is perfect:**
- ✅ **FREE** with generous limits (60 requests/minute)
- ✅ Excellent at identifying movies
- ✅ Can analyze images directly
- ✅ Simple API

**Pricing:**
- **FREE tier:** 15 requests/minute, 1,500 requests/day
- **Paid tier:** $0.00025 per image (4,000 images for $1!)

### Option 2: Claude Sonnet 4.5

**Pros:**
- ✅ Very accurate at movie identification
- ✅ Great at describing scenes
- ✅ Good context understanding

**Cost:**
- $3 per million input tokens
- Images: ~$0.0048 per image
- Still cheap! (~200 images for $1)

### Option 3: GPT-4 Vision

**Pros:**
- ✅ Highly accurate
- ✅ Well-documented

**Cons:**
- ❌ More expensive (~$0.01 per image)
- ❌ Requires OpenAI account

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- Text editor (VS Code recommended)
- Web browser (Chrome)
- Google account (for free Gemini API key)

### Step 1: Project Setup

```bash
# Create project folder
mkdir movie-identifier
cd movie-identifier

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install google-generativeai pillow flask flask-cors
```

### Step 2: Get FREE Google Gemini API Key

1. Go to: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy your API key (FREE, no credit card needed!)
4. Save it for the next step

### Step 3: Project Structure

Create these files in your `movie-identifier` folder:

```
movie-identifier/
├── venv/
├── app.py          # Backend Flask server
├── index.html      # Frontend web interface
└── README.md       # This file
```

---

## Complete Code

### Backend: `app.py`

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from PIL import Image
import io
import base64
import os

app = Flask(__name__)
CORS(app)

# Configure Gemini - REPLACE WITH YOUR API KEY
GEMINI_API_KEY = 'YOUR_API_KEY_HERE'
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/identify', methods=['POST'])
def identify_movie():
    try:
        # Get image from request
        data = request.json
        image_data = data['image'].split(',')[1]  # Remove data:image/jpeg;base64,
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
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
    return jsonify({'status': 'healthy', 'message': 'Movie Identifier API is running'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Frontend: `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Identifier</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 10px;
            font-size: 32px;
        }
        
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }
        
        .upload-area {
            border: 3px dashed #667eea;
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 20px;
            background: #f8f9ff;
        }
        
        .upload-area:hover {
            background: #e8ebff;
            border-color: #764ba2;
            transform: translateY(-2px);
        }
        
        .upload-area.dragover {
            background: #d8e0ff;
            border-color: #764ba2;
            transform: scale(1.02);
        }
        
        input[type="file"] {
            display: none;
        }
        
        .upload-icon {
            font-size: 48px;
            margin-bottom: 10px;
        }
        
        .upload-text {
            color: #666;
            font-size: 16px;
            margin-bottom: 5px;
        }
        
        .upload-hint {
            color: #999;
            font-size: 12px;
        }
        
        .preview-container {
            margin: 20px 0;
        }
        
        .preview-item {
            background: #f8f9ff;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
        }
        
        .preview-image {
            width: 100%;
            max-height: 300px;
            object-fit: contain;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }
        
        .result {
            margin-top: 15px;
            padding: 15px;
            background: white;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        
        .result h3 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 16px;
        }
        
        .result-content {
            white-space: pre-wrap;
            font-family: inherit;
            color: #333;
            line-height: 1.6;
            font-size: 14px;
        }
        
        .loading {
            text-align: center;
            padding: 20px;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .loading-text {
            color: #666;
            font-size: 14px;
        }
        
        .error {
            background: #fee;
            border-left-color: #f44;
        }
        
        .error-text {
            color: #c33;
        }
        
        .clear-btn {
            background: #f44;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            margin-top: 20px;
            width: 100%;
            transition: background 0.3s;
        }
        
        .clear-btn:hover {
            background: #d33;
        }
        
        .confidence-high {
            color: #28a745;
            font-weight: bold;
        }
        
        .confidence-medium {
            color: #ffc107;
            font-weight: bold;
        }
        
        .confidence-low {
            color: #dc3545;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎬 Movie Identifier</h1>
        <p class="subtitle">Upload screenshots from TikTok, YouTube, or Instagram to discover the movie!</p>
        
        <div class="upload-area" id="uploadArea">
            <div class="upload-icon">📷</div>
            <p class="upload-text">Click to upload or drag & drop</p>
            <p class="upload-hint">Supports JPG, PNG • Multiple images allowed</p>
            <input type="file" id="fileInput" accept="image/*" multiple>
        </div>
        
        <div id="previewContainer"></div>
    </div>

    <script>
        const uploadArea = document.getElementById('uploadArea');
        const fileInput = document.getElementById('fileInput');
        const previewContainer = document.getElementById('previewContainer');
        let processedCount = 0;

        // Click to upload
        uploadArea.addEventListener('click', () => fileInput.click());

        // Drag and drop handlers
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });

        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('dragover');
        });

        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            handleFiles(e.dataTransfer.files);
        });

        // File selection handler
        fileInput.addEventListener('change', (e) => {
            handleFiles(e.target.files);
        });

        function handleFiles(files) {
            // Don't clear existing results, just add new ones
            processedCount = 0;
            
            // Add clear button if not already present
            if (!document.getElementById('clearBtn')) {
                const clearBtn = document.createElement('button');
                clearBtn.id = 'clearBtn';
                clearBtn.className = 'clear-btn';
                clearBtn.textContent = 'Clear All Results';
                clearBtn.onclick = clearResults;
                previewContainer.appendChild(clearBtn);
            }
            
            Array.from(files).forEach((file, index) => {
                if (file.type.startsWith('image/')) {
                    processImage(file, Date.now() + index);
                }
            });
        }

        function clearResults() {
            previewContainer.innerHTML = '';
            fileInput.value = '';
        }

        async function processImage(file, uniqueId) {
            const reader = new FileReader();
            
            reader.onload = async (e) => {
                // Create preview container
                const previewDiv = document.createElement('div');
                previewDiv.className = 'preview-item';
                previewDiv.id = `preview-${uniqueId}`;
                previewDiv.innerHTML = `
                    <img src="${e.target.result}" class="preview-image" alt="Screenshot">
                    <div class="loading" id="loading-${uniqueId}">
                        <div class="spinner"></div>
                        <p class="loading-text">Analyzing movie...</p>
                    </div>
                    <div class="result" id="result-${uniqueId}" style="display: none;"></div>
                `;
                
                // Insert at the beginning (newest first)
                const clearBtn = document.getElementById('clearBtn');
                if (clearBtn) {
                    previewContainer.insertBefore(previewDiv, clearBtn);
                } else {
                    previewContainer.appendChild(previewDiv);
                }
                
                // Call API
                try {
                    const response = await fetch('http://localhost:5000/identify', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            image: e.target.result
                        })
                    });
                    
                    const data = await response.json();
                    
                    // Hide loading
                    document.getElementById(`loading-${uniqueId}`).style.display = 'none';
                    
                    // Show result
                    const resultDiv = document.getElementById(`result-${uniqueId}`);
                    resultDiv.style.display = 'block';
                    
                    if (data.success) {
                        // Format the result nicely
                        let formattedResult = data.result;
                        
                        // Add color coding for confidence
                        formattedResult = formattedResult.replace(
                            /CONFIDENCE: (High|Medium|Low)/gi,
                            (match, level) => {
                                const className = `confidence-${level.toLowerCase()}`;
                                return `CONFIDENCE: <span class="${className}">${level}</span>`;
                            }
                        );
                        
                        resultDiv.innerHTML = `
                            <h3>✨ Identified!</h3>
                            <div class="result-content">${formattedResult}</div>
                        `;
                    } else {
                        resultDiv.className = 'result error';
                        resultDiv.innerHTML = `
                            <h3>❌ Error</h3>
                            <p class="error-text">${data.error}</p>
                        `;
                    }
                    
                } catch (error) {
                    document.getElementById(`loading-${uniqueId}`).style.display = 'none';
                    const resultDiv = document.getElementById(`result-${uniqueId}`);
                    resultDiv.style.display = 'block';
                    resultDiv.className = 'result error';
                    resultDiv.innerHTML = `
                        <h3>❌ Connection Error</h3>
                        <p class="error-text">Could not connect to server. Make sure the backend is running on http://localhost:5000</p>
                        <p class="error-text" style="font-size: 12px; margin-top: 10px;">Error: ${error.message}</p>
                    `;
                }
            };
            
            reader.readAsDataURL(file);
        }
    </script>
</body>
</html>
```

---

## Running the App

### Step 1: Start the Backend

```bash
# Make sure you're in the project folder and virtual environment is activated
cd movie-identifier
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the Flask server
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Debugger is active!
```

### Step 2: Open the Frontend

Simply open `index.html` in your web browser:
- **Option 1:** Double-click `index.html`
- **Option 2:** Right-click → Open with → Chrome
- **Option 3:** Drag and drop into Chrome

### Step 3: Use the App

1. Click the upload area or drag & drop images
2. Select one or multiple screenshots
3. Wait for AI analysis (5-10 seconds per image)
4. View results with movie title, year, confidence, and scene description

---

## Using on iPhone

### Find Your Computer's IP Address

**On Mac:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

**On Windows:**
```bash
ipconfig
```

Look for something like: `192.168.1.100`

### Update index.html

In the `fetch()` call, replace `localhost` with your IP:

```javascript
const response = await fetch('http://192.168.1.100:5000/identify', {
```

### Access from iPhone

1. Make sure iPhone and computer are on same WiFi
2. Open Chrome on iPhone
3. Go to: `http://192.168.1.100:8000/index.html` (replace with your IP)
4. Upload screenshots from camera roll!

---

## Cost Analysis

### Gemini FREE Tier (Recommended)
- **1,500 requests/day** = FREE
- That's **1,500 screenshots per day** at $0!
- Perfect for personal use

### If You Exceed Free Tier

| Service | Cost per Image | Images per $1 |
|---------|----------------|---------------|
| Gemini Pro | $0.00025 | 4,000 |
| Claude | $0.0048 | 208 |
| GPT-4 Vision | $0.01 | 100 |

**Verdict:** For personal use, Gemini FREE tier is more than enough!

---

## Future Improvements

### Phase 2: Enhanced Features

1. **Movie Posters**
   - Fetch from TMDB API
   - Display alongside results

2. **Streaming Links**
   - Show where to watch (Netflix, Prime, etc.)
   - Use JustWatch API

3. **Similar Movies**
   - Recommend similar films
   - Based on genre/director/cast

4. **Save History**
   - Store results in browser localStorage
   - Export as PDF or share

5. **Better Mobile Support**
   - Progressive Web App (PWA)
   - Install on home screen
   - Offline support

### Phase 3: Advanced AI

1. **Character Recognition**
   - Identify specific actors in frame
   - Link to their filmography

2. **Quote Extraction**
   - Extract famous quotes from scene
   - Search quotes database

3. **Timestamp Detection**
   - Identify exact scene timing
   - Deep link to streaming service

4. **Batch Processing**
   - Upload entire folders
   - Process hundreds of images

### Phase 4: Social Features

1. **User Accounts**
   - Save favorite identifications
   - Share with friends

2. **Community Database**
   - Crowdsource difficult identifications
   - Rate accuracy

3. **Browser Extension**
   - Right-click any image → Identify movie
   - Works on any website

---

## Troubleshooting

### Backend won't start

**Error:** `ModuleNotFoundError: No module named 'flask'`
```bash
# Make sure virtual environment is activated
source venv/bin/activate
pip install flask flask-cors google-generativeai pillow
```

### API Key Error

**Error:** `API key not valid`
- Check you copied the full API key
- Make sure there are no extra spaces
- Get a new key from: https://aistudio.google.com/app/apikey

### CORS Error

**Error:** `Access to fetch blocked by CORS policy`
- Make sure Flask server is running
- Check `flask-cors` is installed
- Try accessing via `http://` not `file://`

### Can't connect from iPhone

**Error:** `Failed to fetch`
- Check firewall settings on computer
- Make sure both devices on same WiFi
- Try disabling firewall temporarily
- Use computer's IP address, not localhost

### Image too large

**Error:** `Image file too large`

Add image compression in `app.py`:
```python
# Add before sending to Gemini
max_size = 800
image.thumbnail((max_size, max_size))
```

---

## Deployment (Optional)

### Deploy Backend to Render (Free)

1. Create `requirements.txt`:
```
flask==3.0.0
flask-cors==4.0.0
google-generativeai==0.3.2
pillow==10.1.0
```

2. Create `render.yaml`:
```yaml
services:
  - type: web
    name: movie-identifier
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: GEMINI_API_KEY
        sync: false
```

3. Push to GitHub
4. Connect to Render.com
5. Deploy!

### Deploy Frontend to Netlify (Free)

1. Update API URL in `index.html` to your Render URL
2. Drag & drop `index.html` to Netlify
3. Done!

---

## Alternative APIs

### If Gemini doesn't work well:

**Claude API:**
```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": base64_image}},
            {"type": "text", "text": prompt}
        ]
    }]
)
```

**GPT-4 Vision:**
```python
from openai import OpenAI

client = OpenAI(api_key="your-key")

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }]
)
```

---

## License

This project is for educational purposes. Movie identification uses AI vision models.

---

## Support

Having issues? Check:
1. Virtual environment is activated
2. All packages installed
3. API key is correct
4. Backend is running on port 5000
5. No firewall blocking connections

---

## Next Steps

1. **Get API key** from Google AI Studio
2. **Copy the code** into your files
3. **Run** `python app.py`
4. **Open** `index.html` in browser
5. **Upload** a screenshot and test!

Good luck! 🚀
