# coding=utf-8

from flask_sqlalchemy import SQLAlchemy

from app.config import CONFIG


database = SQLAlchemy(engine_options=CONFIG["database"]["engine_options"])
