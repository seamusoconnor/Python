import pprint

dic = {'name':'seamus','age':'40', 'occupation':'bobby'}


print dic
print '\n'


dic.update({'work':'yes'})

print dic

del dic['work']

print '\n'
print dic


dic['a'] = 'b'

print '\n'
print dic

print len(dic)


print dic.get('name')
print dic['name']



for key, val in dic.items():
    print key, '->', val


pprint.pprint(dic)

print dic

