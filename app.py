import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Read APP_MESSAGE from environment variable; provide a default if not set
    message = os.getenv('APP_MESSAGE', 'Default message')
    return message

@app.route('/health')
def health():
    # Read APP_HEALTH from environment variable
    health_status = os.getenv('APP_HEALTH', 'healthy')
    return health_status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)