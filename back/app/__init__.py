# coding=utf-8

from .utils import *
from .server import create_app
from .database import database


app = create_app()
database.init_app(app)
