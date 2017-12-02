import re

output = """seamusconnor@gmail.com, 5 Springlawn Drive, Dublin 15
barryohanlon@gmail.com, 5 summerfield Drive, Dublin 13"""

regex = (re.findall("\w+\@\w+", output))

print '\n'
print regex[0]
print '\n'
print regex[1]
print '\n'
