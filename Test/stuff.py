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