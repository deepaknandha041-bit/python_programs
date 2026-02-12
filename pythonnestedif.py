n=int(input("Enter a number: "))
if n>=18:
    print("your are eligible to vote")
    if n>=21:
        print("you are eligible for candidate")
    else:
        print("you are not eligible for candidate") 
else:
    print("you are not eligible to vote")   
    print("you are not eligible for candidate")