# filepath: app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
try:
    from config import config
except ImportError:
    raise ImportError("The 'config' module could not be found. Ensure 'config.py' exists in the project directory with a 'config' object defined.")

# Ensure 'config.py' exists in the project directory
import os

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_CONFIG') or 'default'])

db = SQLAlchemy(app)

from app import models  # Import models here to avoid circular imports

if __name__ == '__main__':
    app.run(debug=True)
