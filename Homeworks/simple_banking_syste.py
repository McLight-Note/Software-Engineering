# 2025.03.18
# Mavzu: Simple Banking System
# Muallif: Muhammadsodiq - Salohiddin - Rahimjon - Zhou Zixuan

def banking_system():
  print('Welcome to our AAA Bank')
  balance = 1000

  while True:
    print(f"1. Deposit\n"
          f"2. Widthdraw\n"
          f"3. Check Balance\n"
          f"4. Exit")
    
    choice_of_user = int(input('Enter your option: >>> '))

    if choice_of_user == 1:
      fund = int(input('Enter the abount you want to deposit; \n>>>'))
      balance += fund
      print(f"Your balance is now {balance}\n")
    elif choice_of_user == 2:
      fund = int(input('Enter the amount you want to withdraw: \n>>>'))
      if balance >= fund:
        balance -= fund
        print(f"Your balance in now {balance}\n")
      else:
        print('You have no money :)')
    elif choice_of_user == 3:
      print(f"You balance is {balance}\n")
    elif choice_of_user == 4:
      print('Thanks for using our AAA Bank')
      break
    else:
      print('You chose the wrong input. So choose another option\n')

banking_system()
