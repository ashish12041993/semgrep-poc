import os

user_input = input("Enter filename: ")

# ❌ Command injection vulnerability
os.system("cat " + user_input)

