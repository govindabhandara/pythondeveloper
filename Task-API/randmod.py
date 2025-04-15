
import random
print(random.random())
print(random.uniform(1,10))

import random
colors=['red','brown','white']
print(random.choice(colors))
print(random.randint(1,10))

import random
deck=list(range(1,50))
random.shuffle(deck)
print(deck[:5])

import random
# Weighted random choices (Python 3.6+)
from random import choices
population = ['win', 'lose', 'draw']
weights = [0.5, 0.4, 0.1]
print(choices(population, weights, k=10))

# Random bytes
print(random.randbytes(4))  # Python 3.9+