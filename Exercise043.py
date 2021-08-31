import csv

data_dict={}

with open("Customer.csv","r",encoding="utf-8") as file:
    data = csv.DictReader(file, delimiter=",")
    for row in data:
        key = row["Id"]
        del row["Id"]
        data_dict[key] = row

print(data_dict["BOLID"])
