from math import *
from time import *
from string import *
from pylab import *
from random import *
from tp2 import *

S = montecarlo2(10000)
print S

print('      n | erreur  | temps (sec) ')
print('---------------------------------')
for i in range(1,7):
	n = 10**i
	tps1 = clock()
	S = montecarlo2(n)
	tps2 = clock()
	tps3 = tps2 - tps1
	E = abs(S - I)
	print(' {0}  | {1}   | {2}  '.format(n,E,tps3))


entete = '      n | erreur  | temps (sec) '
pointilles = '---------------------------------'


with open ('tableau7', 'w') as fichier:
	fichier.write(entete + '\n')
	fichier.write(pointilles + '\n')
	for i in range(1,7):
		n = 10**i
		tps1 = clock()
		S = montecarlo2(n)
		tps2 = clock()
		tps3 = tps2 - tps1
		E = abs(S - I)
		fichier.write(' {0}  | {1}   | {2}  \n'.format(n,E,tps3))



