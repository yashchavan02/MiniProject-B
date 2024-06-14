import datetime
import random
import time 

print("\n")

current_datetime = datetime.datetime.now()
day_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

def account_number_generate():
    return str(random.randint(1000, 9999))

class ATM: 

    def get_email_address(self):
        while True:
            self.Email_Id = input("$ Email Address: ")
            if ".com" not in self.Email_Id:
                print("$ Invalid Email Address.")
            else:
                break

    def get_account_data(self):
        print("\n$ Please Enter Your Account Details.")
        self.acc_holder_name = input("$ Account Holder Name : ")
        self.get_email_address()
        self.acc_type = input("$ Account Type (Saving/Current/Salary) : ") 
        self.current_balance = float(input("$ Initial Deposit Amount : ")) 
        self.pin = input("$ Create 4 Digit PIN : ")
    
    def print_data(self): 
        time.sleep(0.25)
        print("\n$ Bank Account Is Created Successfully.") 
        time.sleep(0.25)
        print(f"\n$ {self.acc_type.capitalize()} Bank Account")
        print(f"$ Customer Name : MR. {self.acc_holder_name.upper()}") 
        print(f"$ Customer Email Id : {self.Email_Id}")
        print(f"$ Bank Account No. 3241{self.pin}{self.account_number}") 
        print("\n") 
         
    def withdrawal_paisa(self): 
        withdrawal_amount = float(input("\n$ Enter Withdrawal Amount From " + self.acc_type.capitalize() + " Account : ")) 
        if self.current_balance < withdrawal_amount: 
            print("Insufficient balance! Your available balance is ", self.current_balance) 
        else: 
            self.current_balance -= withdrawal_amount 
            print(f"$ Rs. {withdrawal_amount} Debited from XXXXXXXX{self.account_number} Account On {day_date} . Current Balance: {self.current_balance}") 

    def deposit_paisa(self): 
        deposit_amount = float(input("\n$ Enter Deposit Amount: ")) 
        self.current_balance += deposit_amount 
        print(f"$ Rs. {deposit_amount} Credited To XXXXXXXX{self.account_number} Account On {day_date}. Current Balance: {self.current_balance}") 

    def start(self):
        while True:
            print("$ Please Press s To Start ATM")
            start_value = input("Input Here : ")
            if start_value.lower() == "s":
                print("\n<<--- Welcome To YC Bank ATM --->>")
                print("\n$ Please Create A New Bank Account.")
                self.get_account_data() 
                self.account_number = account_number_generate() 
                self.print_data() 
                self.check_pin()
            else:
                print("$ Invalid Input.")

    def check_pin(self):
        while True:
            print("$ Please Enter Your 4 Digit Pin.")
            pin_value = input("Input Here : ")
            if pin_value == self.pin:
                self.choice()
                break
            else:
                print("$ Invalid Pin.")

    def choice(self):
        while True:
            print("\n$ Please Enter Your Choice [ Enter Number ex. For Deposit --> 2]\n")
            print("1. Withdrawal")
            print("2. Deposit")
            print("3. Check Balance")
            choice_value = input("\nInput Here : ")
            if choice_value == "1":
                self.withdrawal_paisa()
            elif choice_value == "2":
                self.deposit_paisa()
            elif choice_value == "3":
                print(f"\n$ Your Current Balance is {self.current_balance}")
            else:
                print("\n$ Invalid input! Please enter a valid input.")
                continue

            if input("\nDo you want to continue (yes/no)? ").lower() != "yes":
                print("\n$ Thank You For Using YC Bank ATM. \n\n")
                exit()

o = ATM() 
o.start()
