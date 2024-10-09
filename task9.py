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

y_lines = ys_dict.values()

[plt.plot(xs, y_line) for y_line in y_lines]

plt.show()
