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


def get_ladder(lad_args):
    a = []
    b = []
    fin = ""
    for i in range(lad_args[2], lad_args[1]+1):
        a.append('*' * (i))
    for i in range(lad_args[0], lad_args[2]+1):
        b.append('*' * (i))
    a = a[::-1]
    for j in b:
        a.append(j)
    for k in a:
        fin += k + "\r\n"
    #return fin.rstrip()
    return a


def main(arr):  ## Input the array matrix / Program start
    for i in arr:
        if check_input(i):
            foo = i
            break
    ladder = get_ladder([foo[0], foo[1], random.randint(foo[0], foo[1])])
    #print(ladder)
    print("\r\n".join(ladder))
    
    
