# -*- coding: utf-8 -*-
###VF
##UPD // 06.01.2024 // After further testing this code is considered not viable for the task provided, due to my own hands growing from
##the wrong place. Code reworking in progress...
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
        b.append('*' * (lad_random + 1 - i))
    a = a[::-1]
    b = b[::-1]
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
    
    
