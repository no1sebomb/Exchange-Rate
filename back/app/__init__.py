# coding=utf-8

from flask_migrate import Migrate

from .utils import *
from .server import create_app
from .database import database


app = create_app()
database.init_app(app)
migration = Migrate(app, database)
