t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())
    height = 1
    if n == 0:
        print height
    else:
        for j in xrange(n):
            if j % 2 == 0:
                height = height * 2
            else:
                height = height + 1
               
        print height
