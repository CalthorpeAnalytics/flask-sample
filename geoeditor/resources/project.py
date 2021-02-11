from typing import List

from flask.views import MethodView
from flask_smorest import Blueprint

from geoeditor.extensions import db
from geoeditor.schemas.project import Project
from geoeditor.models.project import ProjectModel

blueprint = Blueprint(
    "project", "project", url_prefix="/project", description="Operations on project"
)


@blueprint.route("/")
class Projects(MethodView):
    @blueprint.response(Project.Schema(many=True))
    def get(self) -> List[Project]:
        """List projects"""
        return [
            Project.Schema().load({"id": p.id, "name": p.name})
            for p in db.session.query(ProjectModel).all()
        ]

    @blueprint.arguments(Project.Schema())
    @blueprint.response(Project.Schema(), code=201)
    def post(self, new_data: Project) -> Project:
        """Add a new project"""
        item = ProjectModel(name=new_data.name)
        db.session.add(item)
        db.session.commit()
        return Project.Schema().load({"id": item.id, "name": item.name})


@blueprint.route("/<int:project_id>")
class ProjectsById(MethodView):
    @blueprint.response(Project.Schema())
    def get(self, project_id: int) -> Project:
        """Get project by ID"""
        item = db.session.query(ProjectModel).get(project_id)
        return Project.Schema().load({"id": item.id, "name": item.name})

    @blueprint.arguments(Project.Schema())
    @blueprint.response(Project.Schema())
    def put(self, update_data: Project, project_id: int) -> Project:
        """Update existing project"""
        item = db.session.query(ProjectModel).get(project_id)

        item.name = update_data.name
        db.session.add(item)
        db.session.commit()

        return Project.Schema().load({"id": item.id, "name": item.name})

    @blueprint.response(code=204)
    def delete(self, project_id: int) -> None:
        """Delete project"""
        item = db.session.query(ProjectModel).get(project_id)
        db.session.remove(item)
