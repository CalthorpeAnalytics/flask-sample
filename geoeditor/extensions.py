"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_dataclass import dataclass as _dataclass
from flask_migrate import Migrate
from flask_smorest import Api


api = Api()
db = SQLAlchemy()
ma = Marshmallow()
dataclass = _dataclass(base_schema=ma.Schema)
migrate = Migrate()
