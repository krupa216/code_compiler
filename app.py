from flask import Flask, render_template, request, jsonify
import subprocess
import sys
import os
from datetime import datetime
import time

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB max request size
app.config['TIMEOUT'] = 10  # 10 second execution timeout

# Security: Languages and their commands
SUPPORTED_LANGUAGES = {
    'python': {
        'name': 'Python 3',
        'ext': '.py',
        'command': [sys.executable, '{file}'],
        'icon': '🐍'
    },
    'javascript': {
        'name': 'JavaScript (Node.js)',
        'ext': '.js',
        'command': ['node', '{file}'],
        'icon': '⚡'
    },
    'java': {
        'name': 'Java',
        'ext': '.java',
        'command': ['java', '-cp', '.', '{classname}'],
        'compile': ['javac', '{file}'],
        'icon': '☕'
    },
    'cpp': {
        'name': 'C++',
        'ext': '.cpp',
        'command': ['{output}'],
        'compile': ['g++', '{file}', '-o', '{output}'],
        'icon': '⚙️'
    },
    'c': {
        'name': 'C',
        'ext': '.c',
        'command': ['{output}'],
        'compile': ['gcc', '{file}', '-o', '{output}'],
        'icon': '📝'
    }
}

@app.route('/')
def index():
    """Render the main page"""
    languages = [
        {'id': lang, 'name': config['name'], 'icon': config['icon']}
        for lang, config in SUPPORTED_LANGUAGES.items()
    ]
    return render_template('index.html', languages=languages)

@app.route('/api/execute', methods=['POST'])
def execute_code():
    """Execute code and return output"""
    try:
        data = request.get_json()
        language = data.get('language', 'python')
        code = data.get('code', '')
        
        # Validate language
        if language not in SUPPORTED_LANGUAGES:
            return jsonify({'error': 'Language not supported'}), 400
        
        if not code.strip():
            return jsonify({'error': 'Code cannot be empty'}), 400
        
        lang_config = SUPPORTED_LANGUAGES[language]
        
        # Create temp file
        temp_dir = '/tmp/code_exec'
        os.makedirs(temp_dir, exist_ok=True)
        
        if language == 'java':
            filename = f"{temp_dir}/Main.java"
        else:
            filename = f"{temp_dir}/code{lang_config['ext']}"
        
        # Write code to file
        with open(filename, 'w') as f:
            f.write(code)
        
        output = ""
        error = ""
        execution_time = 0
        
        try:
            # Compile if needed
            if 'compile' in lang_config:
                compile_cmd = [cmd.replace('{file}', filename).replace('{output}', f"{temp_dir}/code") 
                              for cmd in lang_config['compile']]
                subprocess.run(compile_cmd, cwd=temp_dir, capture_output=True, 
                             timeout=5, check=True)
            
            # Execute code
            cmd = lang_config['command'].copy()
            cmd = [c.replace('{file}', filename)
                    .replace('{output}', f"{temp_dir}/code")
                    .replace('{classname}', 'Main')
                    for c in cmd]
            
            start_time = time.time()
            result = subprocess.run(cmd, cwd=temp_dir, capture_output=True, 
                                   timeout=10, text=True, check=False)
            execution_time = time.time() - start_time
            
            output = result.stdout
            error = result.stderr
            
            # Limit output
            max_output = 5000
            if len(output) > max_output:
                output = output[:max_output] + f"\n... (output truncated, {len(output)} chars total)"
            if len(error) > max_output:
                error = error[:max_output] + f"\n... (error truncated, {len(error)} chars total)"
        
        except subprocess.TimeoutExpired:
            error = "Execution timeout! Code took too long to run."
        except Exception as e:
            error = str(e)
        
        # Cleanup
        try:
            import glob
            for f in glob.glob(f"{temp_dir}/*"):
                os.remove(f)
        except:
            pass
        
        return jsonify({
            'output': output,
            'error': error,
            'time': round(execution_time, 3),
            'success': not error or error == ''
        })
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/templates/<language>')
def get_template(language):
    """Get code template for a language"""
    templates = {
        'python': '''# Python Example
print("Hello, World!")
x = 10
y = 20
print(f"Sum: {x + y}")''',
        
        'javascript': '''// JavaScript Example
console.log("Hello, World!");
const x = 10;
const y = 20;
console.log(`Sum: ${x + y}`);''',
        
        'java': '''public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        int x = 10;
        int y = 20;
        System.out.println("Sum: " + (x + y));
    }
}''',
        
        'cpp': '''#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    int x = 10;
    int y = 20;
    cout << "Sum: " << (x + y) << endl;
    return 0;
}''',
        
        'c': '''#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    int x = 10;
    int y = 20;
    printf("Sum: %d\\n", x + y);
    return 0;
}'''
    }
    
    return jsonify({'template': templates.get(language, '')})

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
