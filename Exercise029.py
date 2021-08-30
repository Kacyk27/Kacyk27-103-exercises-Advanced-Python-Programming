import json


def json_to_csv():
    with open("users.json","r") as file:
        data=json.load(file)

    headers = ",".join(data[0].keys())
    users=[user.values() for user in data]
    rows=[",".join([str(item) for item in user]) for user in users]

    with open("users.csv","w") as file:
        file.write(headers + "\n")
        for row in rows:
            file.write(row+"\n")