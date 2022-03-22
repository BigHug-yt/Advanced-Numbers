from numbersImpl import expression, num
from solver import solve

print("all number variants:\n")
print(Int := num("INT", 1)) # integer number
print(Float := num("FLOAT", 1.1)) # float number
print(Angle := num("ANGLE", 90)) # angle in degrees
print(Rad := num("RAD", 1)) # angle in radians (1 = 180 degrees)
print(Pi := num("PI")) # pi
print(E := num("E")) # e
print(Epsilon := num("EPSILON")) # epsilon
print(Omega := num("OMEGA")) # omega

print("\nAll NUMB expressions with the nums:\n")
print(NumbInt := expression("NUMB", [Int]))
print(NumbFloat := expression("NUMB", [Float]))
print(NumbAngle := expression("NUMB", [Angle]))
print(NumbRad := expression("NUMB", [Rad]))
print(NumbPi := expression("NUMB", [Pi]))
print(NumbE := expression("NUMB", [E]))
print(NumbEpsilon := expression("NUMB", [Epsilon]))
print(NumbOmega := expression("NUMB", [Omega]))

print("\nAll other expressions:")
print("Neg:")
print(Neg := expression("NEG", [Int]))
print("Abs:")
print(Abs := expression("ABS", [Int]))
print("Add:")
print(Add := expression("ADD", [Int, Float]))
print("Sub:")
print(Sub := expression("SUB", [Int, Float]))
print("Mul:")
print(Mul := expression("MUL", [Int, Float]))
print("Div:")
print(Div := expression("DIV", [Int, Float]))
print("Pow:")
print(Pow := expression("POW", [Int, Float]))
print("Root:")
print(Root := expression("ROOT", [Int, Float]))

print("\nExpressions can also be combined:\n")
print(expression("ADD", [Neg, Abs]))
print(expression("MUL", [Pow, Mul, Add, Neg]))

x = expression("add", [-2, 5])
y = expression("add", [-3, x])
z = expression("add", [x,y])
b = expression("neg", [-3])
a = expression("abs", [b])

print("\nAnd be solved:\n")
print(a)
print(solve(a))
print(x)
print(solve(x))
print(y)
print(solve(y))

print("\n\nOperator overloading:\n")
x=num("int",90)
y=num("pi")
z=x*y
b=z**z
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x+y+x)
print(b)