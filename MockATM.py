import random

database = {}   #My Database Dictionary declearation


def init():

    isRightOptionSelected = False   #A checker variable
    print("Welcome to NAS Bank")

    while isRightOptionSelected == False:

        haveAccount = int(input("Do you have an Account with us: 1 (yes) 2 (no) \n"))

        if(haveAccount == 1):
            isRightOptionSelected = True
            login()
        elif(haveAccount ==2):
            isRightOptionSelected = True
            print(register())
        else:
            print("You have selected a wrong option")

#login function
def login():
    print("*****Kindly Login with your credentials*****")

    isLoginCorrect = False

    while isLoginCorrect == False:
        
        accountNumberFromUser = int(input("What is your Account Number\n"))
        
        password = input("What is your password\n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    isLoginCorrect = True
                    print(bankOperations(userDetails))
            else:
                print("Invalid Account or Password")


#register function
def register():
    print("*****Kindly Register an Account*****")
    firstName = input("What is your first name\n")
    lastName = input("What is your last name\n")
    email = input("What is your email address\n")
    password = input("Input a password\n")

    accountNumber = generateAccountNumber() #Variable to create Account Number

    database[accountNumber] = [ firstName, lastName, email, password]

    #return database;   #This is to return database

    print("Your Account Has Been Successfully Created")
    print("==========================================================")
    print("Here is Your Generated Account Number %d" % accountNumber)

    login()


#bankOerations function
def bankOperations(user):
    print("Welcome %s %s " % (user[0], user[1]))
    print("How would you like to be assisted")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Balance")
    print("4. Complaint")

    optionSelected = int(input("Pick your preferred option \n"))

    if(optionSelected == 1):
        print("You selected %s" %optionSelected)
        withdrawal = int(input("Type in the amount you wish to Withdrawal \n"))
        print("THANK YOU FOR BANKING WITH US,\nKINDLY TAKE YOUR #%s" %withdrawal)

        print('============================================\n')
        homePage(user)
    

    elif(optionSelected == 2):
        print("You selected %s" %optionSelected)
        deposit = int(input("Type in the Amount you want to Deposit \n"))
        print("Deposit successful of #%s" %deposit)
        print('============================================\n')
        print("Do you still want to Withdraw? \n")
        withdrawal = int(input("Type in the amount you wish to Withdrawal \n"))
        if( withdrawal <= deposit):
            print("WITHDRAW CASH SUCCESSFUL\nKINDLY TAKE YOUR #%s" %withdrawal)
            print('============================================\n')
            homePage(user)
        else:
            print("INSUFFICIENT CASH\n")
            print('============================================\n')
            homePage(user)

            
        pass
        
    elif(optionSelected == 3):
        print("You selected %s" %optionSelected)
        balance = input("Type in to check Balance\n")
        print("Balance amount is #%s" %balance)
        print('============================================\n')
        homePage(user)
        pass
        
    elif(optionSelected == 4):
        print("You selected %s" %optionSelected)
        complain = input("Type in your Complain\n")
        print("THANK YOU, WE WILL LOOK INTO IT AND GET BACK TO YOU")
        print('============================================\n')
        homePage(user)
        pass

    else:
        print("NO INVALID OPTION SELECTED")
        print('============================================\n')
        homePage(user)
        

def homePage(user):
    print("Would you like to perform another transcation")
    print("1. Main Menu")
    print("2. Logout")
    

    optionSelected2 = int(input("Select option \n"))

    if(optionSelected2 == 1):
        print("WELCOME BACK TO MAIN MENU\n")
        print('============================================\n')
        bankOperations(user)
    

    elif(optionSelected2 == 2):
        print("YOU HAVE SUCCESSFULLY LOGOUT\n")
        print('============================================\n')
        login()
        
    else:
        print("NO INVALID OPTION SELECTED")

#generateAccountNumber function
def generateAccountNumber():
    
    #print("Generated Account Number is ")  #This is to print "Generated Account Number is "
    return random.randrange(1111111111,9999999999) #to return range between 1111111111 and 9999999999




####ACTUAL BANK SYSTEM####

#print(generateAccountNumber())
init()

