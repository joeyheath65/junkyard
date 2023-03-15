import random
import collections

results = collections.Counter()
bonus = collections.Counter()

for __ in range(1000000):
    num1 = random.randint(1,35)
    bonus1 = random.randint(1,35)
    results.update([ '%d' % (num1) ])
    bonus.update([ '%d' % (bonus1)])

print()
print('4 most common numbers (1 mil drawings):', results.most_common(4))
print()
print('Most common bonus ball (1 mil drawings):', bonus.most_common(1))

print()
print('4 most common numbers:')
print()
for x in results.most_common(4):
    print('  %s - %d times' % x)
print('')    
