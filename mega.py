import random
import collections

results = collections.Counter()
mega = collections.Counter()

for __ in range(1000000):
    num1 = random.randint(1,70)
    mega1 = random.randint(1,25)
    results.update([ '%d' % (num1) ])
    mega.update([ '%d' % (mega1)])

print()
print('5 most common numbers (1 mil drawings):', results.most_common(5))
print
print('Most common Megaplier (1 mil drawings):', mega.most_common(1))

print()
print('5 most common numbers:')
print()
for x in results.most_common(5):
    print('  %s - %d times' % x)
print('')    

