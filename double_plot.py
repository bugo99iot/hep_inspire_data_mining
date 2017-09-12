import json
import xml.etree.ElementTree as ET
import plotly.plotly as py
import matplotlib.pyplot as plt
import re
import sys
from datetime import datetime
import numpy as np


with open('PHD_results.json') as json_data:
    phd_results = json.load(json_data)

with open('UG_results.json') as json_data:
    ug_results = json.load(json_data)


#selected europe
target_countries=["italy","france","united kingdom","germany","netherlands","spain","finland","hungary","ireland","switzerland","portugal","sweden", "greece", "austria"]


#data from www.wordmeters.info
with open('demographics.json') as json_data:
    demographics = json.load(json_data)


target_dict={}
for country in target_countries:
    count=ug_results[country]
    target_dict[country]=count


#we adjust for the fact that only 11.84% of researchers have provided information about their UG
#coefficient_dict includes number of researchers every 1000 inhabitants
#for phd this is 0.2834
total_coeff_UG =0
coefficient_dict={}
for key, item in target_dict.items():
    coefficient=float(item)/float(demographics[key])*1/0.1184*1000000
    coefficient=float("{0:.2f}".format(coefficient))
    total_coeff_UG += coefficient 
    coefficient_dict[key]=coefficient

percentage_dict_UG = {}
for key, item in coefficient_dict.items():
    percentage = float(item)*100/total_coeff_UG
    percentage_dict_UG[key]=percentage

print(percentage_dict_UG)
    

capitals = {}
for key, value in percentage_dict_UG.items():
    key=key.title()
    capitals[key] = value
percentage_dict_UG = capitals




target_dict={}
for country in target_countries:
    count=phd_results[country]
    target_dict[country]=count

total_coeff_PHD =0
coefficient_dict={}
for key, item in target_dict.items():
    coefficient=float(item)/float(demographics[key])*1/0.2834*1000000
    coefficient=float("{0:.2f}".format(coefficient))
    total_coeff_PHD += coefficient 
    coefficient_dict[key]=coefficient

percentage_dict_PHD = {}
for key, item in coefficient_dict.items():
    percentage = float(item)*100/total_coeff_PHD
    percentage_dict_PHD[key]=percentage

print(percentage_dict_PHD)

capitals = {}
for key, value in percentage_dict_PHD.items():
    key=key.title()
    capitals[key] = value
percentage_dict_PHD = capitals

sorted_coefficients = sorted(percentage_dict_PHD.items(), key=lambda value: value[1],reverse=True)

ordered_list = []
for tupla in sorted_coefficients:
    country = tupla[0]
    ordered_list.append(country)

print(ordered_list)

ordered_PHD=[]
for item in ordered_list:
    percent = percentage_dict_PHD[item]
    ordered_PHD.append([item,percent])

ordered_UG=[]
for item in ordered_list:
    percent = percentage_dict_UG[item]
    ordered_UG.append([item,percent])

print(ordered_PHD)
print(ordered_UG)

PHD_array = np.array(ordered_PHD)
UG_array = np.array(ordered_UG)

y1=PHD_array[:,1]
y2=UG_array[:,1]
x=np.arange(len(y1))

plt.style.use('fivethirtyeight')
width = 0.40

fig, ax = plt.subplots()
rects1 = ax.bar(x, y1, width, color='b', alpha = 0.6, label="% of PHD")
rects2 = ax.bar(x + width, y2, width, color='r', alpha = 0.45, label="% of UG")
plt.xticks(x + 0.4, PHD_array[:,0], rotation='vertical')
plt.ylabel("% of titles compared to the total")
plt.legend(loc='upper right')
plt.tight_layout()
plt.suptitle("Inspire data mining: PHD and UG as a percentage, Europe", fontsize=36, fontweight='bold')
#plt.subplots_adjust(left=0, bottom=0.5, right=0.1, top=0.6, wspace=0, hspace=0)
plt.matplotlib.rcParams.update({'font.size': 34})
plt.show()

sys.exit()



#sorted_coefficients = sorted(percentage_dict_UG.items(), key=lambda value: value[1],reverse=True)

#print(sorted_coefficients)
coefficient_array=np.array(sorted_coefficients)


print(coefficient_array)


plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')


import brewer2mpl
bmap = brewer2mpl.get_map('Set1','qualitative',9 ,reverse=True)
colors = bmap.mpl_colors



y=coefficient_array[:,1]
x=np.arange(len(y))

plt.bar(x,y,color=colors,alpha=0.6)
plt.ylabel("Titles / 1000 inhabitants")

plt.xticks(x + 0.4, coefficient_array[:,0], rotation='vertical')
plt.tight_layout()
plt.suptitle("Inspire data mining: UG Europe", fontsize=36, fontweight='bold')
#plt.subplots_adjust(left=0, bottom=0.5, right=0.1, top=0.6, wspace=0, hspace=0)
plt.matplotlib.rcParams.update({'font.size': 34})
plt.show()
#plt.savefig("test.png",bbox_inches='tight')




