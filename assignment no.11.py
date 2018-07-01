#Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class animal:
	def __init__(self,no_of_legs):
		self.no_of_legs=no_of_legs
		
	def display(self):
		print("it has",self.no_of_legs,"legs")
		
class tiger(animal):
	def show(self):
		print("tiger is a carnivorous animal")
		
a=tiger(int(input("enter no_of_legs of tiger:")))
a.show()
a.display()

#Q.2- What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

# output:-
# A B
# A B

#Q.3- Create a class Cop. Initialize its name, age , work experience and designation. 
# Define methods to add, display and update the following details. Create another class 
# Mission which extends the class Cop. Define method add_mission _details. Select an 
# object of Cop and access methods of base class to get information for a particular cop 
# and make it available for mission.

class cop:
	def __init__(self,name,age,work_experience,designation):
		self.name=name
		self.age=age
		self.work_experience=work_experience
		self.designation=designation
		
	def display(self):
		print("your name:",self.name)
		print("your age:",self.age)
		print("your work_experience:",self.work_experience)
		print("your designation:",self.designation)
		
	def update(self,name,age,work_experience,designation):
		self.name=name
		self.age=age
		self.work_experience=work_experience
		self.designation=designation
		
class mission(cop):
	def add_mission_details(self):
		print("for murder mystery:")	
		print("this cop is suitable")
		
m=mission(input("enter your name:"),int(input("enter your age:")),int(input("enter your work experience:")),input("enter your designation:"))

m.add_mission_details()
m.display()
m.update(input("enter your name:"),int(input("enter your age:")),int(input("enter your work experience:")),input("enter your designation:"))

m.add_mission_details()
m.display()	

#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. 
#Create class rectangle and square which inherits shape and access the method Area.

class shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
		
	def area(self):
		self.result=self.length*self.breadth
		
class rectangle(shape):
	def rectarea(self):
		print("area of rectangle is",self.result)
		
class square(shape):
	def sqarea(self):
		print("area of square is",self.result)
		
s=square(int(input("enter length of square:")),int(input("enter breadth of square:")))
s.area()
s.sqarea()

r=rectangle(int(input("enter length of rectangle:")),int(input("enter breadth of rectangle:")))
r.area()
r.rectarea()


	