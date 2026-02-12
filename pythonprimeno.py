n=int(input("Enter the number: "))
c=0
for i in range(2,n):
    if n%i==0:
        c=c+1   
if c==0:
    print("prime number")   
else:
    print("not a prime number")
