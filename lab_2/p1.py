def main():
	class_on = ["Tuesday", "Wednesday","Friday"]
 	today = input("What day is today? ")
 	if today in class_on:
  		print(today + ' you have class')
 	else:
  		print(today + " you don't have class")
  		print(["Tuesday", "Wednesday","Friday"])



if __name__ == '__main__':
	main()