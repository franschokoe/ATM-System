# ----Global Variable------

Balance = 0
attempt = 3
bank_running = True

# Deposite function
def deposite(dp_amount):

    global Balance
    Balance += dp_amount #adding balance and assigning it back to itself

    print("**************************")
    print(f'Balance : R {Balance:.2f}')
    print("**************************")


# Withdraw Function
def withdraw(wd_amount):

    global bank_running
    global Balance
    global attempt
    
    # Preventing 0 rand withdrawal
    if Balance < wd_amount:
        attempt -= 1
        print()
        print("❌ Insufficient fund.")
        print(f'You have {attempt} attempt remaining.')

    else :
        Balance -= wd_amount 

        print(f'You Withdraw {wd_amount:.2f}')
        print()
        print("**************************")
        print(f'Balance : R {Balance:.2f}')
        print("**************************")

# Check balance Function
def checkBalance():

    print()
    print("**************************")
    print(f'Available balance : R {Balance:.2f}')
    print("**************************")
    print()


print("----------------------------------------------")
print("----------------BANK ATM SYSTEM---------------")
print("----------------------------------------------")
print()
print("👋 Hi, What would you like to do?")

# while loop for iterating the bank session
while bank_running:
    # attempt loop to breakout
    if attempt != 0:

        print()
        decision = input("1.Deposite 2.Withdraw 3.Balance: ").lower()
        # Decision loop
        if decision == "1":
            print()
            Deposite_Amount = int(input('Deposite : '))
            deposite(Deposite_Amount)
            
        elif decision == "2":

            print()
            Withdraw_Amount = int(input('Withdraw : '))
            withdraw(Withdraw_Amount)
            
        elif decision == '3':
            # envoking the check balance
            checkBalance()
        else:
            print()
            print("Wrong input please try again ")
            break


        print()
        # to stop loop
        bank_session = input('Do you want to [1.logout or 2.continue banking]?: ').lower()

        if bank_session == '2':
            continue

        elif bank_session == '1':

            print()
            print("Thanks for your time.")
            break
        else:
            print('Error try again.')
            break
    elif attempt == 0 :

        print()
        print("Your card is blocked")
        break
    else:
        print('error extended....')
        break
    
    
# Engineered by Frans M Chokoe
# Date of built : 05 July 2025
# Project name : ATM SYSTEM