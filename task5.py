import csv

names = []
last_input = input("Enter a name: ")

while last_input != "quit":
    names.append(last_input)
    last_input = input("Enter a name: ")

with open("task5.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    [writer.writerow([name]) for name in names]
    
with open("task5.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row[0]) # index the first element of the row (name) 