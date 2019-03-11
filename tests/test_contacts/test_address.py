from random import randrange
import re


def test_address_on_home_page(app):
    all_contacts = app.contact.get_contact_list()
    user_index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contact_list(user_index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(user_index)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)


def clear(s):
    return re.sub(r"^\s+|\s+$", "", s, 0, re.M)
