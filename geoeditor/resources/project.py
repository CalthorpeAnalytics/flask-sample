from typing import List

from flask.views import MethodView
from flask import Blueprint

from geoeditor.extensions import db
from geoeditor.schemas.project import Project
from geoeditor.models.project import ProjectModel

blueprint = Blueprint(
    "project", "project", url_prefix="/project", description="Operations on project"
)


@blueprint.route("/")
class Projects(MethodView):

    def get(self) -> List[Project]:
        """List projects"""
        return [
            Project(id=p.id, name=p.name)
            for p in db.session.query(ProjectModel).all()
        ]

    def post(self, new_data: Project) -> Project:
        """Add a new project"""
        item = ProjectModel(name=new_data.name)
        db.session.add(item)
        db.session.commit()
        item = ProjectModel(name=new_data.name)
        return Project(id=item.id, name=item.name)


@blueprint.route("/<int:project_id>")
class ProjectsById(MethodView):

    def get(self, project_id: int) -> Project:
        """Get project by ID"""
        item = db.session.query(ProjectModel).get(project_id)
        return Project(id=item.id, name=item.name)

    def put(self, update_data: Project, project_id: int) -> Project:
        """Update existing project"""
        item = db.session.query(ProjectModel).get(project_id)

        item.name = update_data.name
        db.session.add(item)
        db.session.commit()

        return Project(id=item.id, name=item.name)

    def delete(self, project_id: int) -> None:
        """Delete project"""
        item = db.session.query(ProjectModel).get(project_id)
        db.session.remove(item)
