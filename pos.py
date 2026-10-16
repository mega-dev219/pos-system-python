
open = input("Press the power btn : ")
if open =="on":
     print("power on")
else:
      print("power off")
balance = 5000
user_pin = input("Enter user pin: ")
menu =['withdraw', 'Transfer', 'Data', 'Airtime', 'check balance']
menu.append("Transaction History")
History =[]
print(menu)
choice= input("choose an option: ")
if choice=="withdraw":
    print("Enter Amount")
    amount=int(input("Amount: "))
    if amount <= balance:
        print("Next")
        print("Input card")
        pin = input("Enter user_pin : ")
        if pin == user_pin:
            print("Transaction approved")
            print(f"""------RECEIPT--------
transaction: withdraw
amount:{amount},
status: successful,
Thank you for banking with us""")
            History.append({'type': 'withdraw', 'amount':amount, 'status': 'successful'})
        else:
            print("Wrong pin try again")
    else:
        print("Amount exceeds balance")
           

print("Would you like another Transaction?")
choice = input("Yes/No: ")
if choice == "Yes":
     print("Select transaction")
choice = input("select transaction type :")
if choice == "Transfer":
      print("Enter Amount")
      amount = int(input("Enter amount:"))
      if amount > 500:
           print("Enter Account number")
      else:
              print("amount too low")
      account_num = (input("Enter account number: "))
      print(f"Transfering to account{account_num}")
print("input pin")
pin = int(input("Enter your pin: "))      
if pin == user_pin:
  print("Transaction approved")
else:
    print("Wrong pin")
print(f""" ------RECEIPT--------
transaction: Transfer
amount:{amount}
account:{account_num}
status: successful
Thank you for banking with us """)

print("would you like another transfer")
choice = input("Yes/No: ")
if choice == "Yes":
  print("select transaction type")
choice = input("Select transaction type: ")
if choice == "Airtime":
    print("Enter amount")
    amount = int(input("Enter amount: "))
    if amount >= 100:
        print("Enter Pin")
        print("Enter phone number") 
        phone_number = input("Enter phone number :")
        print(f"Enter into phone number{phone_number}")
        pin = int(input("Enter your pin: "))
        if pin == user_pin :
            print("Transaction approved")
            print(f""" ------RECEIPT--------
transaction: Airtime
amount:{amount}
phone number:{phone_number}
status: successful
Thank you for banking with us""")
            History.append({'type': 'Airtime', 'amount': amount, 'phone_number': phone_number, 'status': 'successful'})
        else:
            print("Wrong pin")
    else:
            print("amount too low")  
elif choice == "Transaction History":
    for record in History:
        print(record)
