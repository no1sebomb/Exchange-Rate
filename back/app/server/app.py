# coding=utf-8

from flask_smorest import Api

from .server import RateAPIServer
from .routes import rate_blueprint
from .handlers import handlers_blueprint

from app.config import CONFIG


app = RateAPIServer(__name__)

# Configurate app
app.config.update(CONFIG["server"]["config"])

# Database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
    CONFIG["database"]["username"],
    CONFIG["database"]["password"],
    CONFIG["database"]["host"],
    CONFIG["database"]["port"],
    CONFIG["database"]["schema"]
)

# Instantiate API docs object
api = Api(app)

# Register API blueprints
app.register_blueprint(handlers_blueprint)
api.register_blueprint(rate_blueprint)
