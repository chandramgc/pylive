import csv
import json

data = {}
# Change each fieldname to the appropriate field name. I know, so difficult.
fieldnames = ("id", "fieldname1", "fieldname2", "fieldname3")
# spamReader = csv.reader(open('eggs.csv', newline=''), delimiter=' ', quotechar='|')
reader = csv.reader(open('C:/Girish-PC/ROOT/INPUT/sample1.txt', newline='\n'), delimiter=';')
for row in reader:
    print(row)
    id = row[0]
    data[id] = [row[1], row[2], row[3]]
with open('C:/Girish-PC/ROOT/OUTPUT/sample1.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

print(data)
