class Employee:
	def __init__(self,name,yearsOfExperience,pastEmployers):
		self.name = name
		self.yearsOfExperience = yearsOfExperience
		self.pastEmployers = pastEmployers
		def pastEmployers(self):
			return(self,pastEmployers)

		def yearsOfExperience(self,y):
			self,yearsOfExperience = y
		def needsPromotion(self):
			if(self.yearsOfExperience > 5):
				return(True)
			else:
				return(False)



def main():
	employee1 = Employee(name = 'John' ,yearsOfExperience = 6,pastEmployers = [])
	employee2 = Employee(name = "joe",yearsOfExperience = 8,pastEmployers = "cook")
print(employee2.needsPromotion())


if __name__ == "__main__":
	main()