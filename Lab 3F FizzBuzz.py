for i in xrange(1, 100):
    if i % 3 == 0:
        print "{} Fizz".format(i)
        continue
for i in xrange(1, 100):
    if i % 5 == 0:
        print "{} Buzz".format(i)
        continue
for i in xrange(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        print "{} FizzBuzz".format(i)
        continue
    print i
  

