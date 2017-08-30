import itertools

def find_num_of_permutions(input):	#Find the total number of permutations
	
	product = 1
	for i in range(1, input + 1):
		product *= i
		i -= 1
	
	return product


def get_list_of_permuations(input):	#Find a list of possible permuations
	
	num_combinations = []
	list_of_permutations = []
	
	for i in range(input):
		list_of_permutations.append(i + 1)
	
	#Use permuation tool (no need to reinvent the wheel).  Loops through the list_of_permutations would also do it.
	for subset in itertools.permutations(list_of_permutations, len(list_of_permutations)):
		#Print in required format for problem
		for i in subset:
			print(i, '', end='')	
		print('')
	
	return(input)


if __name__ == "__main__":
	
	#Importing data from text file
	with open("rosalind_perm.txt", "r") as file:
		for line in file:
			length = int(line.rstrip())
	
	print(find_num_of_permutions(length))
	get_list_of_permuations(length)





