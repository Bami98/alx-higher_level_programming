#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if not chr(a) == 'q' or chr(a) == 'e':
        print('{:c}'.format(a), end="")
