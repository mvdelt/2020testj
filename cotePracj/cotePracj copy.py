import collections

p = ['mislav', 'stanko', 'mislav', 'ana', 'mislav']
c = ['stanko', 'ana', 'mislav']

print(collections.Counter(p))
# Counter({'mislav': 2, 'stanko': 1, 'ana': 1})

print(collections.Counter(c))
# Counter({'stanko': 1, 'ana': 1, 'mislav': 1})

print(collections.Counter(p) - collections.Counter(c))
print(list((collections.Counter(p) - collections.Counter(c)).keys())[0])  # 'mislav'