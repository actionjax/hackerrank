nt = raw_input().split(" ")
width = raw_input().split(" ")
for x in xrange(int(nt[1])):
    ij = raw_input().split(" ")
    answer = 3
    for y in range(int(ij[0]),int(ij[1])+1):
        if int(width[y]) < answer:
            answer = int(width[y])
    print answer
        
