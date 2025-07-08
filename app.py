import yaml
from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    try:
        with open('_config.yaml', 'r', encoding='utf-8') as file:
            website_data = yaml.safe_load(file)
        return render_template('index.html', data=website_data)
    except Exception as e:
        print(f"Error loading config: {e}")
        return f"Error loading configuration: {e}", 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
