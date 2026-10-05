
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
radius = int(input("Enter radius: "))

pi = 3.14
area = (length * breadth) + (0.5 * pi * radius * radius)
perimeter = (2 * length) + breadth + (pi * radius)

print("Area =", area)
print("Perimeter =", perimeter)