from flask import Flask, render_template
import os

app = Flask(__name__, 
            static_folder=os.path.join(os.path.dirname(__file__), 'page', 'static'),
            static_url_path='/static',
            template_folder=os.path.join(os.path.dirname(__file__), 'page', 'templates'))

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)