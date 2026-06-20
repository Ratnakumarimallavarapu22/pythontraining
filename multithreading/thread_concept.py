''''''
#what is a program?
#a program is a set of instructions stored on adisk

print("hello")
#storing on a disk?
#python hello.py
#hello

#what is process?
#when a program starts executing it becomes a process
#running?
#python hello.py
#hello

#os --operating system

#chrome:
#vs code:
#spotify:
#each one is seperate process

#characterstics:
#1.independent
#2.seperate memory:
#chrome:1.8GB,vs-code-500MB
#3.heavy a weight:
#memory allocation
#resource allocation
#cpu scheduling

#what is a thread?
#a thread is smallest unit of execution inside a process

#restaurent == process
#workers inside res = threads

#worker1-  taking the orders
#worker2 - cooking
#worker3 - billing
#worker4 - cleaning

#visually:
#process:
#chrome:
#    +thread1
    
#    +thread2
#   +thread3

#process                        thread
#1.independent                  part of process
#2.heavy weight                 light weight
#3.seperate memory              shered memory
#4.slow                         fast
#5.expensive                    cheap
#6.communication                difficult easy


''''''
#why threads are faster?
#threads will share the memory process needs seperate memory process needs seperate memory aalocation

#concurrency?
#teacher checking the notebooks
#student A
#student B
#student C

#concurrency:
#A
#B
#C
#A
#B
#C
#one at a time
#rapidly switching appears simultaneously


#parallelism:
#cashier1 --> customer 1
#cashier2 --> customer 2
#cashier3 --> customer 3
#truly simultaneous

#CPU1 --> Task a
#cpu2 --> Task b
#cpu3 --> Task c
#A
#B
#A
#B
#A
#B

#parallelism:
#cpu1 - AAA
#cpu2 - BBB

#one chef cooking:
#soup
#noodles
#fried rice


#parallelism:
#chef1 - soup
#chef2 - noodles
#chef3 - fried rice

#python threads will use ---concurrency due to GIL -global interpreter lock




''''''
# #creation of threads:
# import threading
# #function created (do's nothing)
# def display():
#     print("hello")
# #thread object(creation)
# t = threading.Thread(target=display)
# #start thread
# t.start()


# #multiple threads:
# import threading

# def task():
#     print("thread running")
# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)
# t3 = threading.Thread(target=task)

# t1.start()
# t2.start()
# t3.start()


# #thread with loops:
# def numbers():
#     for i in range(5):
#         print(i)
# t = threading.Thread(target=numbers)
# t.start()


# #Two threads with diff task
# def even():
#     for i in range(0,10,2):
#         print("even:",i)
# def odd():
#     for i in range(1,10,2):
#         print("odd:",i)
# t1 = threading.Thread(target=even)
# t2 = threading.Thread(target=odd)
# t1.start()
# t2.start()


# #os schedular decides:
# #which thread to runs first?
# ''''''
# import threading
# print(threading.current_thread())

# #naming of theads:
# import threading

# def task():
    
#     print(threading.current_thread().name)
# t = threading.Thread(target=task,name="student_thread")
# t.start()


''''''
#passing arguments
def square(n):
    print(n*n)

t = threading.Thread(target = square,args = (5,))

t.start()


''''''

#to delay the thread
import time
print("start")
time.sleep(3)
print("end")


import threading
import time

def task():
    for i in range(5):
        print(i)
        time.sleep(1)
t = threading.Thread(target=task)
t.start()

#retry mechanism:
#while true:
#try:
# connect
#except:
#     time.sleep(5)