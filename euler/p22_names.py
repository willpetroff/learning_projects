"""

"""
import csv
doc_path = ".\\files\\p22_names.txt"

names = []
total = 0
with open(doc_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        names = sorted(line)

for name in range(len(names)):
    name_total = 0
    for char in names[name]:
        name_total += (ord(char) - 64)
    total += name_total * (name + 1)

print(total)