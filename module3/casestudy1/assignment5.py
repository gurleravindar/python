
def cahsWithdraw():
    print('Selected Cash Withdraw option')
    pass
def cashCredit():
    print('Selected Cash Credit Option')
    pass
def changePassword():
    print('Selected Change Password Option')
    pass
def cancel():
    print("Selected Cancel option")
    exit

user_option = int(input('Enter your option number \n Cash Withdraw:1 \n Cash Credit:2 \n Change Password:3 \n To Cancel:4\n'))

if(user_option == 1):
    cahsWithdraw()
elif(user_option == 2):
    cashCredit()
elif(user_option == 3):
    changePassword()
elif(user_option == 4):
    cancel()
else:
    print('Selected wrong option')
    exit