import re
from random import randrange


def test_phones_on_home_page(app):
    all_contacts = app.contact.get_contact_list()
    user_index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contact_list(user_index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(user_index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_details_page(app):
    all_contacts = app.contact.get_contact_list()
    user_index = randrange(len(all_contacts))
    contact_from_detail_page = app.contact.get_contact_from_details_page(user_index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(user_index)
    assert contact_from_detail_page.homephone == contact_from_edit_page.homephone
    assert contact_from_detail_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_detail_page.workphone == contact_from_edit_page.workphone
    assert contact_from_detail_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.homephone, contact.mobilephone, contact.workphone,
                                                           contact.phone2]))))
