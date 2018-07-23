import math

def main():
	
	prob_list = []
	AT_count = 0
	GC_count = 0
	
	with open('rosalind_prob.txt') as file:
		for line in file:
			if line[0] == 'A' or line[0] == 'C' or line[0] == 'G' or line[0] == 'T':
				for c in line:
					if c == 'A' or c =='T':
						AT_count += 1
					elif c == 'G' or c =='C':
						GC_count += 1
			else:
				prob_list = line.split()
	
		prob_list = [float(i) for i in prob_list]
		
	output_list = []
	for prob in prob_list:
		output = math.log10((((1-float(prob))/2)**AT_count) * ((float(prob)/2)**GC_count))
		output_list.append(output)
	
	output_list = [ '%.3f' % elem for elem in output_list ]
	print(output_list)
	output_string = ' '.join(output_list)
	
	output_file = open('output.txt', 'w')
	output_file.write(output_string)
	
	
if __name__ == "__main__":
		main()