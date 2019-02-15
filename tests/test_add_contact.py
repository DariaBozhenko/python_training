# -*- coding: utf-8 -*-
import pytest

from contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.create_new_contact(Contact(firstname="Dara", middlename="Test", lastname="Bozhenko", username="dbozhenko",
                                        title="TestContact", company="Company", address="Address,105/10",
                                        homephone="+38048578993", mobilephone="+38902849903", workphone="+98248585985",
                                        fax="+89240984749", email="db@exampl.com", email2="db2@example.com",
                                        email3="db3@example.com", homepage="test.db.com", birthday="4",
                                        birthmonth="July", birthyear="1989", aday="26", amonth="November", ayear="2000",
                                        address2="Second Adress, 35/9", phone2="+924050485498", notes="Testing notest"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.create_new_contact(Contact(firstname="", middlename="", lastname="", username="", title="", company="",
                                            address="", homephone="", mobilephone="", workphone="", fax="", email="",
                                            email2="", email3="", homepage="", birthday="", birthmonth="-",
                                            birthyear="",
                                            aday="", amonth="-", ayear="", address2="", phone2="", notes=""))
    app.session.logout()
