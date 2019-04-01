import math

def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True

    else:
        if((int(math.sqrt(n))**2) == n):
            return True
        else:
            return False