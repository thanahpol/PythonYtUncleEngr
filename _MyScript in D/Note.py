
# Calculate note average

t = int(input('Wieviel mal hast du den Test gamacht?: '))

j = 0
listn = []

for i in range(t):
    print('Geb mir deine ',i+1,'. Note: ')
    n = float(input())
    listn.append(n)
    #print(j)
    j += n
    #print(j)
    
ave = j/t

print()
print('Dein Noten sind: ', listn)
print('Dein Durchschnitt ist: ', ave)
print()

if ave <= 1.4:
    print('Toll!!! aber Du muss noch weiter freißig sein')
elif ave > 1.4 and ave <= 2.4:
    print('Na ja!!! Du bist noch nicht fleißig genug')
else:
    print('Schade!!! Du muss noch Mehr Mehr Mehr und Mehr fleißig')

print()

    
