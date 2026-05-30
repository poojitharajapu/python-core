import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start=time.asctime()
        start=time.time()
        print("started: ",start)
        print(f"sum: {func(*args,**kwargs)}")
        end=time.asctime().split()
        end=time.time()
        print(f"end: {end}")
        print("time taken: ",end-start)
    return wrapper
@timer
def add(x,y):
    """this is a docstring"""
    su=0
    for i in range(1,x+y+1):
        su+=i
    return su
add(100000,200000)
print(add.__doc__)
print(time.asctime())
print(list(time.asctime().split()))
