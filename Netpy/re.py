import re

#print (re.split(r'[a-f][a-f]', 'lscdjdf;lsjfl;sjlks;jf',re.I|re.M))


print (re.findall(r'\d{1,5}\s\w+\s\w+\.', 'fslfjlksjfl324 main st.sdjflkdsjkdj'))