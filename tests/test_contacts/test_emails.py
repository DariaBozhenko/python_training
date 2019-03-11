from random import randrange


def test_email_on_home_page(app):
    all_contacts = app.contact.get_contact_list()
    user_index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contact_list(user_index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(user_index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_email_on_details_page(app):
    all_contacts = app.contact.get_contact_list()
    user_index = randrange(len(all_contacts))
    contact_from_detail_page = app.contact.get_contact_from_details_page(user_index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(user_index)
    assert merge(contact_from_detail_page) == merge_emails_like_on_detail_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def merge(contact):
    return "\n".join(contact.emails)


def merge_emails_like_on_detail_page(contact):
    return "\n".join(
        filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
