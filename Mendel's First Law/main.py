#Importing allele traits from text file and store in list
f = open('rosalind_iprb.txt', 'r')
alleleList = []
for line in f:
    alleleList = line.split()

#Initialize variables
k = int(alleleList[0])	#Number of homozygous dominant individuals
m = int(alleleList[1])	#Number of heterozygous individuals
n = int(alleleList[2])	#Number of homozygous recessive individuals
total = k + m + n		#Total population

kprob = k/total			#Probability of homozygous dominant individuals in total population
mprob = m/total			#Probability of heterozgous individuals in total population
nprob = n/total			#Probability of homozygous recessive individuals in total population

#Calculating probability of each mating pair multiplied by dominant allele punnet square results
	#Key: 1 = 100% chance of dominant allele, 0.50 = 50% chance, and so on...
kk = kprob * ((k-1)/(total-1)) * (1)
km = kprob * ((m)/(total-1)) * (1)
kn = kprob * ((n)/(total-1)) * (1)

mk = mprob * ((k)/(total-1)) * (1)
mm = mprob * ((m-1)/(total-1)) * (0.75)
mn = mprob * ((n)/(total-1)) * (0.50)

nk = nprob * ((k)/(total-1)) * (1)
nm = nprob * ((m)/(total-1)) * (0.50)
nn = nprob * ((n-1)/(total-1)) * (0)

#Combine all probabilities to determine final dominant allele probability
finalProb = (kk + km + kn + mk + mm + mn + nk + nm + nn)
print(finalProb)
