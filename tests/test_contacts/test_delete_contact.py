def test_delete_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_delete_contact_from_modify_page(app):
    app.session.login("admin", "secret")
    app.contact.delete_contact_from_modify_page()
    app.session.logout()
