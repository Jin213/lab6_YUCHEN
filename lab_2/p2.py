def main():
 	mylist = ['Tuesday','Wednesday','Friday']
 	print(mylist)
 	replacement_day = input("Enter the day: ")
 	mylist[0] = replacement_day
 	print(mylist)
 	remove_day = int(input("Enter the index of the day: "))
 	del mylist[remove_day]
 	print(mylist)



if __name__ == "__main__":
 	main()