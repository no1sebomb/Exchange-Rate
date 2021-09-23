# coding=utf-8

from .server import RateAPIServer
from .routes import rate_blueprint
from .handlers import handlers_blueprint


app = RateAPIServer(__name__)

# Register API blueprints
app.register_blueprint(handlers_blueprint)
app.register_blueprint(rate_blueprint)
