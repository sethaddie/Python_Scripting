#n=int(input("Enter value for comparision here:"))
#print(n>=100)
#print(n=100)
#print(n>=100)

n=int(input("Enter value here:"))
y=int(input("Enter value here"))
total=n+y
def get_comparision(total,n,y):
    answer=total>=100
    return answer

print(get_comparision(total,n,y))