#problem Set1 
#Name : Yuchen Jin 
#Time spent : 14 min 
# Last modefied : Jan 26 ,2020 






def main():
	P = float(input("enter the initial balance: "))
	r = float(input("enter the interest rate: "))
	n = float(input("enter the numbers of times interest applied per time period: "))
	t = float(input("number of time periods elaped: " ))
	A = P*(1+r/n)**(n*t)
	print(A)
	













if __name__ == "__main__":
	main() 