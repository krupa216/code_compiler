# CodeEX - Online Code Compiler

A sleek, modern online code compiler built with Python and Flask. Execute code in multiple programming languages with a beautiful, responsive UI.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Flask](https://img.shields.io/badge/flask-3.0-blue.svg)

## Features

✨ **Premium Features:**
- 🎨 Modern, dark-themed UI with gradient design
- ⚡ Fast code execution engine
- 🐍 Multi-language support (Python, JavaScript, Java, C++, C)
- 📊 Real-time execution time tracking
- 🎯 Syntax-highlighted code editor
- 📱 Fully responsive design (desktop & mobile)
- 🔒 Secure code execution with timeouts
- 🚀 Ready to deploy on Render

## Supported Languages

| Language | Version |
|----------|---------|
| Python | 3.8+ |
| JavaScript | Node.js 18+ |
| Java | 11+ |
| C++ | GCC 9+ |
| C | GCC 9+ |

## Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd code-compiler
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Deployment on Render

### Quick Deploy (Recommended)

1. **Fork this repository** on GitHub
2. **Connect Render to GitHub**
   - Go to [render.com](https://render.com)
   - Sign up / Login with GitHub
   - Click "New +" → "Web Service"
   - Select your repository

3. **Configure on Render**
   - Name: `code-compiler` (or any name)
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Plan: Free or Starter

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete (~2 minutes)
   - Access your app at the provided URL

### Environment Variables

No environment variables required for basic setup.

## Project Structure

```
code-compiler/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment config
├── render.yaml           # Render deployment settings
├── .gitignore            # Git ignore file
├── README.md             # This file
├── templates/
│   └── index.html        # Main UI template
└── static/               # (Optional) For static files
```

## Usage

### Writing Code

1. Select a programming language from the dropdown
2. Write or paste your code in the editor
3. Click "Run Code" or press `Ctrl+Enter` (or `Cmd+Enter` on Mac)
4. View output and execution time

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` / `Cmd+Enter` | Execute code |
| `Tab` | Indent code |

## API Documentation

### Execute Code

**Endpoint:** `POST /api/execute`

**Request:**
```json
{
  "code": "print('Hello, World!')",
  "language": "python"
}
```

**Response:**
```json
{
  "output": "Hello, World!\n",
  "error": "",
  "time": 0.123,
  "success": true
}
```

### Get Template

**Endpoint:** `GET /api/templates/<language>`

**Response:**
```json
{
  "template": "# Python Example\nprint('Hello, World!')"
}
```

## Security Features

- ✅ Code execution timeout (10 seconds)
- ✅ Output size limits (5000 characters)
- ✅ Input size limits (1MB max)
- ✅ Temporary file cleanup
- ✅ Sandboxed execution
- ✅ Language whitelist validation

## Performance

- **Response Time:** < 500ms (typical)
- **Execution Timeout:** 10 seconds per code
- **Max Output:** 5000 characters
- **Max Input:** 1MB per request

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py or use environment variable
PORT=8000 python app.py
```

### Module Not Found Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Render Deployment Issues

1. **Build fails:** Check if Python version is compatible
2. **Timeout:** Ensure no infinite loops in test code
3. **Memory:** Free tier has 512MB limit; optimize code

## Browser Compatibility

- ✅ Chrome/Chromium (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers

## Performance Tips

1. **Keep code snippets reasonable** (< 1000 lines)
2. **Avoid infinite loops** - will timeout
3. **Use `print()` strategically** for debugging
4. **Check network latency** if requests are slow

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

- Built with [Flask](https://flask.palletsprojects.com/)
- Deployed on [Render](https://render.com)
- Inspired by popular online code editors

## Support

For issues, questions, or suggestions:
1. Check existing issues
2. Create a new GitHub issue
3. Provide detailed error messages and steps to reproduce

## Roadmap

- [ ] Add more languages (Go, Rust, PHP)
- [ ] Code sharing via unique URLs
- [ ] Code syntax highlighting
- [ ] Dark/Light theme toggle
- [ ] Execution history
- [ ] User accounts and saved snippets
- [ ] Collaborative editing

---

**Made with ❤️ for developers**

Happy coding! 🚀
