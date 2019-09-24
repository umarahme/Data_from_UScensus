import csv
import urllib.request
import pandas as pd
import json
import time
from datetime import datetime
#Purpose of this code: get FIPS code and extract census block codes from it and add to an existing csv - will have to be
#modified for whatever csv you are adding to or csv you are creating

#I have this in my code so I could see how long it took to get one FIPS code
start_time = time.time()


#NOTE: I have each of the code blocks separated and only ran one at a time and left the rest commented out just in case anything overlapped


#This is the first code block I had to loop through my lat and lons to get the FIPS code
# - Each one takes about .15 seconds to get in my case, and I had 180000ish pairs of lat and lon so it took abt 9hours to run
# count = 0
# with open("/Users/umarahmed/Downloads/Crime_incidents.csv") as f:
#     with open("/Users/umarahmed/Downloads/testing_file.csv", "w") as file:
#         reader = csv.reader(f)
#         writer = csv.writer(file)
#         for line in reader:
#             if(line[12] != "latitude" and line[13] != "longitude"):
#                 lat = line[12]
#                 lon = line[13]
#                 url = "https://geo.fcc.gov/api/census/block/find?latitude="
#                 url = url + lat + "&longitude=" + lon + "&showall=true&format=json"
#                 response = urllib.request.urlopen(url)
#                 content = response.read().decode()
#                 cont = json.loads(content)
#                 code = [cont["Block"]["FIPS"]]
#                 writer.writerow(code)
#                 print("My program took", time.time() - start_time, "to run")
#                 count = count + 1
#                 print(count)
#             else:
#                 print("it not working")




#My code stopped for some reason in the middle and had no idea why,
# so I continued from the spot it left off and put the FIPS codes in a new csv and copy pasted it into the original one
# with open("/Users/umarahmed/Downloads/Crime_incidents.csv") as f:
#     with open("/Users/umarahmed/Downloads/testing_file1.csv", "w") as file:
#
#         writer = csv.writer(file)
#         reader = csv.reader(f)
#
#         count = 1
#
#         for line in reader:
#             if count >= 155795:
#                 lat = line[12]
#                 lon = line[13]
#                 url = "https://geo.fcc.gov/api/census/block/find?latitude="
#                 url = url + lat + "&longitude=" + lon + "&showall=true&format=json"
#                 response = urllib.request.urlopen(url)
#                 content = response.read().decode()
#                 cont = json.loads(content)
#
#                 code = [cont["Block"]["FIPS"]]
#
#                 writer.writerow(code)
#
#                 count = count + 1
#                 print("My program took", time.time() - start_time, "to run")
#                 print(count)
#             else:
#                 count = count + 1





# This code takes the last 4 of each FIPS code (the census block) and makes a new column for it in the csv,
# I used pandas by first putting the last 4 of each in a list and added it as a column (the last 3 lines of this code block
# blockList = []
# with open("/Users/umarahmed/Downloads/testing_file.csv") as f:
#     with open("/Users/umarahmed/Downloads/Crime_incidents.csv", "a") as file:
#         writer = csv.writer(file)
#         reader = csv.reader(f)
#         for line in reader:
#             if(len(line) != 0):
#                 code = line[0][-4:]
#                 blockList.append(code)
#             else:
#                 blockList.append('')
#
# df = pd.read_csv("/Users/umarahmed/Downloads/Crime_incidents.csv")
# df['Block Codes'] = blockList
# df.to_csv("/Users/umarahmed/Downloads/Crime_incidents.csv")



#This code adds the tracts to the csv, its the 6 numbers before the last 4, also used pandas
# blockList = []
# with open("/Users/umarahmed/Downloads/testing_file.csv") as f:
#      with open("/Users/umarahmed/Downloads/Crime_incidents.csv", "a") as file:
#          writer = csv.writer(file)
#          reader = csv.reader(f)
#          for line in reader:
#              if(len(line) != 0):
#                  code = line[0][5:11]
#                  blockList.append(code)
#              else:
#                  blockList.append('')
#
# df = pd.read_csv("/Users/umarahmed/Downloads/Crime_incidents.csv")
# df['Tract'] = blockList
# df.to_csv("/Users/umarahmed/Downloads/Crime_incidents.csv")
#
# print(blockList)


#Corrects the tracts so they are 6 digits (excel did  not include the zeros)
# test = []
# with open("/Users/umarahmed/Downloads/Crime_incidents.csv") as f:
#     with open("/Users/umarahmed/Downloads/New_Tracts.csv", "w") as file:
#         reader = csv.reader(f)
#         writer = csv.writer(file)
#         for line in reader:
#             if(len(line[29])!= 0 and len(line[29])<6 and line[29] != "Tract"):
#                 tract = line[29]
#                 length = len(line[29])
#                 zeros = 6 - length
#                 for i in range(zeros):
#                     tract = '0' + tract
#                     print(tract)
#                 writer.writerow([tract])
#                 test.append(tract)
#             elif(line[29]=="Tract"):
#                 writer.writerow([line[29]])
#             else:
#                 writer.writerow("")
#                 test.append("")




#creates new year csv, ignore the "hello" being written
#change year to create new year file
# with open("/Users/umarahmed/Documents/updatedTotals2008.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["hello"])



#make block column for totals file
# for thing in tracts:
#     blocks.append(thing[6])
# df = pd.read_csv("/Users/umarahmed/Downloads/updatedTotals.csv")
# df['Tract/Census Block'] = tracts
# df.to_csv("/Users/umarahmed/Downloads/updatedTotals.csv")

#adding tracts and blocks column to new file, array made did not have title at head so added one
# tracts.insert(0,"Tract")


#add good tracts to a diff csv so can copy paste them, no need to run code again
# newTracts.insert(0,"Tract")
# with open("/Users/umarahmed/Downloads/goodTracts.csv", "w") as file:
#     writer = csv.writer(file)
#     for thing in newTracts:
#         writer.writerow([thing])

#add tracts to tract column
# df = pd.read_csv("/Users/umarahmed/Downloads/finalTotals.csv")
# df['Tract'] = tracts
# df.to_csv("/Users/umarahmed/Downloads/finalTotals.csv")


# rape = []
# crimeCount = 0
# count = 0

# with open("/Users/umarahmed/Downloads/Crime_incidents (1).csv") as f:
#     with open("/Users/umarahmed/Downloads/updatedTotals.csv") as file:
#         reader = csv.reader(f)
#         reader2 = csv.reader(file)
#         for line in reader2:
#             if(line[0] != "Tract/Census Block"):
#                 for line2 in reader:
#                     count += 1
#                     if line[0] == line2[27][5:12]:
#                         if line2[4] == "ASSAULT":
#                             crimeCount += 1
#                 value = crimeCount
#                 rape.append(value)
#                 crimeCount = 0

# ALSO THIS ONE

# count = 0
# crimeCount = 0
# rape = []
# with open("/Users/umarahmed/Downloads/updatedTotals2019.csv") as f:
#     with open("/Users/umarahmed/Downloads/Crime_incidents (1).csv") as file:
#         reader = csv.reader(f)
#         reader2 = csv.reader(file)
#         for line in reader:
#             print(count)
#             if(line[0] != "Tract"):
#                 file.seek(0,0)
#                 for line2 in reader2:
#                     count += 1
#                     if line[0] == line2[27][5:11]:
#                         print(line[1])
#                         print(line2[27][12:14])
#                         if line[1] == line2[27][12:14]:
#                             if "2019" in line2[3]:
#                                 if line2[4] == "ROBBERY":
#                                     crimeCount += 1
#                                 elif line2[4] == "Robbery":
#                                     crimeCount += 1
#                 value = crimeCount
#                 rape.append(value)
#                 crimeCount = 0
#                 print(rape)
#
# df = pd.read_csv("/Users/umarahmed/Downloads/updatedTotals2019.csv")
# df['ROBBERY'] = rape
# df.to_csv("/Users/umarahmed/Downloads/updatedTotals2019.csv")


#checks if correct year and adds to array to add to year file based category of crime
#this code must be modified based on what column needs to be made, see end of script for list of crime categories
#also adds tracts to separate array
years = []
tracts = []
crime = []
items = {}
with open("/Users/umarahmed/Downloads/Crime_incidents (1).csv") as file:
    reader = csv.reader(file)
    for line in reader:
        if "2008" in line[3]:
            if "UUV" in line[4]:
                items.update({line[27][5:12]: (line[3], line[4])})
                years.append(line[3])
                tracts.append(line[27][5:12])
            # elif "CRIM NEGLIGENT HOMICIDE" in line[4]:
            #     items.update({line[27][5:12]: (line[3], line[4])})
            #     years.append(line[3])
            #     tracts.append(line[27][5:12])
        elif "/08 " in line[3]:
            if "UUV" in line[4]:
                items.update({line[27][5:12]: (line[3], line[4])})
                years.append(line[3])
                tracts.append(line[27][5:12])
            # elif "CRIM NEGLIGENT HOMICIDE" in line[4]:
            #     items.update({line[27][5:12]: (line[3], line[4])})
            #     years.append(line[3])
            #     tracts.append(line[27][5:12])


#print(len(years))
#sort tracts so in order to match crimes
tracts.sort()
#print(len(tracts))


#add specific crimeCount to its respective column
tc = []
#print(len(items))
for key in items:
    tc.append(key)
count = 0
crimeCount = []
with open("/Users/umarahmed/Documents/updatedTotals2008.csv") as f:
    reader = csv.reader(f)
    for line in reader:
        if line[16] != "Tract":
            if line[17] != "Block":
                for key in tracts:
                    if key == line[16]+line[17]:
                        count += 1
                value = count
                crimeCount.append(value)
                count = 0
print(crimeCount)

df = pd.read_csv("/Users/umarahmed/Documents/updatedTotals2008.csv")
df['UUV'] = crimeCount
df.to_csv("/Users/umarahmed/Documents/updatedTotals2008.csv")


# "THEFT" "Theft"
# "ROBBERY" "Robbery"
# "BURGLARY" "Breaking & Entering"
# "ASSAULT" "Assault"
# "MURDER" "Homicide"
# "SEXUAL ABUSE" "Other Sexual Offense"
# "MANSLAUGHTER" "CRIM NEGLIGENT HOMICIDE"
# "RAPE"
# "UUV"

#BURGLARY
#LARCENY/THEFT
#UUV
#ASSAULT
#ROBBERY
#RAPE
#MURDER
# CRIM NEGLIGENT HOMICIDE
# SEXUAL ABUSE
# THEFT OF SERVICES

#crim negligent homicide and Manslaughter - done

#burglary and Breaking and entering - DONE

#robbery - DONE

#larceny/theft and theft of services - DONE

#Assault - DONE

#homicide and murder - DONE

#Sexual Abuse/Offense - DONE

#uuv - DONE

#rape - DONE

#make new years w/this one
# with open("/Users/umarahmed/Downloads/updatedTotals2019.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["1"])



