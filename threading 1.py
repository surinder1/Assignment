#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.

# method-1
# import threading
# from threading import Thread
# import time 
# def display():
	# print("child thread:",threading.current_thread().getName())
	# bt=time.time()
	# time.sleep(3)
	# print("child thread:",threading.current_thread())
	# et=time.time()
	# print("total time taken:",et-bt)

# t=Thread(target=display)
# t.start()

#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between

import threading
from threading import Thread
import time 

class mythread(Thread):
	def run(self):
		for x in range(1,11):
			print(x)
			time.sleep(1)
			
t=mythread()
t.start()

#Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list 
#with a delay of multiple of 2 sec between each display.Delay goes like 2sec-4sec-6sec-8sec-10sec

import threading
from threading import Thread
import time

class mythread(Thread):	
	def run(self):
		l=[]
		for x in range(5):
			l.append(int(input("enter the no:")))
		print(l)
		bt=time.time()
		time.sleep(2)
		i=2
		for x in l:
			print(x)
			et=time.time()
			print("time taken:",et-bt)
			time.sleep(i)
			i=i+2

t=mythread()
t.start()

#Q4. Call factorial function using thread.

import threading
from threading import Thread
import time

class factorial(Thread):
	def run(self):
		n=int(input("enter any number:"))
		fact=1
		for i in range(1,n+1):
			fact = fact * i
		print("factorial:",fact)
		
t=factorial()
t.start()

