#Importing allele traits from text file and store in list
f = open('rosalind_iev.txt', 'r')
alleleList = []
for line in f:
    alleleList = line.split()

#Initialize variables of each allele grouping (e.g. AA mates with Aa)
AAAA = int(alleleList[0])
AAAa = int(alleleList[1])
AAaa = int(alleleList[2])
AaAa = int(alleleList[3])
Aaaa = int(alleleList[4])
aaaa = int(alleleList[5])

#Find expected number of dominant phenotypes for each couple
expectedAAAA = AAAA * (2 * 1)
expectedAAAa = AAAa * (2 * 1)
expectedAAaa = AAaa * (2 * 1)
expectedAaAa = AaAa * (2 * 0.75)
expectedAaaa = Aaaa * (2 * 0.50)
expectedaaaa = aaaa * (2 * 0)

#Find total expected number of dominant phenotypes
totalDom = expectedAAAA + expectedAAAa + expectedAAaa + expectedAaAa + expectedAaaa + expectedaaaa
print(int(totalDom))