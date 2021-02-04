print("Welcome to Dream Rollercoaster ")

print("Before your ride you should take your ticket")

bill = 0

height = int(input("please enter your height\n"))

if height >= 120:
    print("Hey buddy you can ride on Rollercoaster")

    age = int(input("Please enter your age!!\n"))
    if age < 12:
        bill = 5
        print("you are a child and your ticket cost is $5")

    elif age < 18:
        bill = 25
        print("you are a teenager so your ticket cost is $25")

    else:
        bill = 50
        print("You are an adult so your ticket cost is $50")

    camera = input("Do you have a camera? Y or N.\n")
    if camera == "Y":
        print("hey buddy you want to take photos for that you need to pay some more")

    wants_photo = input("want to click photo? Y or N.\n")
    if wants_photo == "Y":
        bill = bill + 5

    print(f"Your total bill is {bill}")

    def welcome():
        print("Now Have your great adventure ahead")

    welcome()
else:
    print("Sorry You can not have your ride, you can come when u r grown enough& come here we are always here to welcome you")
