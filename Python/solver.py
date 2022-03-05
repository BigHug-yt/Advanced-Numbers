from numbersImpl import num, expression

class solver:
	def __init__(self):
		pass
	class lvl_0:
		def __init__(self):
			pass
		def numb(self,expr):
			return expr.Args[0]
			
		def abs(self,expr):
			arg1 = solve(expr.Args[0],0)
			if type(arg1) == num:
				return arg1.abs()
			if type(arg1) == expression:
				if arg1.Type == "NUMB":
					return arg1.Args[0].abs()
				if arg1.Type == "ABS":
					return arg1
				if arg1.Type == "NEG" and arg1.Args[0].Type == "NUMB":
					return arg1.Args[0].Args[0]
				return arg1
			
			
		def solve(self,expr):
			if type(expr) == num:
				return num
				
			if type(expr) == expression:
				if expr.Type == "NUMB":
					return self.numb(expr)
				if expr.Type == "ABS":
					return self.abs(expr)
				return expr
			raise Exception(f"type {type(expr)} can't yet be solved on this lvl")


				
	def solve(self,expr,lvl):
		if lvl == 0:
			lvl0 = self.lvl_0()
			return lvl0.solve(expr)
		raise Exception(f"{lvl} is not a valid solve lvl")




def solve(expr, lvl=0):
	Solver = solver()
	return Solver.solve(expr,lvl)
