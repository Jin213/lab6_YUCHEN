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









def main():
	student1 = student(name = "yuchen", year = 2 ,gpa = 3.6,current_classes = {"csc": 3})
	print("student name: ", student1.name, "student name: ", student1.year, "student gpa: ",student1.gpa, "student gpa: ",student1.current_classes)



		



if __name__ == '__main__':
	main()
		