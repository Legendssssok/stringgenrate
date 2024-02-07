from .all_db import legend_db

def get_refill(id):
    legend_db.get_key("REFILL") or {}

def is_refill(id):
    users = list(get_refill())
    return id in users()

def add_refill(id, no_refill):
    users = get_refill()
    lol = list(users)
    if not id in lol:
        users[id] = no_refill
        return legend_db.set_key("REFILL", users)
    elif id in lol:
        users[id] = get_refill.get(id) + no_refill
        return legend_db.set_key("REFILL", users)
    return False


def rem_refill(id):
    user = get_refill()
    lol = list(users)
    if id in lol:
        if user.get(id) == 0:
            user.pop(id)
        new_number = user.get(id) - 1
        user[id] = new_number
        legend_db.set_key("REFILL", user)
    return False


 
