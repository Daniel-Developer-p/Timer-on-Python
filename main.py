# Connect the necessary module
import time
# We ask for the reminder text, which should then be shown to the user
print("What should I remind you about?")
# We wait for the user's response and put the result in the string variable text
text = str(input())
# Asking about the time
print("In how many minutes?")
# Here we will store the time after which you need to show a reminder
local_time = float(input())
# Convert minutes to seconds
local_time = local_time * 60
# Wait for the required number of seconds, the program does nothing at this time
time.sleep(local_time)
# Showing the reminder text
print(text)
