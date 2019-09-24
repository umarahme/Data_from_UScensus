import csv
import pandas as pd

tracts = []
count = 0
with open("/Users/umarahmed/Downloads/Crime_incidents (1).csv") as f:
    reader = csv.reader(f)
    for line in reader:
        if(line[27] != "Block Codes" and line[27] != ""):
            if(line[27][5:12] not in tracts):
                tracts.append(line[27][5:12])
                count += 1
                print(count)
tracts.sort()
print(tracts)
print(count)

blocks = []
newTracts = []
for thing in tracts:
    newTracts.append(thing[0:6])

df = pd.read_csv("/Users/umarahmed/Documents/updatedTotals2008.csv")
df['Tract'] = newTracts
df.to_csv("/Users/umarahmed/Documents/updatedTotals2008.csv")