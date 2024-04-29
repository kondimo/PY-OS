# Importing libraries
from time import sleep, strftime, localtime
from maskpass import askpass
from json import load
import ascii

# Initializaton
version = "Alpha 0.20"

# Setup
current_user = username = input("Please set username: ")
pin = int(askpass("Please set PIN: ", "*"))

while True:
    if pin == int(askpass("Confirm PIN: ", "*")):
        print("Correct.")
        break
    else:
        print("Try again.")

# Starting OS
print("Loading...")
sleep(2)
print(f"---------------------------------\nNote: This OS is fully open-source\nPY-OS [Version: {version}]\n---------------------------------\n{ascii.art['logo']}\n---------------------------------\nHint: Type 'help' for commands.\n---------------------------------\n")

# Main loop
while True:
    com = input(f"{current_user}:~$ ")
    if com == "help":
        print("Command list:\nprint: prints text on the console\nlogout: logs out of the current instance\nshutdown: terminates the os\ntime: shows the current time\nascii: shows ascii art\ncalculate: does simple mathematical calculations")
    elif com == "print":
        print(input("Enter text: "))
    elif com == "logout":
        print("To login press Enter")
        askpass("")
        while True:
            if input("Username: ") == username:
                break
            else:
                print("User not found.")
        while True:
            if int(askpass("PIN: ", "*")) == pin:
                break
            else:
                print("Wrong PIN. Please try again.")
        print("Successfully logged in.")
    elif com == "shutdown":
        exit()
    elif com == "time":
        print("The time is:",strftime("%d-%m-%Y %H:%M:%S", localtime()))
    elif com == "ascii":
        print("---------------------------------\nAscii art list:\nlogo\nbig_stickman\nsmall_stickman\n---------------------------------")
        while True:
            art = input("Enter a name from the list: ")
            if art == "logo":
                print(ascii.art["logo"])
                break
            elif art == "big_stickman":
                print(ascii.art["big_stickman"])
                break
            elif art == "small_stickman":
                print(ascii.art["small_stickman"])
                break
            else:
                print("Ascii art not found.")
    elif com == "calculate":
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        operation = input("Operation(+,-,*,/): ")
        try:
            if operation == "+":
                result = num1 + num2
            if operation == "-":
                result = num1 - num2
            if operation == "*":
                result = num1 * num2
            if operation == "/":
                result = num1 / num2
            print(num1, operation, num2, "=", result)
        except:
            print("Calculation error.")
    else:
        if not com == "":
            print("Command not found.")
        else:
            continue
        
        
