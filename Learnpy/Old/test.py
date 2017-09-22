import os
os.system("clear")

for bottles in range(20, 0, -1):
    print "%d bottles of beer on the wall, %d bottles of beer, take one down pass it around" % (bottles, bottles)
    print bottles -1, "bottles of beer on the wall"
