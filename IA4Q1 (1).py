# Name: Nhu-Quynh Ho, 
# Email: nho19@student.gsu.eduimport math

d = float(input("Enter the distance to the skier (meters): "))
theta_degrees = float(input("Enter the angle in degrees: "))

theta_radians = math.radians(theta_degrees)

h = d * math.sin(theta_radians)
x = d * math.cos(theta_radians)
L = h / math.tan(theta_radians)

print("Vertical height:", round(h, 2), "meters")
print("Horizontal distance:", round(x, 2), "meters")
print("Ramp length:", round(L, 2), "meters")