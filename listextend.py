a=list(map(int,input("Enter numbers separated by spaces: ").split()))
b=list(map(int,input("Enter numbers separated by spaces: ").split()))
a.extend(b)
print("List after extending:", *a)