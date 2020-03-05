def main():
 number1 = int(input("Please enter number1: "))
 number2 = int(input("Please enter number2: "))

 while(number1 <= number2):
  print("Make sure number1 > number2!")
  number1 = int(input("Please enter number1: "))
  number2 = int(input("Please enter number2: "))

 answer = int(input("Please enter your answer to " + str(number1) + "-" + str(number2) + " here: "))

 while((number1 - number2) != answer):
  print("Wrong answer. Try again. What is the answer to " + str(number1) + "-" + str(number2) + "?")
  answer = int(input("Please enter your answer here: "))
 print("You got it!")



if __name__ == "__main__":
	main() 




	









	



















