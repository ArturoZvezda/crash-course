import random

def fac(n=random.randint(0,5)):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)
    
