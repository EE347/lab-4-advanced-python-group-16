import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

ys_dict = {}
xs = []
xlabel = None
header = None

with open("task9.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    header = reader.__next__()

    xlabel = header[0]
    
    for label in header[1:]:
        ys_dict[label] = []
    
    for row in reader:
        date = datetime.strptime(row[0], "%d/%m/%Y")
        xs.append(date)

        for i in range(1,len(header)):
            ys_dict[header[i]].append(float(row[i]))

color_dict = {"META":"b","AAPL":"gray","AMZN":"black","NFLX":"r","NVDA":"g","GOOGL":"orange"}


[plt.plot(xs, y_line, color=color_dict[label]) for label, y_line in ys_dict.items()]
plt.title("FAANNG Performance")
plt.xlabel("Date")
plt.ylabel("Price (USD)")

labels = [label + ": +" + str(
    round((ys_dict[label][-1]/ys_dict[label][0])*100,2)
    ) + "%"
    for label in header[1:]]

plt.legend(labels)
plt.show()
