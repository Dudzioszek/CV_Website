from flask import Flask, render_template, request, redirect, url_for, make_response, send_from_directory
from flask_babel import Babel, gettext

app = Flask(__name__)

# Configure Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'pl'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Pobierz język z ciasteczka lub ustaw domyślny język na polski
    return request.cookies.get('locale') or request.accept_languages.best_match(['en', 'pl'])

# Dodaj funkcję get_locale do globalnego kontekstu Jinja2
app.jinja_env.globals['get_locale'] = get_locale

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/media/<path:filename>')
def media_files(filename):
    return send_from_directory('static/media', filename)

@app.route('/set_language/<language>')
def set_language(language):
    resp = make_response(redirect(request.referrer))
    resp.set_cookie('locale', language)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
