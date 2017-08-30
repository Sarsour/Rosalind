#Importing sequences from text file
from Bio import SeqIO                      
sequences = []                             
handle = open('rosalind_tran.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):  #Automatically parses the fasta file format
    seq = ''                               
    for s in record.seq:	#Isolate sequences since that's what we need
        seq += s
    sequences.append(seq)
handle.close()

#Loop through both sequences in the list and compare each index to see if there's a transition or tranversion, then add to transList
firstSequence = sequences[0]
secondSequence = sequences[1]
transList = []	#'X' = Transition, 'O' = Transversion, '-' = Neither

for i in range(len(firstSequence)):
	if (firstSequence[i] == 'A' and secondSequence[i] == 'G') or (firstSequence[i] == 'G' and secondSequence[i] == 'A') or \
	(firstSequence[i] == 'C' and secondSequence[i] == 'T') or (firstSequence[i] == 'T' and secondSequence[i] == 'C'):	#Transition
		transList.append('X')
	
	elif (firstSequence[i] == 'A' and secondSequence[i] == 'A') or (firstSequence[i] == 'C' and secondSequence[i] == 'C') or \
	(firstSequence[i] == 'G' and secondSequence[i] == 'G') or (firstSequence[i] == 'T' and secondSequence[i] == 'T'):	#Neither
		transList.append('-')
		
	else:
		transList.append('O')

#Count number of transitions and divide by the number of transversions
print(transList.count('X') / transList.count('O'))
