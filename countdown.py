# 'Countdown' Python program using the time module and a while true loop

import time #Imports time module

# while true loop
# few defenses to protect from invalid user input
while True:
    try:
        my_time = int(input("Enter a time in seconds: "))
        if 0 < my_time <= 864000:
            break
        elif my_time > 864000:
            print("Please enter a number less than or equal to 864,000 (10 days).")
        else:
            print("You can't use 0 or negative numbers!")
    except ValueError:
        print("Invalid! Please use positive numbers!")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        exit()
   
# this is to arrange all the time parts: seconds, minutes, hours and days
try:
    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        days = int(x / 86400)
        print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        exit()

# final print when countdown is over
print("TIME'S UP!")