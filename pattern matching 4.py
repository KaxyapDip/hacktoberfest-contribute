import re

#matching multiple group with pipe

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
o = batRegex.search( 'Batman dead, Batmobile')
mo = batRegex.search( 'Batmobile got damaged, batman dead')
print(o.group())
print(mo.group())

#optional matching with the question mark

batRegex2 = re.compile(r'Bat(wo)?man')
mo2 = batRegex2.search('the adventure of Batman')
print(mo2.group())
mo3 = batRegex2.search('the adventure of Batwoman')
print(mo3.group())

# with integer

numFormat = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = numFormat.search(' his phone number is 415-123-4353')
print(mo4.group())
mo5 = numFormat.search(' his phone number is 123-4353')
print(mo5.group())

#matching zero or more with a star 
# The * or asterisk means "match zero or more"

batRegex3 = re.compile(r'Bat(wo)*man')
mo6 = batRegex3.search('the adventure of Batwowowoman')
print(mo6.group())

mo7 = batRegex3.search('the adventure of Batman')
print(mo7.group())

# matching one or more with a plus 
# the + or plus means "match one or more" 

batRegex4 = re.compile(r'Bat(wo)+man')
mo7 = batRegex4.search('the adventure of Batwoman')
print(mo7.group())
mo8 = batRegex4.search('the adventure of Batwoman')
print(bool(mo8 == None))
mo8 = batRegex4.search('the adventure of Batman')
print(bool(mo8 == None))