n = open("opt1.txt","r")  # open file, read-only
s = open("opt2.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()