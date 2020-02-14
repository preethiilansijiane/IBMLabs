num=int(input("enter an number"))
fact=1
if num < 0:
    print("the number is less than 0")
elif num == 0 :
    print("number is equal to 0")
else:
    for i in range(1,num+1) :
        fact=fact*i
print(fact)
