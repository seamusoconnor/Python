file = open("run.txt", "w")
read = file.read()

lines = read.strip()
z = 0

for a in lines:
    if not a == "l":
        continue
    else:
        z +=1

wr = "We have %d occurences of l" %z

print wr

file.write()
file.close()



