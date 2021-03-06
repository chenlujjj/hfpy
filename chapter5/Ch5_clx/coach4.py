from sanitize import *

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

james = sorted([sanitize(each_t) for each_t in james])
julie = sorted([sanitize(each_t) for each_t in julie])
mikey = sorted([sanitize(each_t) for each_t in mikey])
sarah = sorted([sanitize(each_t) for each_t in sarah])

unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)

unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
        
unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)

unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)

print(unique_james[:3])
print(unique_julie[:3])
print(unique_mikey[:3])
print(unique_sarah[:3])
        
        
        
