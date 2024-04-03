from random import randint
x = int(input('Number of players (between 2 and 6): '))

if x not in range(2,7) and x % 2 != 0: 
    x = 3
    print('I expected between 2 and 6 players')
    print('I\'m setting the number of players to',x)
print(x)
            
y = int(input('Number of coins per player (between 5 and 100):'))

if y<5 or y>100  and y % 2 != 0:
    y = 10
    print('I\'m setting the number of coins to',y)
print(y)    

print('Game begins with',x,'players.\nEach player has',y ,'coins.')


banker = randint(2,x)
print('Player', banker ,'is randomly chosen as banker')
    

#current_balance = y
print('Current balance:')
for player in range(1,x+1):
    print('Players ',player,'has',y,'coins')



#print('Player',banker,': You are the banker! Please enter a valid bank amount:' , input( ))

B = int(input('Player %s: You are the banker! Please enter a valid bank amount:' %banker))
while B < 1 or B > y:
    B = int(input('Player %s: You are the banker! Please enter a valid bank amount:' %banker))

bank_amount = B
bets = []    
for k in range(1,x+1):
    if k == banker:
        continue
    else:
        b = int(input('Player %s: Please enter a valid bank amount:' %k))
        #bets.append(b)
        
        while b > bank_amount:
            b = int(input('Player %s: Please enter a valid bank amount:' %k))
        bets.append(b)
        if sum(bets) <= bank_amount:
            bank_amount-=sum(bets)
        elif sum(bets) == B:
            break
        #else:
        #   break

print('Round starts:')

for n in range(1,len(bets)+1):
    for a in range(0,len(bets)+1):
        if n == banker:
            print('Player %s: Banker with bank amount=%s' %(banker,sum(bets))+':')
            break
        else:
            print('Player %s: has bet %s' %(n,bets[a]) + ':')
            break

    break
