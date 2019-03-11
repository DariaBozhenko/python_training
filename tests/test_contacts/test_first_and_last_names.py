import re
from random import randrange


def test_first_and_last_names_on_home_page(app):
    all_contacts = app.contact.get_contact_list()
    user_index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contact_list(user_index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(user_index)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)


def test_first_and_last_names_on_details_page(app):
    all_contacts = app.contact.get_contact_list()
    user_index = randrange(len(all_contacts))
    contact_from_detail_page = app.contact.get_contact_from_details_page(user_index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(user_index)
    assert contact_from_detail_page.fullname == merge_name_like_on_details_page(contact_from_edit_page)


def clear(s):
    return re.sub(r"^\s+|\s+$", "", s)


def merge_name_like_on_details_page(contact):
    return " ".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                  filter(lambda x: x is not None,
                                                         [contact.firstname, contact.middlename, contact.lastname]))))
