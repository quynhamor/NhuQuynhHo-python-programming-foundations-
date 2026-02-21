# Name: Nhu-Quynh Ho, 
# Email: nho19@student.gsu.educh = input("Enter a letter (A-G): ")

if len(ch) != 1:
    print(ch, "is an invalid input")
elif ch in "ABCabc":
    print(ch, "is a low note")
elif ch in "DEFGdefg":
    print(ch, "is a high note")
else:
    print(ch, "is an invalid input")