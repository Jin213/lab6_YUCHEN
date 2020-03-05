

def main():
	number_of_class = int(input("Please enter the number of classes: "))
	classes = {}
	for i in range(0, number_of_class):
		temp_classes = input("Please add a class: ")

		temp_credit_hour = int(input("Please enter the credit hour: "))




		classes.update({temp_classes : temp_credit_hour})
	



	print(classes)

if __name__ == "__main__":
	main() 





