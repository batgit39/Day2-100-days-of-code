print("Welcome to Tip Calculator!")

bill = int( input( "How much was the total Bill?\n" ))
share = int( input("How many people do you want to share between?\n"))
tip_per = float( input("How much percentage of tip did you give?\n"))

tip = (bill*tip_per)/100
per_person = (bill + tip) / share

print("Each person should pay: ")
print(round( per_person, 2 ))

