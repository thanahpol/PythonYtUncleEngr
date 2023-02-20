
# Calculate times to get note 1

t = int(input('Wieviel mal hast du den Test schon gamacht?: '))

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

#print()
print('Deine Noten sind: ', listn)
print('Dein Durchschnitt ist: ', ave)
print()

k = 0
ave1 = ave
for i in range(100):
    if ave1 >= 1.5:
    #for i in range(20):
        k += 1
        listn.append(1.0)
        #ave1 = sum(listn)/(i+1+t)
        ave1 = sum(listn)/len(listn)

if ave >= 1.5:
    print('Du brauchst noch', k, 'Mal(e), die Note Eins zu erreichen!!!')
    print()
    print('Deine geplanten Noten sind: ')
    print(listn)
    print()
    if ave >= 1.5 and ave <= 2.4:
        print('Na ja!!! Du bist noch nicht fleißig genug!!!')
    else:
        print('Schade!!! Du muss noch Mehr Mehr Mehr und Mehr fleißig!!!')
else:
    print('Toll!!! Du kreigst schon die Eins!!!')
    print()
    print('Aber muss Du noch weiter freißig sein!!!')


'''
if ave <= 1.4:
    print('Toll!!! aber Du muss noch weiter freißig sein')
elif ave > 1.4 and ave <= 2.4:
    print('Na ja!!! Du bist noch nicht fleißig genug')
else:
    print('Schade!!! Du muss noch Mehr Mehr Mehr und Mehr fleißig')

print()
'''
    
