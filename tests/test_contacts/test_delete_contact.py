def test_delete_contact(app):
    app.contact.delete_first_contact()


def test_delete_contact_from_modify_page(app):
    app.contact.delete_contact_from_modify_page()
