trials = int(raw_input())
for i in range(trials):
    cuts = int(raw_input())
    if cuts % 2 == 0:
        print pow(cuts/2,2)
    else:
        print cuts/2 * (cuts/2+1)