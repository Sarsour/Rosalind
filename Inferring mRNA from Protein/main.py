#Importing data from text file
with open("rosalind_mrna.txt", "r") as file:
    for line in file:
        protein_string = line.rstrip()

#Importing codon key from text file
codon_list = []
aminoacid_list = []
with open("codon_list.txt", "r") as file:
	for line in file:
		temp_list = []
		temp_list = line.split(' ')
		codon_list.append(temp_list[0].rstrip())
		aminoacid_list.append(temp_list[1].rstrip())
		

#Method to calculate total by finding all combinations
def possible_rna_strings(input):

	total = 1
	for c in input:
		total *= aminoacid_list.count(c)	#Count number of combinations of amino acid
	
	total = total * 3	#Multipy by 3 for total different RNA strings
	
	return total


if __name__ == "__main__":

    print(possible_rna_strings(protein_string) % 1000000)