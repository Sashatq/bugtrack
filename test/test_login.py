from model.objects import Objects


def test_login(app):
    assert app.session.is_logged_in_as("administrator")


    #app.project.create(Objects(pname="bbb", description="2wsx"))

