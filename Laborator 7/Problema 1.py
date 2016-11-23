import random
import time

def afisare_infinity(a,b):
    start_time=time.time()

    while True:
        x = random.randint(a, b)  # x secunde
        time.sleep(x)
        print(time.strftime("%M:%S",time.gmtime(time.time()-start_time)))


print(afisare_infinity(2,4))