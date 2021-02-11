from geoeditor.extensions import db


class ProjectModel(db.Model):
    """Project"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
