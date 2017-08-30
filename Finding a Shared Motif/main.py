#Importing sequences from fasta file
from Bio import SeqIO                      
sequence_list = []                             
handle = open('rosalind_lcsm.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):  #Automatically parses the fasta file format
    seq = ''                               
    for s in record.seq:	#Isolate sequences since that's what's needed
        seq += s
    sequence_list.append(seq)
handle.close()

#Organize sequences shortest to longest.  Isolate the shortest sequence.
sequence_list.sort(key=len)
shortest_sequence = sequence_list[0]

not_found = True
found_list = []

#Loop through the shortest sequence and find every combination.  Find the longest subsequence that is in every other sequence.
for i in range(len(shortest_sequence)):
  for j in range(len(shortest_sequence)):
    #print(shortest_sequence[i:j+1])

    k = 1
    count = 0
    while k < len(sequence_list):
      if shortest_sequence[i:j+1] in sequence_list[k] and len(shortest_sequence[i:j+1]) > 1:
        #print("true", 'for', shortest_sequence[i:j+1] )
        count += 1
      if count == (len(sequence_list)-1):
          found_list.append(shortest_sequence[i:j+1])
      k += 1
      
  #print(" ")

#Print out the longest sequence that is in every other sequence.
print(max(found_list, key=len))