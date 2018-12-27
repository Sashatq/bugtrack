from model.objects import Objects
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[7]/a/i").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, objects):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_form(objects)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        time.sleep(4)

    def fill_form(self, objects):
        self.change_field_value("name", objects.pname)
        self.change_field_value("description", objects.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[7]/a/i").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("td > a").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()