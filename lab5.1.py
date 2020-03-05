class student:
	def __init__(self,name,year,gpa,current_classes):
		self.name = name
		self.year = year
		self.gpa = gpa 
		self.current_classes = current_classes

	def addYear(self):
		if(self.year < 4):
			self.year += 1 

	def setgpa(self,newgpa):
		self.gpa = newgpa
		
	def addClass(self,newClass):
		self.current_classes.update(newClass)

