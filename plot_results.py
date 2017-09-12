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
target_countries=["italy","france","united kingdom","germany","netherlands","spain","finland","hungary","norway","ireland","switzerland","portugal","sweden", "greece", "austria", "slovenia"]

target_countries=["latvia","lithuania","bosnia-herzegovina","czech republic","italy","france","united kingdom","argentina","colombia","germany","netherlands","russia","pakistan","spain","finland","israel","south africa","mexico","russia","belgium","hungary","pakistan","cuba","chile","norway","ireland","denmark","switzerland","portugal","sweden","usa","canada","greece","iran","south korea","japan","india","china", "austria", "turkey", "australia", "iceland", "new zealand", "serbia and montenegro", "slovenia", "croatia", "poland", "romania","slovakia", "armenia", "ukraine", "brazil", "thailand", "vietnam"]

target_countries=["italy","france","united kingdom","argentina","germany","netherlands","spain","finland","israel","south africa","russia","belgium","hungary","russia","cuba","chile","norway","ireland","denmark","switzerland","portugal","sweden","usa","canada","greece","iran","south korea","japan","india","china", "austria", "turkey", "australia", "new zealand", "poland", "ukraine", "brazil"]


#replace ug_results with phd_results in here in order to plot the two
target_dict={}
for country in target_countries:
    count=ug_results[country]
    target_dict[country]=count

#data from www.wordmeters.info

with open('demographics.json') as json_data:
    demographics = json.load(json_data)


#we adjust for the fact that only 11.84% of researchers have provided information about their UG
#coefficient_dict includes number of researchers every 100000 inhabitants
#for phd this is 0.2834
coefficient_dict={}
for key, item in target_dict.items():
    coefficient=float(item)/float(demographics[key])*1/0.1184*1000000
    #coefficient=float("{0:.2f}".format(coefficient))
    coefficient_dict[key]=coefficient

capitals = {}
for key, value in coefficient_dict.items():
    key=key.title()
    capitals[key] = value
coefficient_dict = capitals


sorted_coefficients = sorted(coefficient_dict.items(), key=lambda value: value[1],reverse=True)

#print(sorted_coefficients)
coefficient_array=np.array(sorted_coefficients)


#print(coefficient_array)


plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')


import brewer2mpl
bmap = brewer2mpl.get_map('Set3','qualitative',8 ,reverse=True)
colors = bmap.mpl_colors



y=coefficient_array[:,1]
x=np.arange(len(y))

plt.bar(x,y,color=colors,alpha=0.6)
plt.ylabel("Titles / 1 million inhabitants")

plt.xticks(x + 0.4, coefficient_array[:,0], rotation="vertical")
plt.tight_layout()
plt.suptitle("Inspire data mining: UG Selected World", fontsize=36, fontweight='bold')
#plt.subplots_adjust(left=0, bottom=0.5, right=0.1, top=0.6, wspace=0, hspace=0)
plt.matplotlib.rcParams.update({'font.size': 34})
plt.show()
#plt.savefig("test.png",bbox_inches='tight')




