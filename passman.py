# IMPORTING REQUIRED MODULE
import os

# FUNCTION TO CHECK FILE EXISTENCE
def Check():
    if os.path.exists('pass.txt'):
        pass
    else:
        data_file = open("pass.txt",'w')
        data_file.close()

# FUNCTION TO ADD NEW ENTRY
def AddNew():
    data_file = open("pass.txt",'a')

    print()
    print("\033[92m ADD NEW PASSWORD \033[0m")
    print()
    usrnm = input("Enter Username: ")
    pswd = input("Enter Password: ")
    site = input("Enter Website Name: ")

    uname = "UserName: " + usrnm + "\n"
    passwd = "Password: " + pswd + "\n"
    web = "Website Name: " + site + "\n"

    data_file.write('----------------------------\n')
    data_file.write(uname)
    data_file.write(passwd)
    data_file.write(web)
    data_file.write('-----------------------------\n')
    data_file.write('\n')
    data_file.close()

# FUNCTION TO DISPLAY ALL ENTRIES
def showPassword():
    data_file = open("pass.txt",'r')
    data = data_file.read()
    data_file.close()
    print()
    print("\033[92m VIEW PASSWORD \033[0m")
    print()
    print(data)
    print()

# FUNCTION TO RESET ALL ENTRIES
def reset():
    data_file = open("pass.txt",'r+')
    data_file.truncate(0)
    data_file.close()
    print("Done with RESET...")

#__main__
while True:
    Check() # CHECK FUNCTION CALLED
    print("\033[92m PASSMAN - PASSWORD MANAGER \033[0m")
    print("\033[96m 1. Add New Password \033[0m")
    print("\033[93m 2. View Password \033[0m")
    print("\033[94m 3. RESET \033[0m")
    print("\033[91m 0. EXIT \033[0m")
    ch = int(input(" Your Choice: "))
    if ch==1:
        AddNew() # ADDNEW FUNCTION CALLED
    elif ch==2:
        showPassword()
    elif ch==3:
        print()
        print("\033[92m RESET \033[0m")
        print()
        print("\033[91m WARNING: IF YOU PROCEED ALL YOUR SAVED PASSWORD WILL BE DELETED!! \033[0m")
        ask = input(" Are you sure to Reset? (y/n): ")
        if ask=='y':
            reset() # RESET FUNCTION CALLED
        elif ask=='n':
            print("\033[91m CANCELLED... \033[0m")
        else:
            print("\033[91m ERROR!! \033[0m")
    elif ch==0:
        print("\033[91m QUITING PASSMAN...")
        raise SystemExit
    else:
        print("\033[91m ERORR!!")
        raise SystemExit