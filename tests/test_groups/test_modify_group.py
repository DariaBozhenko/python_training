from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name=""))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edited_group = Group(name="testdbname", id=group.id)
    app.group.modify_group_by_id(group.id, edited_group)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(edited_group)
    assert sorted(old_groups, key=Group.id_or_max) == new_groups
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())

        db_list = map(clean, db.get_group_list())
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

# def test_modify_group_header(app):
#   if app.group.count() == 0:
#      app.group.create(Group(name="Test", header=""))
# old_groups = app.group.get_group_list()
# app.group.modify_first_group(Group(header="edited header"))
# new_groups = app.group.get_group_list()
# assert len(old_groups) == len(new_groups)
