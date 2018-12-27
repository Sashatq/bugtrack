from model.objects import Objects


def test_login(app):
    app.session.login("administrator", "test")
    assert app.session.is_logged_in_as("administrator")
    app.project.delete_project()
