class student:
	def __init__(self,name,year,gpa,current_classes):
		self.name = name
		self.year = year
		self.gpa = gpa 
		self.current_classes = current_classes

	def addYear(self):
		if(self.year < 6):
			self.year += 1 

	def setgpa(self,newgpa):
		self.gpa = newgpa
		
	def addClass(self,newClass):
		self.current_classes.update(newClass)









class PHD_student(student):
	def __init__(self,name,year,gpa,current_classes,advisor,numberOfResearchPapers):
		super(PHD_student,self).__init__(name,year,gpa,current_classes)
		self.advisor = advisor
		self.numberOfResearchPapers = numberOfResearchPapers


class athlete_student(student):
	def __init__(self,name,year,gpa,current_classes,sport,yearsOfExercise,onScholarship,starter):
		super(athlete_student,self).__init__(name,year,current_classes)
		self.sport = sport
		self.yearsOfExercise = yearsOfExercise
		self.onScholarship = onScholarship
		self.starter = starter



		

if __name__ == "__main__":
	main()




		