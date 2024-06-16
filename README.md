## ⬇️ **Run Above Code On Your Local Machine :** 
#### ✦ Copy Below Text As It Is And Run On Your CMD Pannel ➜

```
git clone https://github.com/yashchavan02/MiniProject-B.git
```
---

## 🔵 Mini Project B Details

|Project Title| ATM Machine       |
|:-----------:|:-----------------:|
|Bank Name    |YC Bank            |
|Owner Name   |Yash Anil Chavan   |
|Project Type |Console Based      |
|Data Manage  |MySql              |

---

## 🟤 Used Python Concept
- [x] Time Module
- [x] Random Module
- [x] Datetime Module
- [x] Loops
- [x] String Formatting
- [x] Classes and Objects
- [x] Class Methods
- [x] Conditional Statements

---

## 🟡 ATM Machine Document

---

###      🟢 Overview
This documentation provides an in-depth explanation of an ATM system implemented in Python, with a backend integration using MySQL. The system allows users to perform various banking operations such as creating accounts, depositing money, withdrawing money, changing PINs, and checking balances.

### 🟣 Implementation Overview
The ATM system is designed with the following features and functionality:

#### 🔵 Account Creation
- Users can create a bank account by providing their name, email, gender, account type, initial deposit amount, and PIN.
- Account details are stored in a MySQL database `bank` , specifically in the `customerdata` table.

#### 🟠 Transactions
- **Deposit:** Users can deposit money into their account.
- **Withdrawal:** Users can withdraw money from their account, provided they have sufficient funds.
- **Balance Inquiry:** Users can check their current account balance.

#### 🟤 Security
- The system includes PIN validation when accessing the account or making changes.
- Account locking mechanism after three unsuccessful PIN attempts to prevent unauthorized access.

### 🟡 Uses and Functionality

#### ⭕ Account Creation
- Users enter their personal details such as name, email, gender, account type, and initial deposit amount.
- A unique 4-digit PIN is set during account creation.
- Upon successful creation, account details are stored in the MySQL database.

#### ⭕ Transactions
- **Deposit:** Users can add funds to their account, with the transaction recorded including the date and time.
- **Withdrawal:** Users can withdraw funds, with the system checking for available balance before processing.
- **Balance Inquiry:** Users can check their current balance, displayed in the system.

#### ⭕ PIN Management
- **Change PIN:** Users can change their PIN by entering the old PIN and setting a new 4-digit PIN.
- **Account Locking:** After three consecutive incorrect PIN attempts, the account is locked for security reasons. The user must contact support to regain access.

### 🔴 Conclusion
This ATM system provides a basic yet functional implementation of banking operations integrated with a MySQL database for data persistence. It offers essential features for managing accounts securely and performing common banking transactions. Future enhancements could include additional security measures, transaction history tracking, and multi-account support.


---
<br/>

## 🟣 Screenshot
- 01
  
![NewPythonProjectA](https://github.com/yashchavan02/MiniProject-B/assets/152779289/c3909d86-026c-4c9b-8af4-b53041d9151c)

- 02
 
![NewPythonProjectB](https://github.com/yashchavan02/MiniProject-B/assets/152779289/505a4174-2b6f-4626-a2ef-16070b65bbea)

- 03
  
![NewPythonProjectC](https://github.com/yashchavan02/MiniProject-B/assets/152779289/c6bb3abb-bf7d-434f-9fa4-a1aa970d6e8f)

- 04

![NewPythonProjectD](https://github.com/yashchavan02/MiniProject-B/assets/152779289/d87f765e-03b8-4b1e-bfc8-d1cda610d2fb)





