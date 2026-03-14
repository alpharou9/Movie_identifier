# 🎬 Movie Identifier

An AI-powered web application that identifies movies and TV shows from screenshots. Perfect for when you see random clips on TikTok, YouTube, or Instagram and want to know what movie they're from!

![Movie Identifier Demo](https://img.shields.io/badge/AI-Powered-blue) ![Python](https://img.shields.io/badge/Python-3.8+-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🤖 **AI-Powered Identification** - Uses Google Gemini Vision AI to analyze screenshots
- 📱 **Mobile Friendly** - Access from your iPhone or Android device
- 🎯 **High Accuracy** - Identifies movies with confidence levels
- 🎭 **Actor Recognition** - Detects visible actors in scenes
- 📝 **Scene Descriptions** - Provides detailed context about the scene
- ⚡ **Fast Processing** - Results in 5-10 seconds
- 💰 **Free to Use** - 1,500 free identifications per day

## 🖼️ Screenshots

![Movie Identifier Interface](screenshot.png)
*Upload any movie screenshot and get instant identification*

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (free)
- Modern web browser (Chrome recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/movie-identifier.git
   cd movie-identifier
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your FREE Gemini API key**
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Click "Create API Key"
   - Copy your key

5. **Configure API key**
   - Open `app.py`
   - Replace `YOUR_API_KEY_HERE` with your actual API key:
   ```python
   GEMINI_API_KEY = 'AIzaSy...'
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open in browser**
   - Simply double-click `index.html`
   - Or open in browser: `http://localhost:5000`

## 📱 Mobile Access

Want to use it on your phone? Follow these steps:

### Setup for iPhone/Android

1. **Find your computer's IP address**
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```
   Look for your IPv4 address (e.g., `192.168.1.16`)

2. **Update index.html**
   - Open `index.html`
   - Find line with `http://localhost:5000`
   - Replace with `http://YOUR_IP:5000` (e.g., `http://192.168.1.16:5000`)

3. **Start both servers**
   
   **Terminal 1 - Backend:**
   ```bash
   python app.py
   ```
   
   **Terminal 2 - Frontend:**
   ```bash
   python -m http.server 8000
   ```

4. **Access from phone**
   - Make sure phone and computer are on **same WiFi**
   - Open browser on phone
   - Go to: `http://YOUR_IP:8000/index.html`

## 💡 How It Works

1. **Upload** - Take a screenshot from any video (TikTok, YouTube, Instagram, etc.)
2. **Analyze** - AI processes the image using Google Gemini Vision
3. **Identify** - Get movie title, year, confidence level, scene description, and actors
4. **Discover** - Learn what movie the clip is from instantly!

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **AI Model:** Google Gemini 2.5 Flash Vision
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Image Processing:** Pillow (PIL)

## 📊 API Usage & Limits

### Free Tier
- ✅ 1,500 requests per day
- ✅ 15 requests per minute
- ✅ Perfect for personal use
- ✅ No credit card required

### Paid Tier (if you upgrade)
- 💰 $0.00025 per image (~4,000 images for $1)
- 🚀 2,000 requests per minute
- ♾️ No daily limit

## 🎯 Example Results

```
✨ Identified!

TITLE: Snowden
YEAR: 2016
CONFIDENCE: High
SCENE: A man in a uniform, likely a TSA agent, is shown in what 
       appears to be an airport security checkpoint, leaning on a 
       counter and smiling.
ACTORS: LaKeith Stanfield
```

## 📁 Project Structure

```
movie-identifier/
├── app.py              # Flask backend server
├── index.html          # Web interface
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore file
```

## 🔧 Configuration

### Changing the Model

If you want to use a different Gemini model, edit `app.py`:

```python
# Current model
model = genai.GenerativeModel('gemini-2.5-flash')

# Alternative models
# model = genai.GenerativeModel('gemini-1.5-pro')
# model = genai.GenerativeModel('gemini-pro-vision')
```

### Adjusting Image Compression

To reduce token usage, you can adjust image compression in `app.py`:

```python
# Current setting (line 27)
max_size = 800

# For higher quality (uses more tokens)
max_size = 1200

# For lower quality (uses fewer tokens)
max_size = 600
```

## 🐛 Troubleshooting

### Common Issues

**"API key not valid"**
- Make sure you copied the entire API key
- Check for extra spaces
- Generate a new key at [Google AI Studio](https://aistudio.google.com/app/apikey)

**"Connection Error" on mobile**
- Ensure both devices are on the same WiFi
- Check that you updated `index.html` with correct IP address
- Verify both servers are running (ports 5000 and 8000)
- Try disabling Windows Firewall temporarily

**"Module not found"**
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

**"404 model not found"**
- Check the model name in `app.py` line 15
- Try using `gemini-2.5-flash` or `gemini-1.5-pro`

## 🚀 Future Enhancements

Potential features to add:

- [ ] Movie posters from TMDB API
- [ ] Streaming service links (Netflix, Prime, etc.)
- [ ] Save identification history
- [ ] Export results as PDF
- [ ] Similar movie recommendations
- [ ] Character/actor detection with links to IMDb
- [ ] Browser extension version
- [ ] Progressive Web App (PWA) for offline use

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for providing the vision API
- Flask for the lightweight web framework
- All the movie enthusiasts who struggle to identify random clips on social media!

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/YOUR_USERNAME/movie-identifier](https://github.com/YOUR_USERNAME/movie-identifier)

---

⭐ If you found this project helpful, please give it a star!

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/movie-identifier?style=social)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/movie-identifier?style=social)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/movie-identifier)

---

Made with ❤️ and AI
