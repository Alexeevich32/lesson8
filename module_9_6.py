import itertools


def all_v1(text):
    for i in range(len(text)):
      combinations = []
      combinations = itertools.combinations(text, i + 1)
      subsequences = [''.join(c) for c in combinations]
      declimer = f'\n'
      res = declimer.join(subsequences)
      yield res






a = all_v1(text = 'abc')
print(a)
for i in a:
    print(i)