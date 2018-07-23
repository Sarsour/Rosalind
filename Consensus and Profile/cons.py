import numpy as np

def main():
	
	dna_list = []
	length = 0
	
	i = 1
	with open('rosalind_cons.txt') as file:
		for line in file:
			if line.startswith('>'):
				dna_list.append('|||')
			else:
				dna_list.append(line)


	for x in dna_list:
		print(x)
	
	full_seq_str = ''.join(dna_list)
	full_seq_str = full_seq_str.replace('\n', ' ').replace('\r', '').replace(' ', '')
	
	pure_dna_list = full_seq_str.split('|||')
	
	for x in pure_dna_list:
		print(x)
		
	dna_list_str = ' '.join(pure_dna_list)
	print(dna_list_str)	
	
	# BELOW HERE GOOD
	
	
	a_list = []
	c_list = []
	g_list = []
	t_list = []	
	cons_list = []
	length = len(pure_dna_list[1])
	
	x=0
	while x < length:
		output = "".join(item[x].upper() for item in dna_list_str.split())
		cons_list.append(max(set(output), key=output.count))
		a_list.append(output.count('A'))
		c_list.append(output.count('C'))
		g_list.append(output.count('G'))
		t_list.append(output.count('T'))
		x += 1
		
	print(length)
	
	final_list = []
	final_list.append(a_list)
	final_list.append(c_list)
	final_list.append(g_list)
	final_list.append(t_list)
	
	dna_matrix = np.array(final_list)
	
	
	row_title_list = ['A: ', 'C: ', 'G: ', 'T: ']
	cons_seq = ''.join(cons_list)
	
	output_file = open('output.txt', 'w')
	output_file.write(cons_seq + '\n')
	for row in dna_matrix:
		output_file.write(row_title_list[1] + ' '.join(map(str,row)) + '\n')
	
	
	
	
	
	
	
if __name__ == "__main__":
		main()