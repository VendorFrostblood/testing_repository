# -*- coding: utf-8 -*-
###VF
import random


def check_input(chk):
    if len(chk) == 2 and isinstance(chk[0], int) and isinstance(chk[1], int):
        if chk[0] < chk[1]:
            return True
        else:
            return False
    else:
        return False


def get_ladder(lad_start, lad_end, lad_random):
    a = []
    b = []
    fin = ""
    for i in range(lad_random, lad_end+1):   ## From here and on to line 26 is a bit of magic dust, or as a normal person would call it: "what the..."
        a.append('*' * (i))
    for i in range(lad_start, lad_random+1):
        b.append('*' * (i))
    a = a[::-1]
    for j in b:
        a.append(j)
    for k in a:
        fin += k + "\r\n"
    return fin


def main(arr):  ## Input the array matrix / Program start
    for i in arr:
        if check_input(i):
            foo = i
            break
    ladder = get_ladder(foo[0], foo[1], random.randint(foo[0], foo[1]))
    print(ladder.rstrip())
    
    
