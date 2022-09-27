import csv
file = open("email.csv")
csvreader = csv.reader(file)
rows = []
count = 0
for row in csvreader:
    if len(row[0]) > 0:
        rows.append(row[0])
    else:
        continue

for i in rows:
    print(i)
#     if '@' in i:
#         count += 1


# print(rows)
# print(len(rows), count)