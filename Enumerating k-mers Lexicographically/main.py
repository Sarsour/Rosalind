import itertools

# Simple way using itertools.permutations
def simple_limited_permuations(symbol_list, answer_length):
	
	# Find all permutations of length imported and convert to a list format
	all_permuations = itertools.permutations(symbol_list, answer_length)
	permuation_list = [''.join(item) for item in all_permuations]
	
	# Add combinations that are identical.  Example: AA or BB
	for i in symbol_list:
		temp_string = ''
		for x in range(answer_length):
			temp_string = temp_string + i
		permuation_list.append(temp_string)
	
	permuation_list.sort()	# Alphabetize list
	
	for perm in permuation_list:
		print(perm, "", end='')

# Full method without using modules	
def full_limited_permutations(symbol_list, answer_length):
	
	new_symbol_list = [[]]
	for i in range(answer_length):
		new_symbol_list = [[i]+j for i in symbol_list for j in new_symbol_list]
    
	print(new_symbol_list)
	

if __name__ == "__main__":
	
	#Importing data from text file
	data_list = []
	symbol_list = []
	answer_length = 0
	
	with open("rosalind_lexf.txt", "r") as file:
		for line in file:
			data_list.append(line.strip())
			
	symbol_list = data_list[0].split(' ')
	answer_length = int(data_list[1])
	
	print(symbol_list)
	print(answer_length)

	
	# Call simple length limited permuation method
	simple_limited_permuations(symbol_list, answer_length)
	
	print('')
	
	# Call full length limited permuatation method
	full_limited_permutations(symbol_list, answer_length)
	
	
	