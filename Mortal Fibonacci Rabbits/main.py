#Importing data from text file
with open("rosalind_fibd.txt", "r") as file:
    for line in file:
        datalist = line.split(' ')

#Parse file in order to get total months and the lifespan of the rabbits
total_months = int(datalist[0])
lifespan = int(datalist[1])
print('months:', total_months)
print('lifespan:', lifespan)

'''
Setup 2 lists.  The ages_list list how many of each age there are.
The temp_ages_list is there so recently changed values in earlier indexes are not used.
The positions of the indexes in both lists represent the ages, to clarify:
	index 0 = 1 month
	index 1 = 2 months
	index 2 = 3 months
	and so on...
'''
ages_list = []
temp_ages_list = []

for i in range(lifespan):
	temp_ages_list.append(0)
	ages_list.append(0)
	
ages_list[0] = 1	#Initialize first index to represent the first pair of rabits

'''
Loop through ages_list and follow these rules:
	All rabbits pairs that are 1 month old become 2 months old and do not have a pair of babies.
	All rabbits pairs that are 2 months old become 3 months old and have a pairs of babies.
	All rabbits pairs that are 3 months old die and have a pair of babies.
	*Babies are represented by 1 month olds even though their technically 0 months old for the sake of the problem

In the loop, temp_ages_list is updated then transferred over to ages_list afterwards.
This is to prevent any error of the numbers moving around the list.
For example: if we update the ages of 1 month olds to 2 month olds in the list,
then when we get to 2 month olds, it's a higher number than it's supposed to be
'''

#print('Month', 1, ages_list)	#For testing
for i in range(total_months - 1):
	for j in range(lifespan):
		if j == 0:
			temp_ages_list[0] = sum(ages_list) - ages_list[0]
		else:
			temp_ages_list[j] = ages_list[j-1]
	
	for j in range(lifespan):
		ages_list[j] = temp_ages_list[j]
	
	#print('Month', i+2, ages_list)	#For testing
		
print('After', total_months, 'months, there are', sum(ages_list), 'pairs of rabbits')
		


	
