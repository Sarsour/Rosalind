
# Calculating partial permutations (this method sometimes doesn't work with very large numbers, would have to use a big number module)
def find_partial_permutations(full_set_number, subset_number):
	
	# Formula for partial permutations: n! / (n - k)! = n(n - 1)(n - 2)...(n - k + 1)
	return( (factorial(full_set_number)) / (factorial(full_set_number - subset_number)) % 1000000)

	
# Calculating factorial for a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculating partial permutations more efficiently (works with all numbers, however large)
def more_efficient_find_partial_permutations(full_set_number, subset_number):
	partial_perm = 1
	for i in range(subset_number):
		partial_perm *= (full_set_number - i)
	return(partial_perm % 1000000)

	
if __name__ == "__main__":
	
	# Importing data from text file
	full_set_number = ''
	subset_number = ''
	
	with open("rosalind_pper.txt", "r") as file:
		for line in file:
			full_set_number, subset_number = line.split(' ')
	
	full_set_number = int(full_set_number)
	subset_number = int(subset_number)
	print(full_set_number, subset_number)

	partial_permutations = int(find_partial_permutations(full_set_number, subset_number))
	print(partial_permutations)
	
	print('')
	
	more_efficient_partial_permutations = more_efficient_find_partial_permutations(full_set_number, subset_number)
	print(more_efficient_partial_permutations)