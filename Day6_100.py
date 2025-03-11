#This is for day 6 and this is what I learned

print("===== Login System =====")
username = input("Username: ")
password = input("Password: ")

if username == "Ray" and password == "secret":
  print(f"Welcome back Ray!")
elif username == "Jack" and password == "password123":
  print(f"Hey Jack!")
elif username == "Emma" and password == "securepass":
  print(f"Hello Emma!")
else:
  print("I don't recognize you. Access denied.")

print("===== End of program =====")
