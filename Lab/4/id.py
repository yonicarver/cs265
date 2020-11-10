from sys import argv
import collections

with open(argv[1], 'r') as f:
    lines = [line.strip() for line in f]


ids = []
for i in lines:
    ids.append(int(i.split(' ',1)[0]))

names = []
for i in lines:
    names.append(i.split(' ',1)[1])

entries = dict(zip(ids, names))
print(entries)
#int_entries = {int(k) : v for k, v in entries.items()}
#print(sorted(entries))

for key, value in sorted(entries.items()):
    print(key, value)

od = collections.OrderedDict(sorted(entries.items()))
#for k, v in od.items(): print(k, v)
