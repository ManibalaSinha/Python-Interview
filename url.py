from flask import Flask, request, redirect, render_template
import random
import string

app = Flask(__name__)
url_map = {}  # In-memory dictionary to store short:long URLs

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        while short_code in url_map:
            short_code = generate_short_code()
        url_map[short_code] = original_url
        short_url = request.host_url + short_code
    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_original(short_code):
    original_url = url_map.get(short_code)
    if original_url:
        return redirect(original_url)
    return 'Invalid short URL', 404

if __name__ == '__main__':
    app.run(debug=True)
