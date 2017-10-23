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

james = sorted(set([sanitize(each_t) for each_t in james]))
julie = sorted(set([sanitize(each_t) for each_t in julie]))
mikey = sorted(set([sanitize(each_t) for each_t in mikey]))
sarah = sorted(set([sanitize(each_t) for each_t in sarah]))

print(james[:3])
print(julie[:3])
print(mikey[:3])
print(sarah[:3])
        
        
        
