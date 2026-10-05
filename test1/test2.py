principal = int(input("Enter Principal Amount: "))
rate = int(input("Enter Rate of Interest: "))
time = int(input("Enter Time: "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)