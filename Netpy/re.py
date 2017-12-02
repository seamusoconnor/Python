import re

#print (re.findall('\d{1,5}\s\w+\s\w+\.', 'fslfjlksjfl324 main st.sdjflkdsjkdj'))


#0000-1235-9874
#print (re.findall('\d+''-''\d+''-''\d+', '0000-1235-9874'))

print (re.findall('[0-9a-fA-F]+''-''[0-9a-fA-F]+''-''[0-9A-fA-F]+', '0000-1235-9874'))


REGEX = 'interface ''cts manual sap pmk[0-9]+'
print re.match(REGEX, 'interface eth1/1 cts manual sap pmk123456789')


