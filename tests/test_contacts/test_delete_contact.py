from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Dara", middlename="Test", lastname="Bozhenko", username="dbozhenko",
                                   title="TestContact", company="Company", address="Address,105/10",
                                   homephone="+38048578993", mobilephone="+38902849903", workphone="+98248585985",
                                   fax="+89240984749", email="db@exampl.com", email2="db2@example.com",
                                   email3="db3@example.com", homepage="test.db.com", birthday="4",
                                   birthmonth="July", birthyear="1989", aday="26", amonth="November", ayear="2000",
                                   address2="Second Adress, 35/9", phone2="+924050485498", notes="Testing notest"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts

def test_delete_contact_from_modify_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Dara", middlename="Test", lastname="Bozhenko", username="dbozhenko",
                                   title="TestContact", company="Company", address="Address,105/10",
                                   homephone="+38048578993", mobilephone="+38902849903", workphone="+98248585985",
                                   fax="+89240984749", email="db@exampl.com", email2="db2@example.com",
                                   email3="db3@example.com", homepage="test.db.com", birthday="4",
                                   birthmonth="July", birthyear="1989", aday="26", amonth="November", ayear="2000",
                                   address2="Second Adress, 35/9", phone2="+924050485498", notes="Testing notest"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_from_modify_page(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
