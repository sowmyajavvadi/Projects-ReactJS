amount=1000000
total_creditamount=0
total_debitamount=0
option=int(input("select your option 1.credit 2.debit 3.ministatement: "))
if option==1:
    add_amount=int(input("credit amount"))
    total_creditamount=amount+add_amount
    print(total_creditamount)
elif option==2:
    withdrawl_amount=int(input("debit amount"))
    total_debitamount=amount-withdrawl_amount
    print(total_debitamount)
else:
    print("credited amount",total_creditamount)
    print("debited amount",total_debitamount)
   
   
