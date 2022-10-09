
# the Findal Method
# while search() return the first match object , the findal()  method will return the string of every match object
# it has no group
import re

phoneNoRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # it has no group
mo1 = phoneNoRegex.findall('cell: 321-423-4211, work : 432-324-5433')
print(mo1)

phoneNoRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #it has group
mo2 = phoneNoRegex2.findall('cell: 342-3244-2344, work : 533-634-5342')
print(mo2)

# whenm there are no group findall return a list of matched string
# when there are group , findall returns  list of tuples of group