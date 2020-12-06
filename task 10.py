#string contains only A-Z,a-z,0-9
import re
s=input("Enter String")
c=re.compile("[A-za-z0-9]+")
if c.fullmatch(s) is not None:
    print("Vaild")
else:
    print("Invaild")
    
#string contains substring 'ab'
s=input("Enter String")
if re.search('ab',s):
    print("yes")
else:
    print("no")
    
#string ends with digit     
s=input("Enter String")
if re.search(r'.\d$',s) is not None:
    print("yes")
else:
    print("no")

#string contains digits on thr postion 1-3
s=input("Enter String")
r=s[1:4]
c=re.compile("[0-9]+")
if c.fullmatch(r) is not None:
    print("yes")
else:
    print("no")

#string contains only Uppercase
s=input("Enter String")
c=re.compile("[A-Z]+")
if c.fullmatch(s) is not None:
    print("yes")
else:
    print("no")
