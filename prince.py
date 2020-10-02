bank = 50000
print("1 for withdraw\n2 for add money\n3 for lookup amount")
var1 = int(input())
if var1==1:
    print("How much money do you wnt to reedem")
    var2 = int(input())
    if var2<=bank:
        print(bank-var2)
    else:
        print("You have no sufficient amount to reedem")
elif var1==2:
    print("how much money do you want to add")
    var3 = int(input())
    print(bank+var3)
elif var1==3:
    print(bank)
else:
    print("PLease select correct option")