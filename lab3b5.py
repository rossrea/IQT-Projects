f = open('lab.txt' , 'r')
data = f.read()
print data

f.close()

f = open('lab.txt' , 'r')
lines = f.readlines()
print lines[0:9]

f.close()

#def main():
    #f = open('lab.txt' , 'a')
    #for i in range(2):
        #f.write("This is a horrible experience %d\r\n" % (i+1))
        
    #f.close()

#if __name__== "__main__":
    #main()

#num_lines = sum(1 for line in open('lab.txt'))
#print num_lines
    
    
f = open('lab.txt' , 'r')
for line in sorted(r):
		print(line, end='')


