def main():
	result = []
	for f in range(70,120,5):
		c = (f-32) * (5/9)
		result.append(c)
	print(result)


if __name__ == "__main__":
	main()