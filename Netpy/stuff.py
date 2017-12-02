import re
import datetime

#age = input('Enter your age and I\'ll tell you what year it will be once you reach 100 > ')

now = datetime.datetime.now()
nows = '20175555'
regex = '2017'
if re.findall('2017', nows):
    print True
else:
    print False

