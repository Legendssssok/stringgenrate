from StringSessionBot.database.all_db import legend_db


def get_tokenusers():
    return legend_db.get_key("TOKEN") or []


def is_tokenusers(id):
    return id in get_tokenusers()


def add_tokenusers(id):
    tusers = get_tokenusers()
    if not id in tusers:
        tusers.append(id)
        return legend_db.set_key("TOKEN", tusers)
    return False


def del_tokenusers(id):
    if is_tokenusers(id):
        tusers = get_tokenusers()
        tusers.remove(id)
        return legend_db.set_key("TOKEN", tusers)
    return False
