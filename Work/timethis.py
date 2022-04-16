# timethis.py
import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print(f'{func.__module__}.{func.__name__}: {(end - start):0.2f}')
    return wrapper

if __name__ == '__main__':
    @timethis
    def countdown(n):
        while n > 0:
            n -= 1
    
    countdown(1)            #    0.00
    countdown(10)           #    0.00
    countdown(100)          #    0.00
    countdown(1000)         #    0.00
    countdown(10000)        #    0.00
    countdown(100000)       #    0.02
    countdown(1000000)      #    0.11
    countdown(10000000)     #    1.76
    countdown(100000000)    #   10.22
    #countdown(1000000000)   #  103.37
    #countdown(10000000000)  #  735.89
    #countdown(100000000000) # 5812.77