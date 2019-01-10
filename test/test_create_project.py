from model.objects import Objects


def test_create_project(app):
    list_projects = app.project.get_project_list()
    project = Objects(pname="nbv2", description="rt")
    app.project.create(project)
    new_list_projects = app.project.get_project_list()
    assert len(list_projects) + 1 == len(new_list_projects)
