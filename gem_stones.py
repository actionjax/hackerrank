gems = int(raw_input())
elements = set(raw_input())
for i in range(gems-1):
    elements = elements.intersection(set(raw_input()))
print len(elements)