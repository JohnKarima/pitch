from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)


bootstrap = Bootstrap(app)

from app import views
