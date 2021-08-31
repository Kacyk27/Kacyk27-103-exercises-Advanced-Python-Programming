import csv

with open("Customer.csv","r",encoding="utf-8") as file:
    data = csv.reader(file, delimiter=",")
    columns=next(data)
    rows=tuple(data)
x=[]
for row in rows:
    x.append(row[8])

print(sorted(set(x)))