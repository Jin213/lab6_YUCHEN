from lab5 import student 
class PHD_student(student):
	def __init__(self,name,year,gpa,current_classes,advisor,numberOfResearchPapers):
		super(PHD_student,self).__init__(name,year,gpa,current_classes)
		self.advisor = advisor
		self.numberOfResearchPapers = numberOfResearchPapers

def addYear(self):
		if(self.year < 6):
			self.year += 1 

class athlete_student(student):
	def __init__(self,name,year,gpa,current_classes,sport,yearsOfExercise,onScholarship,starter):
		super(athlete_student,self).__init__(name,year,gpa,current_classes)
		self.sport = sport
		self.yearsOfExercise = yearsOfExercise
		self.onScholarship = onScholarship
		self.starter = starter
	def addYear(self):
		if(self.year < 4):
			self.year += 1 

	def setgpa(self,newgpa):
		self.gpa = newgpa
		
	def addClass(self,newClass):
		self.current_classes.update(newClass)
def main():
	PHD_student1 = PHD_student(name = "yuchen", year = 5, gpa = 3.8, current_classes = {"csc1": 3},numberOfResearchPapers = 100,advisor = "malir") 
	athlete_student1 = athlete_student(name = "yuchen", year = 4, gpa =3.0,current_classes = {"chemstry" : 3}, sport = "swiming " ,yearsOfExercise = 5,onScholarship = "Yes",starter = " Joe ")

	print(PHD_student1.name,PHD_student1.year,PHD_student1. gpa,PHD_student1.current_classes,PHD_student1.numberOfResearchPapers)
	print("name: ",athlete_student1.name,"year: ",athlete_student1.year,"gpa: ",athlete_student1.gpa,"current_classes: ",athlete_student1.current_classes,"sport: ",athlete_student1.sport,"years pf exercise: ",athlete_student1.yearsOfExercise,"on scholarship: ",athlete_student1.onScholarship, "starter: ",athlete_student1.starter) 

if __name__ == '__main__':
	main()









