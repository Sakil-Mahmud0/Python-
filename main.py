# # Odd or even exercise
# number=int(input("Which number do you want to check: "))
# if number%2==0:
#   print("This number is even")
# else:
#   print("This number is odd")

# using if,elif,else condition
print("Wellcome to the rollercoster")
height=int(input("What is your height in cm?: "))

if height>=120:
  print("You can ride in rollercoster")
  age=int(input("What is your age?: "))
  if age <=12:
    print("please pay $5")
  elif age<=18:
    print("please pay $7")
  else:
    print("Please pay $12")
else:
  print("You can not ride in rollercoster")

  # BMI Calculator with comments

  height=float(input("What is your height in m : "))
  weight=float(input("What is your weights in kg ?: "))
  bmi=round(weight/height**2)
  if bmi<18.5:
    print(f"Your bmi {bmi}, you are underweighted")
  elif bmi<25:
    print(f" your bmi {bmi}, you are normal")
  elif bmi<30:
    print(f"Your bmi {bmi},you are overweight")
  elif bmi<35:
    print(f"Your bmi {bmi},you are obes")
  else:
    print(f"Your bmi {bmi} clinically obes")

# Calculating Leap Year
year=int(input("Which year do you want to check?: "))

if year%4==0:
  if year%100==0:
  
    if year%400==0:
      print(f"{year} year is leap year")
    else:
      print(f"{year} is not leap year")

  else:
    print(f"{year} is not leap year")
else:
  print(f"{year} is not leap year")

# using if,elif,else condition and add another statement
print("Wellcome to the rollercoster")
height=int(input("What is your height in cm?: "))
bill=0

if height>=120:
  print("You can ride in rollercoster")
  age=int(input("What is your age?: "))
  if age <=12:
    bill=5
    
    print("please pay $5")
  elif age<=18:
    bill=7
    print("please pay $7")
  else:
    bill=12
    print("Please pay $12")
  wants_photo=input("Do you want to take photo? Y,N.")
  if wants_photo =="Y":
    bill+=3
  
  print(f"Your final bill {bill} is")
  

else:
  print("You can not ride in rollercoster")

# pizza order project
size=input("What types of pizza you want?,S,M,L :")
add_peparoni=input("Do you want peoparoni?Y,N: ")
extra_cheez=input("Do you want extra cheez? Y,N: ")
if size=="S":
  price=15
  if add_peparoni=="Y":

    price+=2
    if extra_cheez=="Y":
      price+=1
  print(f"Your pizza price is {price}")
elif size=="M":
  price=20
  if add_peparoni=="Y":
    price+=3
    if extra_cheez=="Y":
      price+=1
  print(f"Your pizza price is {price}")
else:
  price=25
  if add_peparoni=="Y":
    price+=2
    if extra_cheez=="Y":
      price+=1
  print(f"Your pizza price is {price}")

  # Another way 

size=input("What types of pizza you want?,S,M,L :")
add_peparoni=input("Do you want peoparoni?Y,N: ")
extra_cheez=input("Do you want extra cheez? Y,N: ")
price=0
if size=="S":
  price+=15

elif size=="M":
  price=20
else:
  price=25

if add_peparoni=="Y":


  price+=2
else:

  price+=3
  
if extra_cheez=="Y":
  price+=1
print(f"Your pizza price is {price}")
