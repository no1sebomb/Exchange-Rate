# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.server import app
from app.config import CONFIG


database = SQLAlchemy(app, engine_options=CONFIG["database"]["engine_options"])
migrate = Migrate(app, database)
