# python 3.5
# -----------------------------------------------------------------------------
# Yonatan Carver
# CS 265 - Advanced Programming
# Lab 04
# -----------------------------------------------------------------------------
# Q2.4
# -----------------------------------------------------------------------------

from sys import argv, stdin

lines = []
if len(argv) > 1:
    with open(argv[1], 'r') as f:
        lines = [line.strip() for line in f]
else:
    user_input = stdin.readlines()
    lines = [line.strip() for line in user_input]

ids = []
for i in lines:
    ids.append(int(i.split(' ',1)[0]))

names = []
for i in lines:
    names.append(i.split(' ',1)[1])

entries = dict(zip(ids, names))

for key, value in sorted(entries.items()):
    print(key, value)
