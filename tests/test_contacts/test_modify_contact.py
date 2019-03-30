from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
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
    edited_contact = Contact(firstname="edited", middlename="edited", lastname="edited", id=contact.id)
    app.contact.modify_contact_by_id(contact.id, edited_contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(edited_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())

        db_list = map(clean, db.get_contact_list())
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


def test_modify_contact_from_details_page(app, db, check_ui):
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
    edited_contact = Contact(firstname="edited from details", middlename="edited from details",
                             lastname="edited from details",
                             username="edited from details",
                             title="edited from details", company="edited from details", address="edited from details",
                             homephone="+380000000", mobilephone="+3890000000", workphone="+00000000",
                             fax="+000000000", email="editedfromdetailsdb@exampl.com",
                             email2="editedfromdetailsdb2@example.com",
                             email3="editedfromdetailsdb3@example.com", homepage="eeditedfromdetailstest.db.com",
                             birthday="14",
                             birthmonth="May", birthyear="1977", aday="26", amonth="February", ayear="2010",
                             address2="edited from detailsSecond Adress, 35/9", phone2="+00000000",
                             notes="edited from details Testing notest", id=contact.id)
    app.contact.modify_from_details_page_by_id(contact.id, edited_contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(edited_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())

        db_list = map(clean, db.get_contact_list())
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
