import csv
import random

with open('data.csv', 'r', encoding='latin-1') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

random.shuffle(rows)
selected_rows = rows[:120]

with open('selected_questions.csv', 'w', encoding='latin-1', newline='') as out:
    writer = csv.writer(out)
    writer.writerow(header)
    writer.writerows(selected_rows)
