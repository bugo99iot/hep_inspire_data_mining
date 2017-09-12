#https://docs.python.org/2/library/xml.etree.elementtree.html

import json
import xml.etree.ElementTree as ET
import re
import sys
from datetime import datetime

start=datetime.now()

tree = ET.parse('Institutions-records.xml')
root = tree.getroot()

#sent="Istanbul, Turkey"
#losent = sent.lower()
#print(losent)

#print(re.search("turkey", losent) is None)


with open('all_countries_list.json') as json_data:
    all_countries_list = json.load(json_data)


total_records=0

missed = []
dictionary = {}
for record in root.findall('record'):
    total_records+=1
    stop = False
    flag=True
    while stop==False:  
        for controlfield in record.findall("controlfield"):
            if controlfield.attrib["tag"] == "001":
                code=controlfield.text
        for datafield in record.findall("datafield"):
            if datafield.attrib["tag"] == "371":
                for subfield in datafield.findall("subfield"):                
                        if subfield.attrib["code"]=="d":
                            country = subfield.text.lower()
                            if country in all_countries_list:
                                flag=False
                                #print(country)
                                #print(code)
                                if country not in dictionary:
                                    dictionary[country]=[str(code)]
                                    stop=True
                                else:
                                    dictionary[country].append(str(code))
                                    stop=True
        flag2 = False
        if flag==True:
            for datafield in record.findall("datafield"):
                if datafield.attrib["tag"] == "371":
                    for subfield in datafield.findall("subfield"): 
                        for country in all_countries_list:
                            subfield_text=subfield.text.lower()
                            if country in subfield_text:
                                flag2=True
                                if country not in dictionary:
                                    dictionary[country]=[str(code)]
                                    stop=True
                                else:
                                    dictionary[country].append(str(code))
                                    stop=True
            if flag2==False:
                missed.append(code)
                stop=True
unique_dict = {}
for key, item in dictionary.items():
    item=list(set(item))
    unique_dict[key]=item
dictionary=unique_dict
    
        
#print(missed)

"""for item in all_countries_raw:
    regex=re.compile(item)
    sentence = "Istanbul, Turkey"
    senlo=sentence.lower()
    if regex.search(sentence) is not None:
        print("BINGO! It works!")"""
    

print(len(missed)," institutes were missed")
print("out of: ",total_records)
                    
print("Time taken: ", datetime.now()-start)        


with open('countries_dict.json', 'w') as fp:
    json.dump(dictionary, fp, sort_keys=True,ensure_ascii=False)



#with open('countries.json') as json_data:
#    countries = json.load(json_data)

"""
                for subfield in datafield.findall("subfield"):
                    if subfield.text=="UG":
                        try:
                            right_field=datafield.find('.//subfield[@code="a"]')
                            uni = right_field.text.lower()
                            universities.append(uni)
                        except AttributeError:
                               continue
"""

"""for record in root.findall('record'):
        for datafield in record.findall("datafield"):
            if datafield.attrib["tag"] == "371":
                for subfield in datafield.findall("subfield"):
                    if subfield.text=="UG":
                        try:
                        #if datafield.find('.//subfield[@code="a"]') is not None:
                            right_field=datafield.find('.//subfield[@code="a"]')
                            uni = right_field.text.lower()
                            universities.append(uni)
                        except AttributeError:
                               continue"""




