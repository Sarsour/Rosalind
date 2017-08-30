#Importing sequences from text file
#Also'from Bio import SeqIO' can be used to import from a fasta file.  Here's the code that it consists of:
"""
def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

with open('rosalind_splc.txt') as fp:
    for name, seq in read_fasta(fp):
        print(name, seq) 	#Prints out name then sequence in this case, it can be manipulated to what's needed
"""

#The quick way is to download biopython (make sure Microsoft Visual C++ 14.0 is downloaded, it's required...I ran into that problem)
from Bio import SeqIO                      
sequences = []                             
handle = open('rosalind_splc.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):  #Automatically parses the fasta file format
    seq = ''                               
    for s in record.seq:	#Isolate sequences since that's what we need
        seq += s
    sequences.append(seq)
handle.close()

#The first sequence is the full DNA string.  Every sequence after that is the exon.  Isolate the full sequence.
fullSequence = sequences[0]

#Remove the introns (everything including and after index 1 of sequences list) from fullSequence
i = 1
while i < len(sequences):
	fullSequence = fullSequence.replace(sequences[i], '')
	i += 1

#Convert fullSequence to RNA (replace U with T)
fullSequence = fullSequence.replace('T', 'U')

#Convert to protein string by taking every 3 nucleotides and converting to a codon
#Codon conversion list located in text file which is imported and stored as 2 lists (amino acid and codon)
aaList = []
codonList = []

with open('codonkey.txt') as f:
    for line in f:
        line = line.replace("\n", "")
        aa, codon = line.split('_')
        aaList.append(aa)
        codonList.append(codon)

#Match every 3 nucleotides in fullSequence (without introns) with it's respective amino acid.
#Add proteinString repeatedly to form full protein result, then print it
proteinString = ''
i = 0

while i < (len(fullSequence)-2):
	pos = aaList.index(fullSequence[i:i+3])
	proteinString = proteinString + codonList[pos]
	i += 3
	
print(proteinString)