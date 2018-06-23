from Test import *

x = holder()

print x.adder(1)
print x.destroy(1)
print dir(holder)
print x.subber(55)

c = calc()

print c.plusser(99)
print 'this is the plusser {}'.format(c.plusser(12))
print dir(c)



print('\n\n')
print(1+2)

print(int.__add__(1,2))
print(str.__add__('1','2'))

print(int.__mul__(10,10))

class bob(object):

    def __len(self):
        return 10000000
a = bob()

print('test'.__len__())




