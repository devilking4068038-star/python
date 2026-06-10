x=str(input("enter enter your choice(y or n):"))
E=[]
S={}
while x!="n":
    v=int(input("Enter your choice(1=write your item,2= to get sum and item,3=exit):"))
    if v==1:
        expenses =int(input("enter amount of expenses:"))
        items =str(input("enter name of items:"))
        S[items] = expenses
        E.append(expenses)
    elif v==2:
        print(S)
        print(E)
        print(sum(E))
    else:
        break
