import random
charMap = [[5],[4,6],[4,5,6],[1,3,7,9],[1,3,5,7,9],[1,3,4,6,7,9]]
def check(i):
	pass

dM = []
n = random.randint(1,5)
for i in range(1,10):
	if i in charMap[n-1]:
		dM.append('0')
	else:
		dM.append('')
die = f'''{dM[0]} {dM[1]} {dM[2]}
{dM[3]} {dM[4]} {dM[5]}
{dM[6]} {dM[7]} {dM[8]}'''
print(die)
