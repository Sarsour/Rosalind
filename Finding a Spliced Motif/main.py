#Importing sequences from fasta file
from Bio import SeqIO                      
sequence_list = []                             
handle = open('rosalind_sseq.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):  #Automatically parses the fasta file format
    seq = ''                               
    for s in record.seq:	#Isolate sequences since that's what's needed
        seq += s
    sequence_list.append(seq)
handle.close()

#Isolate the main sequence and the spliced motif
main_sequence = sequence_list[0]
spliced_sequence = sequence_list[1]


add_list = []	#This list is used to store the distance between matches

#Find matches and cut string so time isn't wasted searching the previous portion multiple times.  Only trailing nucleotides needed.
for spliced_nucleotide in spliced_sequence:
	for main_nucleotide in main_sequence:
		if main_nucleotide == spliced_nucleotide:
			add_list.append(main_sequence.index(spliced_nucleotide) + 1)
			main_sequence = main_sequence[(main_sequence.index(spliced_nucleotide) + 1):]
			break;

#Add the numbers together in order to find the original position of each matching nucleotide then print in required format.
number = 0
for i in add_list:
	number = number + i
	print(number, '', end='')