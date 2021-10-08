# Author MEE 10/4/21

h = input("Your Height (cm) ")
w = input("Your Weight (kg) ")

bmi = w / (h ** 2) * 10000

if bmi < 19:
    print("You are skinny")
elif bmi < 25:
    print("You are healthy")
elif bmi < 30:
    print("You are fat")
elif bmi < 40:
    print("You are really fat")
else:
    print("You are extremely fat")