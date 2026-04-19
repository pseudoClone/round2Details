from dotenv import load_dotenv
import os
load_dotenv()

user_input = input("Enter the API KEY: ")
if(user_input == os.getenv("API")):
        print("Login Sucessful")
else:
        print("Login invalid")
        exit(1)