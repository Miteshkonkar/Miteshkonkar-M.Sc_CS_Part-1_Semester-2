import time
from datetime import datetime
def func1():
    arr=[]
    arr1=[]
    t1=datetime.now()
    start=t1.microsecond
    print(start)
    for i in range(0,1000):
        arr.insert(0,i)
    print(arr)
    t2=datetime.now()
    end1=t2.microsecond
    print(end1)
    for i in range(0,1000,4):
        arr1.insert(0,i)
        arr1.insert(0,i+1)
        arr1.insert(0,i+2)
        arr1.insert(0,i+3)
    print(arr1)
    t3=datetime.now()
    end2=t3.microsecond
    print(end2)
    print("before unrolling",end1-start)
    print("after unrolling",end2-end1)
func1()
#first loop should run more time then second but get the same output
