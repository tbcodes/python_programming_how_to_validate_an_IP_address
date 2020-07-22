# Creating a IP Checker

# Creating our main function

def ip_checker(ip_address):
    try:
        separated_address = ip_address.split('.')
        # print(separated_address)
        valid_ip = 0
        for i in separated_address:
            if int(i) >= 0 and int(i) <= 255:
                valid_ip += 1
        if valid_ip == 4:
            return True
        else:
            return False
    except:
        return False

# Asking for user input
user_in = input("Enter your IP Address: ")
if ip_checker(user_in):
    print(f"Great!!! {user_in} is a valid IP Address! ")
else:
    print(f"Uuupppsss!!! {user_in} is NOT a valid IP Address! ")

# If I want to verify more than 1 IP Address (We can use a simple "for loop")
#for _ in range(2):
#    user_in = input("Enter your IP Address: ")
#    if ip_checker(user_in):
#        print(f"Great!!! {user_in} is a valid IP Address! ")
#    else:
#        print(f"Uuupppsss!!! {user_in} is NOT a valid IP Address! ")
