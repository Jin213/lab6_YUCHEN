class student:
	def __init__(self,name,year,gpa,current_classes):
		self.name = name
		self.year = year
		self.gpa = gpa 
		self.current_classes = current_classes
		super().__init__(name,year,gpa,current_classes) 
	

	def main():
		student_1 = student(name = "Andy" ,year = 4,gpa = 3.6 ,current_classes = {"csc280:4.0"})
		print(student_1.sex)
	
	

if __name__ == "__main__":
	main() 








