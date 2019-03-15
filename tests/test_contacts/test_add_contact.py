# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
from strgen import StringGenerator


def random_string(prefix):
    symbols = StringGenerator('[\l]{1:10}&[\W]{0:4}').render()
    return prefix + symbols


def random_phone():
    symbols = StringGenerator('[0-9]{0:16}&( \+\-\(\))').render()
    return symbols


def random_address():
    symbols = StringGenerator('[\w\W]{1:50}').render()
    return symbols


def select_random_day():
    days = [i for i in range(1, 32)]
    return str(random.choice(days))


def select_random_month():
    months = ['-', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    return random.choice(months)


def random_mail():
    mail = StringGenerator('[\c]{10}[\p][\c]{5:10}@[\c]{3:12}.(com|net|org)').render()
    return mail


def random_year():
    year = StringGenerator('[\d]{4}').render()
    return year


def random_website():
    website = StringGenerator('[\l]{0:20}&[\d\p\s]{0:10}').render()
    return website


testdata = [Contact(firstname="", middlename="",
                    lastname="", username="",
                    title="", company="", address="", homephone="", mobilephone="", workphone="", fax="", email="",
                    email2="",
                    email3="", homepage="", birthday="", aday="", birthmonth="-", amonth="-", birthyear="", ayear="",
                    address2="", phone2="", notes="")] + [
               Contact(firstname=random_string('first'), middlename=random_string('middle'),
                       lastname=random_string('last'), username=random_string('user'), title=random_string('title'),
                       company=random_string('comp'), address=random_address(), homephone=random_phone(),
                       mobilephone=random_phone(),
                       workphone=random_phone(), fax=random_phone(), email=random_mail(), email2=random_mail(),
                       email3=random_mail(),
                       homepage=random_website(), birthday=select_random_day(), aday=select_random_day(),
                       birthmonth=select_random_month(),
                       amonth=select_random_month(), birthyear=random_year(), ayear=random_year(),
                       address2=random_address(),
                       phone2=random_phone(), notes=random_string('notes'))
               for i in range(5)
               ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)