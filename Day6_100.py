#This is for day 6 and this is what I learned
password = input("Enter your password: ")
if password == "secret":
  print("Welcome Ray")
elif password == "SECRET":
  print("Welcome Jack")
elif password == "Secret":
  print("Welcome Bob")
else:
  print("Not welcome")
