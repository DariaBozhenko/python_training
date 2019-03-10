from selenium.webdriver.support.ui import Select
from model.contact import Contact
import time

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit new contact
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # pick the first record in the list
        wd.find_element_by_name("selected[]").click()
        # click Delete button
        wd.find_element_by_xpath('//*[@value="Delete"]').click()
        # confirm deletion
        wd.switch_to_alert().accept()
        # return to home page
        time.sleep(3)
        self.contact_cache = None

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # pick the first record in the list
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        # fill in the form with new data
        self.fill_contact_form(contact)
        # click update button
        wd.find_element_by_xpath('//*[@value="Update"]').click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_from_details_page(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # open details fo the first contact in the list
        wd.find_element_by_xpath('//*[@title="Details"]').click()
        # click modify button
        wd.find_element_by_name("modifiy").click()
        # fill in the form with new data
        self.fill_contact_form(contact)
        # click update button
        wd.find_element_by_xpath('//*[@value="Update"]').click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_from_modify_page(self):
        wd = self.app.wd
        self.open_contact_page()
        # pick the first record in the list
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        # click delete button
        wd.find_element_by_xpath('//*[@value="Delete"]').click()
        self.open_contact_page()
        self.contact_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        if not (
            wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath('//*[@value="Send e-Mail"]')) > 0):
            wd.find_element_by_link_text("home").click()
            wd.find_element_by_link_text("Last name")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.username)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_value_from_dropdown("bday", contact.birthday)
        self.select_value_from_dropdown("bmonth", contact.birthmonth)
        self.change_field_value("byear", contact.birthyear)
        self.select_value_from_dropdown("aday", contact.aday)
        self.select_value_from_dropdown("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def select_value_from_dropdown(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                column = element.find_elements_by_tag_name("td")
                first = column[2].text
                last = column[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=first, lastname=last, id=id))
        return list(self.contact_cache)
