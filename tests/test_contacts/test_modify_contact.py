from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(
        Contact(firstname="edited", middlename="edited", lastname="edited", username="edited",
                title="edited", company="edited", address="editedAddress,105/10",
                homephone="+380000000", mobilephone="+3890000000", workphone="+00000000",
                fax="+000000000", email="editeddb@exampl.com", email2="editeddb2@example.com",
                email3="editeddb3@example.com", homepage="editedtest.db.com", birthday="28",
                birthmonth="April", birthyear="1987", aday="13", amonth="August", ayear="1999",
                address2="editedSecond Adress, 35/9", phone2="+00000000", notes="edited Testing notest"))


def test_modify_contact_from_details_page(app):
    app.contact.modify_from_details_page(
        Contact(firstname="edited from details", middlename="edited from details", lastname="edited from details",
                username="edited from details",
                title="edited from details", company="edited from details", address="edited from details",
                homephone="+380000000", mobilephone="+3890000000", workphone="+00000000",
                fax="+000000000", email="editedfromdetailsdb@exampl.com", email2="editedfromdetailsdb2@example.com",
                email3="editedfromdetailsdb3@example.com", homepage="eeditedfromdetailstest.db.com", birthday="14",
                birthmonth="May", birthyear="1977", aday="26", amonth="February", ayear="2010",
                address2="edited from detailsSecond Adress, 35/9", phone2="+00000000",
                notes="edited from details Testing notest"))
