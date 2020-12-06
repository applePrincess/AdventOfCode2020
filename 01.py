#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p "python3.withPackages (ps: [])"
import sys
nums = [int(x) for x in sys.stdin.readlines()]

flg = None
for i in nums:
    for j in nums:
        if i + j == 2020:
            flg = i*j
            break
    if not (flg == None):
        break

print("Not found" if flg == None else flg)


flg2 = None
for i in nums:
    for j in nums:
        for k in nums:
            if i + j + k == 2020:
                flg2 = i*j*k
                break
        if not (flg2 == None):
            break
    if not (flg2 == None):
        break

print("Not found" if flg2 == None else flg2)
