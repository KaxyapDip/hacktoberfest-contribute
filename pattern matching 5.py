import re

# Matching specific repetation with curly brackes

#(ha){3} = (ha)(ha)(ha)
#(ha){3,5} =  (ha)(ha)(ha) \ (ha)(ha)(ha)(ha)| (ha)(ha)(ha)(ha)(ha)

haRegex = re.compile(r'(Ha ){3}')
mo1 = haRegex.search('Ha Ha Ha Ha')
print(mo1.group())
print(bool(mo1 == None))
haRegex2 = re.compile(r'(Ha){2,5}')
mo2 = haRegex2.search('HaHaHaHaHaHa')
print('Greedy : ' + mo2.group())


# Greedy and Nongreedy Matching

# python expression are greedy by default

haRegex3 = re.compile(r'(Ha){3,5}?')
mo3 = haRegex3.search('HaHaHaHaHa')
print('Non Greedy : ' + mo3.group()) 
