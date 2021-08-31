import csv

with open("cdr.csv","r") as file:
    data=csv.reader(file, delimiter=",")
    columns=next(data)
    rows=list(data)
    closes = list(map(lambda row: float(row[4]), rows))

# Hard one for me.
def moving_avg(prices):
    id = 0
    moving_averages = []

    while id < len(prices) - 2:
        current_window = prices[id: id+3]
        window_average = round(sum(current_window) / 3,2)
        moving_averages.append(window_average)
        id += 1

    return moving_averages

print(moving_avg(closes))