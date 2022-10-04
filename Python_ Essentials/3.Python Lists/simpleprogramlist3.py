bets=[5,11,9,42,3,49]
drawn=[3,7,11,42,34,49]
hits= 0

for number in bets:
    if number in drawn:
        hits+=1

print("The number of hits are:", hits)