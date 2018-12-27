from model.objects import Objects


def test_create_project(app):
    project = Objects(pname="test", description="Place text")
    app.project.create_project(project)
