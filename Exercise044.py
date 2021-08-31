import csv
import json

data_dict={}
with open("Customer.csv","r",encoding="utf-8") as file:
    data = csv.DictReader(file, delimiter=",")
    for row in data:
        key = row["Id"]
        del row["Id"]
        data_dict[key] = row

with open("customer.json","w",encoding="utf-8") as file:
    file.write(json.dumps(data_dict, indent=4))
