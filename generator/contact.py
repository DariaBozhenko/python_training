from model.contact import Contact
import random
from strgen import StringGenerator
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
