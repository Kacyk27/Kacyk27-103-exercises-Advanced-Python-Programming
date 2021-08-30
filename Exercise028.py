import json

def filter_active_users():
    with open("users.json", "r") as file:
        data=json.load(file)

    active=[]
    for user in data:
        if user["is_active"]:
            active.append(user)

    with open("active_users.json","w") as file:
        json.dump(active,file,indent=2)

filter_active_users()