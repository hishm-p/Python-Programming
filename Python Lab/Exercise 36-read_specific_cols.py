import csv

with open("sample.csv", "r") as file:
    csvrdr = csv.reader(file)
    for row in csvrdr:
        print(row[1], row[2])  # printing only 2 column
    file.close()