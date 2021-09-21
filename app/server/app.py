# coding=utf-8

from .server import RateAPIServer
from .routes import rate_blueprint


app = RateAPIServer(__name__)

# Register API blueprints
app.register_blueprint(rate_blueprint)
