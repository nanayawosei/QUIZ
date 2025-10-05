import csv
import random


    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

random.shuffle(rows)
selected_rows = rows[:120]


    writer = csv.writer(out)
    writer.writerow(header)
    writer.writerows(selected_rows)
