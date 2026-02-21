# Name: Nhu-Quynh Ho, 
# Email: nho19@student.gsu.edu

year = int(input("Enter year: "))
month = input("Enter month (three letters): ")
day = int(input("Enter day: "))

valid = True

if year <= 0:
    valid = False

leap = False
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True

if month == "Jan" or month == "Mar" or month == "May" or month == "Jul" or month == "Aug" or month == "Oct" or month == "Dec":
    if day < 1 or day > 31:
        valid = False

elif month == "Apr" or month == "Jun" or month == "Sep" or month == "Nov":
    if day < 1 or day > 30:
        valid = False

elif month == "Feb":
    if leap:
        if day < 1 or day > 29:
            valid = False
    else:
        if day < 1 or day > 28:
            valid = False
else:
    valid = False

if valid:
    print("Valid date")
else:
    print("Invalid date")