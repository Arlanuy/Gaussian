#Juico, Jules Gerard E.
#2014-40314
#Section

#Successive Relaxation


'''File handling
		The input is a text file. First row is the omega while succeeding rows are the coefficient matrix (augmented) for each equation
'''
File = open("sor_inputh.txt","r")

'''Initialization of values and matrices
		The input is just read from the input text file and stored to a list. The contents of the list are copied to respective lists (the coefficients and the products).
'''
Omega = float(File.readline())
List = [float(Number) for Number in File.readline().replace("\n","").split(" ")]
Size = len(List) - 1
Coefficients = [[0 for x in range(0, Size)] for y in range(0, Size)]
Current = 		[0 for x in range(0, Size)]
Next = 			[0 for x in range(0, Size)]
Product = 		[0 for x in range(0, Size)]
Print = 		[0 for x in range(0, Size)]
Change = 1

Product[0] = List.pop(-1)
Coefficients[0] = List
for y in range(1, Size):
	List = [float(Number) for Number in File.readline().replace("\n","").split(" ")]
	Product[y] = List.pop(-1)
	Coefficients[y] = List
#Current = [0, 0, 0]


'''Function defintion
		The function takes in the i and adds the coefficients multiplied by the value of the other x. The value of x is current or next depending on what the i is.
'''
def Function(y, Size):

	Answer = Product[y]
	for x in range(0, y):
		Answer = Answer - (Coefficients[y][x] * Next[x])
	for x in range(y + 1, Size):
		Answer = Answer - (Coefficients[y][x] * Current[x])

	return Answer

'''Main algorithm
		K is the current step where the algorithm is, used just for printing. The current xs takes the "next xs" and each of the next values are computed, using the function previously defined. If the change of the next step and the previous step is less than a certain threshhold, then the algorithm stops. There is also a hard limit implemented to prevent infinite loops for solutions that don't converge.
'''
K = 0
while (Change == 1):

	print("K = {}".format(K))

	for i in range(0,Size):
		Current[i] = Next[i]

	for y in range(0, Size):
		if (Coefficients[y][y] != 0):
			Next[y] = ((1 - Omega) * (Current[y])) + (Omega * (Function(y, Size)  / Coefficients[y][y]))
		else:
			Next[y] = 0

	Change = 0
	for i in range(0, Size):
		Difference = abs(Next[i] - Current[i])
		if (Difference > 0.00001):
			Change = 1

	for i in range(0, Size):
		Print[i] = round(Current[i], 4)
	print("Current: {}".format(Print))
	for i in range(0, Size):
		Print[i] = round(Next[i], 4)
	print("Next: {}\n".format(Print))

	K += 1

	#if (K == 10):
	#	Change = 0

'''Output
		The last value is printed out to the terminal as a list.
'''
for i in range(0, Size):
	Print[i] = round(Next[i], 3)
print("x: {}".format(Print))
