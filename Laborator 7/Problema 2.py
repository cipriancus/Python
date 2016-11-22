import math
import time

def prim1(a):
    for iterator in range(2,int(math.sqrt(a))):
        if a % iterator==0:
            return False

    return True

def prim2(a):
    for iterator in range(2, int(a/2)):
        if a % iterator == 0:
            return False

    return True


def print_efficiency(a):

    start_time=time.time()
    prim1(a)
    prim1_time=time.time()-start_time

    start_time=time.time()
    prim2(a)
    prim2_time=time.time()-start_time

    if prim1_time>prim2_time:
        return "prim2 is more efficient "
    else:
        return "prim1 is more efficient "



print(print_efficiency(7919))