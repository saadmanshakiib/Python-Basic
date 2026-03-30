# number = int(input("Enter 1st Number"))
# number2 = int(input("Enter 2nd Number"))
# n = number + number2
# if n%2 == 0:
#     print("Even")
# else : print("Odd")

days = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
}


def monday():
    return "Start of the week"
def sunday():
    return "Start of the weekend"

print(monday())


print(days.get(3))
day = 9
match (day):
    case 1: print("Robibar")
    case 2: print("Sombar")
    case 3: print("Mongolbar")
    case 4: print("Budhbar")
    case 5: print("Brihospotibar")
    case 6: print("Sukrobar")
    case 7: print("Sonibar")
    case _: print("Bhul")

