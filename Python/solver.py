from numbersImpl import num, expression

def Neg(arg, lvl):
	if arg.Type == "NUMB":
		if arg.Args[0].Type == "INT" or arg.Args[0].Type == "FLOAT" or arg.Args[0].Type == "ANGLE" or arg.Args[0].Type == "RAD":
			return expression("NUMB", [num(arg.Args[0].Type, -arg.Args[0].Val)])
		return expression("NEG", [arg])
	if arg.Type == "NEG":
		return arg.Args[0]

def Abs(arg, lvl):
	if arg.Type == "NUMB":
		if arg.Args[0].Type == "INT" or arg.Args[0].Type == "FLOAT" or arg.Args[0].Type == "ANGLE" or arg.Args[0].Type == "RAD":
			return expression("NUMB", [num(arg.Args[0].Type, abs(arg.Args[0].Val))])
		return expression("ABS", [arg])
	if arg.Type == "ABS":
		return expression("ABS", [arg.Args[0]])

def Add(arg1, arg2, lvl):
	if arg1.Type == "NUMB":
		if arg2.Type == "NUMB":
			if arg1.Args[0].Type == "INT" and arg2.Args[0].Type == "INT":
				return expression("NUMB", [num("INT", arg1.Args[0].Val+arg2.Args[0].Val)])
			if arg1.Args[0].Type == "INT" and arg2.Args[0].Type == "FLOAT":
				return expression("NUMB", [num("FLOAT", arg1.Args[0].Val+arg2.Args[0].Val)])
			if arg1.Args[0].Type == "FLOAT" and arg2.Args[0].Type == "INT":
				return expression("NUMB", [num("FLOAT", arg1.Args[0].Val+arg2.Args[0].Val)])
			if arg1.Args[0].Type == "FLOAT" and arg2.Args[0].Type == "FLOAT":
				return expression("NUMB", [num("FLOAT", arg1.Args[0].Val+arg2.Args[0].Val)])
			if arg1.Args[0].Type == "ANGLE" and arg2.Args[0].Type == "ANGLE":
				return expression("NUMB", [num("ANGLE", arg1.Args[0].Val+arg2.Args[0].Val)])
			if arg1.Args[0].Type == "RAD" and arg2.Args[0].Type == "RAD":
				return expression("NUMB", [num("RAD", arg1.Args[0].Val+arg2.Args[0].Val)])

		if arg2.Type == "NEG":
			
			raise Exception(f"adding numbers with types {arg1.Args[0].Type} and {arg2.Args[0].Type} is not (yet) supported")
		raise Exception(f"adding {arg2.Type} to NUMB is not (yet) supported")
	raise Exception(f"adding to {arg1.Type} is not yet supported")
			
def solve(expr, lvl=0):
	if type(expr) == num:
		return expression("NUMB", [expr])
	if type(expr) == expression:
		if expr.Type == "NUMB":
			return expr
		if expr.Type == "NEG":
			arg = solve(expr.Args[0])
			return Neg(arg, lvl)
		if expr.Type == "ABS":
			arg = solve(expr.Args[0])
			return Abs(arg, lvl)
		if expr.Type == "ADD":
			prevarg = 0
			for arg in expr.Args:
				if prevarg == 0:
					prevarg = solve(arg, lvl)
				else:
					prevarg = Add(solve(prevarg, lvl), solve(arg, lvl), lvl)
			return solve(prevarg, lvl)

		raise Exception(f"solving an expression of type {expr.Type} is not (yet) implemented")

	raise Exception(f"solving a type {type(expr)} is not (yet) implemented")