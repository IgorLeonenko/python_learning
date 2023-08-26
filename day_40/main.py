from users_manager import UsersManager

user_first_name = input("Tell your name:\n")
user_last_name = input("Tell your last name:\n")
user_email = input("Tell your email:\n")
user_email_confirmation = input("Confirm your email:\n")

if user_email == user_email_confirmation:
  user_manager = UsersManager()
  user_data = {
    "user": {
      "firstName": user_first_name,
      "lastName": user_last_name,
      "email": user_email
    }
  }
  user_manager.add_user(user_data)
  print("You now in club!")
else:
  print("Email not confirmed")