import random
import collections

results = collections.Counter()
pb = collections.Counter()

for __ in range(1000000):
    num1 = random.randint(1,69)
    pb1 = random.randint(1,29)
    results.update([ '%d' % (num1) ])
    pb.update([ '%d' % (pb1)])

print()
print('5 most common numbers (1 mil drawings):', results.most_common(5))
print
print('Most common Megaplier (1 mil drawings):', pb.most_common(1))

print()
print('5 most common numbers:')
print()
for x in results.most_common(5):
    print('  %s - %d times' % x)
print('')    

