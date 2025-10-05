import csv
import random

with open('data.csv', 'r', encoding='cp1252') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

random.shuffle(rows)
selected_rows = rows[:120]

with open('selected_questions.csv', 'w', encoding='utf-8', newline='') as out:
    writer = csv.writer(out)
    writer.writerow(header)
    writer.writerows(selected_rows)
