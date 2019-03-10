# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Dara", middlename="Test", lastname="Bozhenko", homephone="+38082878",
                      mobilephone="+873483748985",
                      workphone="+8977787887", phone2="+83888777874")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", username="", title="", company="",
#                      address="", homephone="", mobilephone="", workphone="", fax="", email="",
#                      email2="", email3="", homepage="", birthday="", birthmonth="-",
#                      birthyear="",
#                      aday="", amonth="-", ayear="", address2="", phone2="", notes="")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
