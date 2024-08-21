# Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side1 = float(input("Enter the length of Side_1\n"))
side2 = float(input("Enter the length of Side_2\n"))
side3 = float(input("Enter the length of Side_3\n"))

if side1 == side2 == side3:
    print("This is an Equilateral Triangle")
elif side1 == side2 != side3 or side2 == side3 != side1 or side3 == side1 != side2:
    print("This is an Isosceles Triangle")
else:
    print("This is a Scalene Triangle")