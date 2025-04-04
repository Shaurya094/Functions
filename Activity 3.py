def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def multi(x,y):
    return x * y
def div(x,y):
    return x / y

print ("a. Add \n b. subtract \n c. multiply \n d. divide")
choice = input("Choose either a, b, c, or d. \n")

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

if choice == "a":
    print ("that equals to: ", add(n1,n2))
elif choice == "b":
    print ("that equals to: ", sub(n1,n2))
elif choice == "c":
    print ("that equals to: ", multi(n1,n2))
elif choice == "d":
    print ("that equals to: ", div(n1,n2))
else:
    print ("invalid")