#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p "python3.withPackages (ps: [])"

import sys
from itertools import chain
from functools import reduce
height = 323
width = 31

dx = 3
dy = 1
trees = list(chain.from_iterable([[(x, y) for (x, ch) in enumerate(xs) if ch == '#'] for (y, xs) in enumerate(sys.stdin.readlines())]))

positions = lambda dx, dy: [((s*dx)%width, y%height) for (s, y) in enumerate(range(0, height, dy))]

print(len(set(positions(dx, dy)).intersection(set(trees))))

print(reduce(lambda x, y: x*y, [len(set(positions(dx, dy)).intersection(set(trees))) for (dx, dy) in [(1,1), (3,1), (5,1), (7,1), (1,2)]], 1))
