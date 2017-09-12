#https://docs.python.org/2/library/xml.etree.elementtree.html

import json
import xml.etree.ElementTree as ET
import re
import sys
from datetime import datetime

start=datetime.now()

tree = ET.parse('Hepnames.xml')
root = tree.getroot()

#print tag of root directory (<collection>)
#print root.tag

#for child in root:
#    print child.tag, child.attrib

print("UG: ")

uni_codes =[]
for record in root.findall('record'):
    for datafield in record.findall("datafield"):
        if datafield.attrib["tag"] == "371":
            for subfield in datafield.findall("subfield"):
                if subfield.text=="UG":
                    try:
                    #if datafield.find('.//subfield[@code="a"]') is not None:
                        right_field=datafield.find('.//subfield[@code="z"]')
                        uni_code = right_field.text
                        uni_codes.append(uni_code)
                    except AttributeError:
                        continue

print("number of researchers providing UG: ", len(uni_codes))

total_number_researchers=0
for record in root.findall('record'):
    total_number_researchers +=1

print("total number researchers: ",total_number_researchers)

percent_researchers= float(len(uni_codes))/float(total_number_researchers)
print(percent_researchers,"percent of researchers provided UG")

print("universities researchers come from: ", len(set(uni_codes)))


with open('countries_dict.json') as json_data:
    countries_dict = json.load(json_data)

#countries.encode("utf-8") automatic woth python3
#print(countries_dict)
#print(type(countries_dict))

counts={}
total=0
missed = []
for code in uni_codes:
    stop=False
    while stop==False:
        flag = True
        for key, items in countries_dict.items():
            if code in items:
                flag=False
                if key in counts:
                    counts[key]+=1
                else:
                    counts[key]=1
                total +=1
                stop=True
        if flag==True:
            missed.append(code)
            stop=True

print("Missed: ", set(missed))
print("Researchers searched: ", len(uni_codes))
print("Researchers identified: ", total)

#merge countries

for item in counts:
    if item == "gujarat, india":
        counts["india"]+=counts[item]
    if item == "korea":
        counts["south korea"]+=counts[item]
    if item == "p.r. china":
        counts["china"]+=counts[item]
    if item == "p.r.china":
        counts["china"]+=counts[item]
    if item == "republic of south africa":
        counts["south africa"]+=counts[item]
    if item == "slovak republic":
        counts["slovakia"]+=counts[item]
    if item == "serbia":
        counts["serbia and montenegro"]+=counts[item]
    
unwanted=["gujarat, india","korea","p.r. china","p.r.china","republic of south africa","slovak republic","serbia"]
for items in unwanted:
    try:
        del counts[items]
    except Exception:
        continue
    
    

with open('UG_results.json', 'w') as fp:
    json.dump(counts, fp, sort_keys=True,ensure_ascii=False)



print("PHD: ")

uni_codes_PHD =[]
for record in root.findall('record'):
    for datafield in record.findall("datafield"):
        if datafield.attrib["tag"] == "371":
            for subfield in datafield.findall("subfield"):
                if subfield.text=="PHD":
                    try:
                        right_field=datafield.find('.//subfield[@code="z"]')
                        uni_code = right_field.text
                        uni_codes_PHD.append(uni_code)
                    except AttributeError:
                        continue

print("number of researchers providing PHD: ", len(uni_codes_PHD))

total_number_researchers=0
for record in root.findall('record'):
    total_number_researchers +=1

print("total number researchers: ",total_number_researchers)

percent_researchers= float(len(uni_codes_PHD))/float(total_number_researchers)
print(percent_researchers,"percent of researchers provided PHD")

print("universities researchers come from: ", len(set(uni_codes_PHD)))


#countries.encode("utf-8") automatic woth python3
#print(countries_dict)
#print(type(countries_dict))

counts={}
total=0
missed = []
for code in uni_codes_PHD:
    stop=False
    while stop==False:
        flag = True
        for key, items in countries_dict.items():
            if code in items:
                flag=False
                if key in counts:
                    counts[key]+=1
                else:
                    counts[key]=1
                total +=1
                stop=True
        if flag==True:
            missed.append(code)
            stop=True

print("Missed: ", set(missed))
print("Researchers searched: ", len(uni_codes_PHD))
print("Researchers identified: ", total)

for item in counts:
    if item == "gujarat, india":
        counts["india"]+=counts[item]
    if item == "korea":
        counts["south korea"]+=counts[item]
    if item == "p.r. china":
        counts["china"]+=counts[item]
    if item == "p.r.china":
        counts["china"]+=counts[item]
    if item == "republic of south africa":
        counts["south africa"]+=counts[item]
    if item == "slovak republic":
        counts["slovakia"]+=counts[item]
    if item == "serbia":
        counts["serbia and montenegro"]+=counts[item]
    
unwanted=["gujarat, india","korea","p.r. china","p.r.china","republic of south africa","slovak republic","serbia"]
for items in unwanted:
    try:
      del counts[items]
    except Exception:
        continue


with open('PHD_results.json', 'w') as fp:
    json.dump(counts, fp, sort_keys=True,ensure_ascii=False)


print("Time taken: ", datetime.now()-start)
