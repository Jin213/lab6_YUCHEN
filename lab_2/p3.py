def main():
	d = { 'Tuesday' : 'cs' }
	today = input("Enter the current day: ")
	if(today in d ):
		print(today + " you have " + d[today] + " as your first lecture")
	else:
		print(today + " you don't have class" )
		print(d)  

				 





if __name__ == "__main__":
	main() 