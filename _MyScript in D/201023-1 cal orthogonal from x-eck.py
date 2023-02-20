
#Calculate orthogonal from x-Eck

r = int(input('Geb mir, wieviel Eck?: '))
j = 0

for i in range(r):
	#j = j+i
	j += i

dia = (r-1)*r - j - r

print('Es gibt', dia, 'Diagonal')
