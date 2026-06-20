'''
'''
#1.race condition
#2.synchronization
#3.lock
#3.rlock
''''''
#why we need synchronization?
''''''
balance = 1000

#thread-1  --withdraw 500
#thread-2  --withdraw 700
#both are accessing the same variable without proper control

#incorrect balance
#wrong transaction
#data corrupt

#to avoid the above we will use:
#synchronization:
#this is a process of controlling access to shared resources so that only one thread modifies at atime



#Lock:hared
#resources:any variable,file,database,object

#example:
count = 0
#if multiple threads modifies count simultaneously

#racecondition:
#occurs when threads access and modify
#shared data simultaneously causing unpredictable outputs

''''''
count = 0
count += 1
print(count)

#write with threads
import threading
count = 0
def increament():
    global count
    count +=1
threads = []
for i in range(1000):
    t = threading.Thread(target=increament)
    threads.append(t)
    t.start()
    print(count)

for t in threads:
    t.join()
print(count)
''''''
#998
#994
#998
''''''
''''''
#critical section:
#code section where shared resources are accessed is called critical section
#count +=1 -->criticalsection

#to avoid the race condition?
#one thread should enter critical section at a time:

#solution:Lock

#what is Lock?
#sync mechanism that allows only one thread to excute a critical section at a time.

#thread A acuires LOCK
#other threads will wait
#thread A releases LOCK
#next thread gets lock

import threading
lock = threading.Lock()
#to apply lock
lock.acquire()
#to realease
lock.release()




''''''
import threading
count = 0
lock = threading.Lock()
def increament():
    global count
    for i in range(10000):
        with lock:
         #critical section
         count +=1
        #lock.release()
t1 = threading.Thread(target=increament)
t2 = threading.Thread(target=increament)
t1.start()
t2.start()
t1.join()
t2.join()
print(count)

#example:BANK
class Bank:
    def __init__(self):
        self.balance = 1000
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
#T1 = 500
#T2 = 700     #negutive

import threading
class bank:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()
    def withdraw(self,amount):
        with lock:
            if self.balance>=amount:
                self.balance -=amount
                print(amount,"withdraw")
            else:
                print("insufficcient balance")
bank = bank()
t1 = threading.Thread(target=bank.withdraw,args=(700,))
t2 = threading.Thread(target=bank.withdraw,args=(500,))
t1.start()
t2.start()
t1.join()
t2.join()
print(bank.balance)

''''''
#deadlock:
#where the threads wait forever for locks
#thread1
#lock A
#waiting for lockB

#thread2
#Lock B
#waiting for Lock A

#thread1 -->waiting LockA
#thread2 -->waiting lockB
#DeadLock





#outer() acquired the lock
#inner() trying to 





''''''
lock = threading.RLock()
def inner():
    with lock:
        print("inner")
def outer():
    with lock:
        print("outer")
        inner()
outer()


''''''
#outer acquire
count = 2
#inner releases






