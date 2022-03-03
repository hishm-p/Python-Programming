import csv
d={1:'Apple',2:'Ball',3:'Cat',4:'Dog'}
with open("sample1.csv","w") as f1:
    csvrdr=csv.writer(f1)
    for item in d.items():
        csvrdr.writerow(item)
with open("sample1.csv","r") as f1:
    csvrdr=csv.reader(f1)
    for row in csvrdr:
        print(" ".join(row))