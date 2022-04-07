import time
from datetime import datetime

def func1(arr1,arr2,arr3):
    t1 = datetime.now()
    print(t1.minute,":",t1.second,":",t1.microsecond)
    start=time.time()
    for i in range(0,100000):
        sum = 0
        for j in range(0,len(arr1)):
            sum=sum+arr1[j]
        for k in range(0,len(arr2)):
            sum = sum + arr2[k]
        for l in range(0,len(arr3)):
            sum = sum + arr3[l]
        if(sum!=210):
            print(false)
    tm = datetime.now()
    print(tm.minute,":",tm.second,":",tm.microsecond)
    end=time.time()
    diff=end - start
    print("time take by first loop",diff)
    start1=time.time()
    for i in range(0,10000000):
        sum = 0
        for j in range(0,len(arr1)):
            sum = sum + arr1[j]
            sum = sum + arr2[j]
            sum = sum + arr3[j]
        if (sum!=210):
            print(false)
    tn= datetime.now()
    print(tn.minute,":",tn.second,":",tn.microsecond)
    end1=time.time()
    diff1=end1-start1
    print("time taken by second loop",diff1)

arr1=[10,20,30]
arr2=[20,10,30]
arr3=[40,40,10]
func1(arr1,arr2,arr3)
