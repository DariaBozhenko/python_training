from selenium.webdriver.support.ui import Select
from model.contact import Contact
import time
import re

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # pick the first record in the list
        wd.find_elements_by_name("selected[]")[index].click()
        # click Delete button
        wd.find_element_by_xpath('//*[@value="Delete"]').click()
        # confirm deletion
        wd.switch_to_alert().accept()
        # return to home page
        wd.find_elements_by_css_selector("div.msgbox")
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_edit_page(index)
        # fill in the form with new data
        self.fill_contact_form(contact)
        # click update button
        wd.find_element_by_xpath('//*[@value="Update"]').click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_details_page(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath('//*[@title="Details"]')[index].click()


    def modify_from_details_page(self, index, contact):
        wd = self.app.wd
        # open details for random contact in the list
        self.open_details_page(index)
        # click modify button
        wd.find_element_by_name("modifiy").click()
        # fill in the form with new data
        self.fill_contact_form(contact)
        # click update button
        wd.find_element_by_xpath('//*[@value="Update"]').click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_from_modify_page(self, index):
        wd = self.app.wd
        self.open_edit_page(index)
        # click delete button
        wd.find_element_by_xpath('//*[@value="Delete"]').click()
        self.open_contact_page()
        self.contact_cache = None

    def open_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # pick any record in the list
        wd.find_elements_by_xpath('//*[@title="Edit"]')[index].click()

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

    def get_contact_list(self, index=None):
        if index is None:
            if self.contact_cache is None:
                wd = self.app.wd
                self.open_contact_page()
                self.contact_cache = []
                for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                    column = element.find_elements_by_tag_name("td")
                    first = column[2].text
                    last = column[1].text
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    all_emails = column[4].text
                    all_phones = column[5].text
                    address = column[3].text
                    self.contact_cache.append(
                        Contact(firstname=first, lastname=last, id=id, all_phones_from_home_page=all_phones,
                                all_emails_from_home_page=all_emails, address=address))
            return list(self.contact_cache)
        else:
            wd = self.app.wd
            self.open_contact_page()
            element = wd.find_elements_by_css_selector("tr[name=entry]")[index]
            column = element.find_elements_by_tag_name("td")
            first = column[2].text
            last = column[1].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            all_emails = column[4].text
            all_phones = column[5].text
            address = column[3].text
            return Contact(firstname=first, lastname=last, id=id, all_phones_from_home_page=all_phones,
                           all_emails_from_home_page=all_emails, address=address)


    def get_contact_from_details_page(self, index):
        wd = self.app.wd
        self.open_details_page(index)
        text = wd.find_element_by_id("content").text
        fullname = wd.find_element_by_xpath('//*[@id=\"content\"]/b').text
        homephone = re.search("H: (.*)", text).group(1)
        workhone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        emails = re.findall("\S+@\S+", text)
        return Contact(fullname=fullname, homephone=homephone, workphone=workhone, mobilephone=mobilephone,
                       phone2=phone2, emails=emails)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_page(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, middlename=middlename, lastname=lastname, id=id, address=address,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2, email=email, email2=email2, email3=email3)
