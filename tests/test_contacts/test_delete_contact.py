from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Dara", middlename="Test", lastname="Bozhenko", username="dbozhenko",
                                   title="TestContact", company="Company", address="Address,105/10",
                                   homephone="+38048578993", mobilephone="+38902849903", workphone="+98248585985",
                                   fax="+89240984749", email="db@exampl.com", email2="db2@example.com",
                                   email3="db3@example.com", homepage="test.db.com", birthday="4",
                                   birthmonth="July", birthyear="1989", aday="26", amonth="November", ayear="2000",
                                   address2="Second Adress, 35/9", phone2="+924050485498", notes="Testing notest"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())

        db_list = map(clean, db.get_contact_list())
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


def test_delete_contact_from_modify_page(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Dara", middlename="Test", lastname="Bozhenko", username="dbozhenko",
                                   title="TestContact", company="Company", address="Address,105/10",
                                   homephone="+38048578993", mobilephone="+38902849903", workphone="+98248585985",
                                   fax="+89240984749", email="db@exampl.com", email2="db2@example.com",
                                   email3="db3@example.com", homepage="test.db.com", birthday="4",
                                   birthmonth="July", birthyear="1989", aday="26", amonth="November", ayear="2000",
                                   address2="Second Adress, 35/9", phone2="+924050485498", notes="Testing notest"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_from_modify_page_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())

        db_list = map(clean, db.get_contact_list())
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
