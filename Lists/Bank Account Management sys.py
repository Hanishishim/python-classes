bank_accounts = {}
while True:
    print("""
    ===================== APEX SYSTEM =======================
    1. Open New Account
    2. Process Deposit
    3. Process Withdrawal
    4. View Single Account
    5. View Bank Analytics (Total, Max, Min)
    6. View Transaction History
    7. Transfer Funds
    8. Exit
    ==========================================================
    """)
    choice = input("Enter option (1-6): ").strip()
    if choice == "1":
        account_number = int(input("Enter new account number: "))
        if account_number in bank_accounts:
            print("An account with that number already exists!")
        else:
            pin = int(input("Create a 4-digit security PIN:"))
            deposit = float(input("Enter initial deposit amount: $"))
            if deposit < 0:
                print("Initial deposit cannot be negative!")
            else:
                bank_accounts[account_number] = {
                    "balance": deposit, 
                    "pin": pin
                }    
                print(f"Account {account_number} created successfully with ${deposit:.2f}!")
    elif choice == "2":
        account_number = int(input("Enter your account number: "))
        if account_number in bank_accounts:
            deposit = float(input("Enter deposit number: "))
            if deposit > 0:
                bank_accounts[account_number]["balance"] += deposit
                bank_accounts[account_number] = {
                "history": {
                "Deposited": deposit
                        }
                    }
                print(f"Deposit successful, new balance for account {account_number} is {bank_accounts[account_number]:.2f}")
            else: 
                print("Deposit amount must be positive!")
        else:
            print("Account not found!")
    elif choice == "3":
        account_number = int(input("Enter your account number: "))
        if account_number in bank_accounts:
            entered_pin = int(input("Enter your 4-digit PIN: "))
            if entered_pin == bank_accounts[account_number]["pin"]:
                withdrawal = float(input("Enter withdrawal amount: "))
                if withdrawal <= 0:
                    print("Withdrawal must be greater than zero.")
                elif withdrawal <= bank_accounts[account_number]:
                    bank_accounts[account_number] -= withdrawal
                    print(f"Withdrawal successful! New balance for account {account_number} is ${bank_accounts[account_number]:.2f}")
                    bank_accounts[account_number] = {
                    "history": {
                            "Deposited": deposit,
                            "Withdrawn": withdrawal
                            }
                        }
                else:
                    print("Your account doesn't have enough money to withdraw that amount!")
            else:
                print("PIN is incorrect!")
        else:
            print("Account not found!") 
    elif choice == "4":
        account_number = int(input("Enter your account number: "))
        if account_number in bank_accounts:
            entered_pin = int(input("Enter your 4-digit PIN: "))
            if entered_pin == bank_accounts[account_number]["pin"]:
                balance = bank_accounts[account_number]["balance"]
                print(f"The balance for account {account_number} is {balance}")
            else:
                print("PIN is incorrect")
        else:
            print(f"Account {account_number} is not found!")
    elif choice == "5":
        if bank_accounts:
            balances = [acc["balance"] for acc in bank_accounts.values()]
            total = sum(balances)
            highest = max(balances)
            lowest = min(balances)
            print(f"The total amount in bank: ${total:.2f}")
            print(f"The Highest amount stored is: ${highest:.2f}")
            print(f"The Lowest amount stored is: ${lowest:.2f}")
        else:
            print("No account is exist in the system yet to run analytics")
    elif choice == "6":
        account_number = int(input("Enter account number to view history: "))
        if account_number in bank_accounts:
            entered_pin = int(input("Enter your 4-digit PIN: "))
            if entered_pin == bank_accounts[account_number]["pin"]:
                print(f"\n--- Transaction History for Account {account_number} ---")
                for transaction in bank_accounts[account_number]["history"]:
                    print(transaction)
            else:
                print("PIN is incorrect!")
        else:
            print("Account not found!")    
    elif choice == "7": 
        sender = int(input("Enter your account number: ")) 
        if sender in bank_accounts: 
            entered_pin = int(input("Enter your 4-digit PIN: "))
            if entered_pin == bank_accounts[sender]["pin"]: 
                receiver = int(input("Enter the receiver's account number: ")) 
                if receiver in bank_accounts: 
                    if sender == receiver: 
                        print("You can't transfer to the same account!") 
                    else: 
                        transfer_amount = float(input("Enter the amount you want to transfer: ")) 
                        if transfer_amount <= 0: 
                            print("Transfer amount should be greater than 0!") 
                        elif bank_accounts[sender]["balance"] >= transfer_amount: 
                            bank_accounts[sender]["balance"] -= transfer_amount
                            bank_accounts[receiver]["balance"] += transfer_amount 
                        
                            bank_accounts[sender]["history"].append(f"Transferred ${transfer_amount:.2f} to Account {receiver}")
                            bank_accounts[receiver]["history"].append(f"Received ${transfer_amount:.2f} from Account {sender}")
                        
                            print("\n--- Transfer Successful! ---") 
                            print(f"Sent ${transfer_amount:.2f} to Account {receiver}") 
                            print(f"Your new balance is ${bank_accounts[sender]['balance']:.2f}") 
                        else: 
                            print("Transfer failed. Insufficient funds!") 
                else: 
                    print(f"Receiver's account {receiver} is not found!") 
            else:
                print("PIN is incorrect!")
        else: 
            print(f"Can't find sender account {sender}!")

    elif choice == "8":
        text1 = "Thank you for trusting APEX!"
        text2 = "Goodbye!"
        print(text1.center(50))
        print(text2.center(50))
        break
    else:
        print("Invalid selection. Please choose an option between 1 and 8.")