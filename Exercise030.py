import json
import collections

def json_to_object():
    with open("users.json","r") as file:
        data=json.load(file)

    attrs= tuple(data[0].keys())

    User=collections.namedtuple("User",attrs)

    values= [tuple(user.values()) for user in data]
    users=[User(*user) for user in values]
    return users