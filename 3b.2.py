file = open('lab.txt', 'rw+')
print("Number of the line: "),file.name
line = file.readline()
print "Read Line: %s" % (line)
line = file.readline(5)
print "Read Line: %s" % (line)
file.close()
