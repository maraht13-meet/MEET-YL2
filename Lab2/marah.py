class Animal():
	def __init__(self,name,age):
		self.name = name
		self.age =age
	def sleep(self):
		print self.name + " of " + str(self.age) + " is sleeping "
	def eat (self,food):
		print self.name + " of " + str(self.age) + " is eating " + food 

class Bird (Animal):
	def __init__(self,name,age,wings_color):
		Animal.__init__(self, name, age)
		self.wings_color = wings_color
	def fly(self):
		print self.name + " of " + str(self.age) + " which has " + self.wings_color + " wings is flying"

class Dog (Animal):
	def __init__(self,name,age,skin_color):
		Animal.__init__(self, name, age)
		self.skin_color = skin_color
	def bark(self):
		print self.name + " of " + str(self.age) + " which is " + self.skin_color + " is barking"
	

x = Animal("MEET" , 11  )
x.sleep()
x.eat("apple")
y = Animal("Cat" , 2 )
y.sleep()
y.eat("pizza") 
z= Bird("Picky" , 3 , "brown")
z.sleep()
z.eat("orange")
z.fly()
f= Dog("Bob" , 5 , "white")
f.sleep()
f.eat("meat")
f.bark()