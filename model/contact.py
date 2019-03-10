from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, username=None, title=None, company=None,
                 address=None, homephone=None,
                 mobilephone=None, workphone=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                 birthday=None, birthmonth=None,
                 birthyear=None, aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None, id=None,
                 all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.username = username
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (
        self.firstname == other.firstname or self.firstname is None or other.firstname is None) \
               and (self.lastname == other.lastname or self.lastname is None or other.lastname is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
