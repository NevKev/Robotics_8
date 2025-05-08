
birth_year = int(input("What year were you born? "))

if birth_year >= 1925 and birth_year <= 1946:
  print("You're a Traditionalist! ")
elif birth_year >= 1947 and birth_year <= 1964:
  print("You're a Baby Boomer!")
elif birth_year >= 1965 and birth_year <= 1981:
  print("You're part of Generation X! ")
elif birth_year >= 1982 and birth_year <= 1995:
  print("You're a Millennial! ")
elif birth_year >= 1996 and birth_year <= 2015:
  print("You're part of Generation Z! ")
else:
  print("The year you entered is not in our generation list! ")
