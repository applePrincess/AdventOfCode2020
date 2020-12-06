#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p "python3.withPackages (ps: [])"

import sys,re

r = '([0-9]+)-([0-9]+)\s+([a-z]):\s+(\w+)'
cnt = 0
# for st in sys.stdin.readlines():
#    mi, ma, ch, s = re.findall(r, st)[0]
#    cn = len(re.findall(ch, s))
#    if int(mi) <= cn and cn <= int(ma):
#        cnt += 1
# print(cnt)


for st in sys.stdin.readlines():
    ca1, ca2, ch, s = re.findall(r, st)[0]
    if (s[int(ca1)-1] == ch) ^ (s[int(ca2)-1] == ch):
        cnt += 1
print(cnt)
