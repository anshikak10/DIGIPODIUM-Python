# wap to find hypotenuse using Pythagoras theorem

# function definition
def pythagoras():
    per = int(input("Enter the perpendicular of the triangle: "))
    base = int(input("Enter the base of the triangle: "))
    hyp = (per**2 + base**2)**0.5
    print(hyp)

# function call
pythagoras()
pythagoras()