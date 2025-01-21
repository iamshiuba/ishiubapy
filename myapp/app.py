# app.py
from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__, 
    static_url_path='/static',
    static_folder='static')

@app.route('/')
def index():
    return render_template('pages/index.html', title='Homepage')

@app.route('/streaming')
def streaming():
    return render_template('pages/streaming.html', title='Streaming')

@app.route('/about')
def about():
    return render_template('pages/about.html', title='About')

@app.route('/tos')
def tos():
    return render_template('pages/tos.html', title='Terms of Service')

@app.route('/privacy')
def privacy():
    return render_template('pages/privacy.html', title='Privacy Policy')

@app.route('/static/translations/<filename>')
def translations(filename):
    return send_from_directory('static/translations', filename)

if __name__ == '__main__':
    app.run(debug=True)