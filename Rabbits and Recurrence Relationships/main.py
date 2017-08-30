#Importing numbers of months and litter size per mate form text file 
f = open('rosalind_fib.txt', 'r')

for line in f:
    input = line

#Setup variables
months = int(input.partition(' ')[0]) #Parsing the first number which represents the number of months
litterSize = int(input.rsplit(None, 1)[-1]) #Parsing the last number which is the litter size per mate

previousLitterSize = 0
currentLitterSize = 1
ppLitterSize = 0 #previous prevous litter size
i = 0

#Calculating the population of rabbits after a certain number of months using the Fibonacci sequence
while i < months:
	currentLitterSize = (currentLitterSize + (ppLitterSize * litterSize))
	ppLitterSize = previousLitterSize
	previousLitterSize = currentLitterSize
	i = i + 1

#Print litter size
print(currentLitterSize)

	

