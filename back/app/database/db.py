# coding=utf-8

from flask_sqlalchemy import SQLAlchemy

from ..config import CONFIG


database = SQLAlchemy(engine_options=CONFIG["database"]["engine_options"])
