def balance(bal):
    print(f"Your Balance is ₹ {bal:.2f}.")
def deposit():
    amt=float(input("Please Enter an Amount to be Deposit: "))
    if amt<0:
        print("Please Enter Valid Amount.")
        return 0
    else:
        print(f"Your {amt} is Credited Successfully.")
        return amt
def withdraw(bal):
    amount=float(input(("Please Enter an Amount to be Withdraw: ")))
    if amount>bal:
        print("Oops! Insufficient Balance.")
        return 0
    elif amount<0:
        print("Your amount must be greaterthan 0.")
        return 0
    else:
        print(f"Your {amount} is Debited Successfully.")
        return amount
def abc(name,cpassw,bal):
    print("Our Bank Of India".center(25,'_'))
    print(" User id: ",name)
    print("Password: ",cpassw)
    print(" Balance: ",bal)
    return ' '
def main(N,pwd,name,cpassw):
    is_running=bool(name==N and pwd==cpassw)
    bal=0
    if is_running:
        print("Our Bank Of India".center(25,'-'))
        print("Perss '1' for -Check Balance.")
        print("Press '2' for -Deposit Money.")
        print("Press '3' for -Withdraw Money.")
        print("Press '4 for -Account Details.")
        print("Press '5' for -Exit.")
        a=input("Please Enter Your Choice : ")
        if a== '1':
            bal=balance(bal)
        elif a=='2':
            bal += deposit()
        elif a=='3':
            bal-=withdraw(bal)
        elif a=='4':
            print(abc(name,cpassw,bal))
        elif a=='5':
            is_running=False
        else:
            print("Please Enter Valid Number")
    print("Thank You! For choosing Our Bank of India.")
print("Welcome To Our Bank Of India".center(50,'-'))
name=input("Create your user Id: ").strip()
with open("Details.txt","r") as file:
    content=file.read()
if name in content:
    print("This Username already exists.")
else:
    passw=input("Create a Password: ").strip()
    cpassw=input("Confirm your Password: ")
with open("Details.txt", "a") as file:
        file.write(f"{name}, {cpassw}\n")
if cpassw==passw:
    print("Registration completed successfully")
    N=input("Enter user ID: ")
    if N==name:
        pwd=input("Enter Password: ")
else:
    print("Password does not matched.")
main(N,pwd,name,passw)