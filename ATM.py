import mysql.connector
import datetime
import random
import time
import re

con = mysql.connector.connect(
    user='root',
    host='localhost',
    database='bank',
    passwd='Y@sh2081%'
)
mycursor = con.cursor()

insert_customer_query = "INSERT INTO customerdata (name, email, gender, pin, bank_acc) VALUES (%s, %s, %s, %s, %s)"

def account_number_generate():
    return str(random.randint(1000, 9999))

class ATM:
    def __init__(self):
        self.current_balance = 0
        self.account_number = ''
        self.acc_holder_name = ''
        self.email_id = ''
        self.acc_type = ''
        self.gender = ''
        self.customer_gen = ''
        self.mysql_gen = ''
        self.pin = ''
        self.acc_no = 0

    def get_email_address(self):
        while True:
            email_id = input("$ Email Address: ")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email_id):
                print("$ Invalid Email Address.")
            else:
                self.email_id = email_id
                break

    def get_initial_balance(self):
        while True:
            try:
                initial_balance = float(input("$ Initial Deposit Amount: "))
                if initial_balance <= 0:
                    print("$ Please enter a valid Initial Deposit Amount")
                else:
                    self.current_balance = initial_balance
                    break
            except ValueError:
                print("$ Please enter a valid number")

    def get_account_data(self):
        print("\n$ Please Enter Your Account Details.")
        self.acc_holder_name = input("$ Account Holder Name: ")
        self.get_email_address()
        self.acc_type = input("$ Account Type (Saving/Current/Salary): ")
        self.get_initial_balance()
        while True:
            gender = input("$ Enter Your Gender [M/F]: ").upper()
            if gender == "M" or gender == "MALE":
                self.customer_gen = "MR."
                self.mysql_gen = 'M'
                break
            elif gender == "F" or gender == "FEMALE":
                self.customer_gen = "MS."
                self.mysql_gen = 'F'
                break
            else:
                print("$ Please Enter Valid Gender.")
        while True:
            pin = input("$ Create 4 Digit PIN: ")
            if pin.isdigit() and len(pin) == 4:
                self.pin = pin
                break
            else:
                print("$ Please enter a valid 4 digit PIN")

    def print_data(self):
        self.account_number = account_number_generate()
        self.acc_no = int("3241" + self.pin + self.account_number)

        time.sleep(0.25)
        print("\n$ Bank Account Is Created Successfully.")
        time.sleep(0.25)
        print(f"\n$ {self.acc_type.capitalize()} Bank Account")
        print(f"$ Customer Name: {self.customer_gen} {self.acc_holder_name.upper()}")
        print(f"$ Customer Email Id: {self.email_id}")
        print(f"$ Bank Account No. 3241{self.pin}{self.account_number}")

        customer_data = (self.acc_holder_name, self.email_id, self.mysql_gen, self.pin, self.acc_no)
        try:
            mycursor.execute(insert_customer_query, customer_data)
            con.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()

        print("\n")

    def withdrawal_paisa(self):
        try:
            withdrawal_amount = float(input(f"\n$ Enter Withdrawal Amount From {self.acc_type.capitalize()} Account: "))
            if self.current_balance < withdrawal_amount:
                print("Insufficient balance! Your available balance is", self.current_balance)
            else:
                self.current_balance -= withdrawal_amount
                print(f"$ Rs. {withdrawal_amount} Debited from XXXXXXXX{self.account_number} Account On {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
        except ValueError:
            print("$ Please enter a valid number")

    def deposit_paisa(self):
        try:
            deposit_amount = float(input("\n$ Enter Deposit Amount: "))
            self.current_balance += deposit_amount
            print(f"$ Rs. {deposit_amount} Credited To XXXXXXXX{self.account_number} Account On {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
        except ValueError:
            print("$ Please enter a valid number")

    def change_pin(self):
        count = 0
        while True:
            old_pin = input("\n$ Please Enter Your Old Pin: ")
            if old_pin == self.pin:
                while True:
                    new_pin = input("\n$ Please Enter Your New Pin: ")
                    if new_pin.isdigit() and len(new_pin) == 4:
                        self.pin = new_pin
                        print("\n$ Your Pin Is Changed Successfully.")
                        try:
                            mycursor.execute("UPDATE customerdata SET pin = %s WHERE bank_acc = %s", (new_pin, self.acc_no))
                            con.commit()
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        break
                    else:
                        print("$ Please enter a valid 4 digit PIN")
                break
            else:
                count += 1
                if count == 3:
                    print("\n$ You Have Entered Wrong Pin 3 Times. Your Account Is Blocked.")
                    try:
                        mycursor.execute("DELETE FROM customerdata WHERE bank_acc = %s", (self.acc_no,))
                        con.commit()
                    except mysql.connector.Error as err:
                        print(f"Error: {err}")
                    print("\n$ Thank You For Using YC Bank ATM.\n\n")
                    exit()
                else:
                    print("\n$ Invalid Pin, Please Try Again.")

    def start(self):
        while True:
            start_value = input("\n$ Please Press s To Start ATM: ")
            if start_value.lower() == "s":
                print("\n<<--- Welcome To YC Bank ATM --->>")
                print("\n$ Please Create A New Bank Account.")
                self.get_account_data()
                self.print_data()
                self.check_pin()
            else:
                print("$ Invalid Input.")

    def check_pin(self):
        count_pin = 0
        while True:
            pin_value = input("$ Please Enter Your 4 Digit Pin: ")
            if pin_value == self.pin:
                self.choice()
                break
            else:
                print("$ Invalid Pin.")
                count_pin += 1
                if count_pin == 3:
                    print("\n$ You Have Entered Wrong Pin 3 Times. Your Account Is Blocked.")
                    print("\n$ Thank You For Using YC Bank ATM.\n\n")
                    try:
                        mycursor.execute("DELETE FROM customerdata WHERE bank_acc = %s", (self.acc_no,))
                        con.commit()
                    except mysql.connector.Error as err:
                        print(f"Error: {err}")
                    exit()

    def choice(self):
        while True:
            print("\n$ Please Enter Your Choice [Enter Number ex. For Deposit --> 2]\n")
            print("1. Withdrawal")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change Pin")
            choice_value = input("\nInput Here: ")
            if choice_value == "1":
                self.withdrawal_paisa()
            elif choice_value == "2":
                self.deposit_paisa()
            elif choice_value == "3":
                print(f"\n$ Your Current Balance is {self.current_balance}")
            elif choice_value == "4":
                self.change_pin()
            else:
                print("\n$ Invalid input! Please enter a valid input.")
                continue

            if input("\nDo you want to continue (yes/no)? ").lower() != "yes":
                print("\n$ Thank You For Using YC Bank ATM.\n\n")
                break

        con.close()

atm = ATM()
atm.start()
