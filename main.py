import requests
import connect

print("Welcome to David's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email2 = input("Type your email again.\n")

if email == email2:
    print("You're in the club!")

    params = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    sheety_response = requests.post(url=connect.SHEETY_ENDPOINT, json=params, headers=connect.sheety_headers)
