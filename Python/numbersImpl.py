def solve(expr, lvl=0):
	if lvl == 0:
		if type(expr) == num:
			return num
			
		if expr.Type == "NUMB":
			return expr.Args[0]
			
		if expr.Type == "ABS":
			arg1 = solve(expr.Args[0], lvl)
			if type(arg1) == num:
				return arg1.abs()
			if arg1.Type == "NUMB":
				return arg1.Args[0].abs()
	return expr


class NumVal:
	def __init__(self):
		pass

	def Validate(self, num):
		if num.Type == "INT":
			self.INT(num)
		elif num.Type == "FLOAT":
			self.FLOAT(num)
		elif num.Type == "ANGLE":
			self.ANGLE(num)
		elif num.Type == "RAD":
			self.RAD(num)
		elif num.Type == "PI":
			self.PI(num)
		elif num.Type == "E":
			self.E(num)
		elif num.Type == "EPSILON":
			self.EPSILON(num)
		elif num.Type == "OMEGA":
			self.OMEGA(num)

		else:
			raise Exception("Num of type", num.Type, "is not (yet) validatable")

	def INT(self, num):
		pass

	def FLOAT(self, num):
		pass

	def ANGLE(self, num):
		pass

	def RAD(self, num):
		pass

	def PI(self, num):
		pass

	def E(self, num):
		pass

	def EPSILON(self, num):
		pass

	def OMEGA(self, num):
		pass


class ExpVal:
	def __init__(self):
		pass

	def Validate(self, exp):
		if exp.Type == "NUMB":
			self.NUMB(exp)
		elif exp.Type == "NEG":
			self.NEG(exp)
		elif exp.Type == "ABS":
			self.ABS(exp)
		elif exp.Type == "ADD":
			self.ADD(exp)
		elif exp.Type == "SUB":
			self.SUB(exp)
		elif exp.Type == "MUL":
			self.MUL(exp)
		elif exp.Type == "DIV":
			self.DIV(exp)
		elif exp.Type == "POW":
			self.POW(exp)
		elif exp.Type == "ROOT":
			self.ROOT(exp)
		else:
			raise Exception("expression of type:", exp.Type, "is not (yet) validatable")

	def ValidateExprList(self, list):
		for i in range(len(list)):
			part = list[i]
			partType = type(part)
			if partType == expression:
				pass
			elif partType == num:
				list[i] = expression("NUMB", [part])
			elif partType == int:
				list[i] = expression("NUMB", [num("INT", part)])
			elif partType == float:
				list[i] = expression("NUMB", [num("FLOAT", part)])
			else:
				raise Exception(partType, "can't (yet) be converted to an expression")

	def NUMB(self, exp):
		if len(exp.Args) != 1:
			raise Exception("a NUMB expression should only have 1 argument, got", len(exp.Args))

		typeArgs0 = type(exp.Args[0])

		if typeArgs0 == expression:
			if exp.Args[0].Type == "NUMB":
				exp.Args[0] = exp.Args[0].Args[0]
			else:
				raise Exception("a NUMB expression can't hold another expression")

		elif typeArgs0 == num:
			pass

		elif typeArgs0 == int:
			exp.Args[0] = num("INT", exp.Args[0])

		elif typeArgs0 == float:
			exp.Args[0] = num("FLOAT", exp.Args[0])

		else:
			raise Exception("NUMB expression can't (yet) hold an object of type:",
				typeArgs0)

	def NEG(self, exp):
		if len(exp.Args) != 1:
			raise Exception("a NEG expression should only have 1 argument, got", len(exp.Args))

		self.ValidateExprList(exp.Args)

	def ABS(self, exp):
		if len(exp.Args) != 1:
			raise Exception("an ABS expression should only have 1 argument, got", len(exp.Args))

		self.ValidateExprList(exp.Args)

		if exp.Args[0].Type == "NUMB" and exp.Args[0].Args[0].Val == 0:
			exp.Type = "NUMB"
			exp.Args[0] = num(exp.Args[0].Args[0].Type, 0)

	def ADD(self, exp):
		if len(exp.Args) < 2:
			raise Exception("an ADD expression should at least have 2 arguments, got", len(exp.Args))

		self.ValidateExprList(exp.Args)

	def SUB(self, exp):
		if len(exp.Args) != 2:
			raise Exception("a SUB expression should have 2 arguments, got", len(exp.Args))

		self.ValidateExprList(exp.Args)

	def MUL(self, exp):
		if len(exp.Args) < 2:
			raise Exception("a MUL expression should at least have 2 arguments, got", len(exp.Args))

		self.ValidateExprList(exp.Args)

	def DIV(self, exp):
		if len(exp.Args) != 2:
			raise Exception("a DIV expression should have 2 arguments, got", len(exp.Args))

		self.ValidateExprList(exp.Args)

		if exp.Args[1].Type == "NUMB" and exp.Args[1].Args[0].Val == 0:
			raise Exception("Can't divide by zero, try using epsilon")

	def POW(self, exp):
		if len(exp.Args) != 2:
			raise Exception("a POW expression should have 2 arguments, got", len(exp.Args))

		self.ValidateExprList(exp.Args)

	def ROOT(self, exp):
		if len(exp.Args) != 2:
			raise Exception("a ROOT expression should have 2 arguments, got", len(exp.Args))

		self.ValidateExprList(exp.Args)


numTypes = ["INT", "FLOAT", "ANGLE", "RAD", "PI", "E", "EPSILON", "OMEGA"]


class num:
	def __init__(self, Type, Val=None):
		self.Type = Type.upper()
		self.Val = Val

		if not self.Type in numTypes:
			raise Exception(self.Type, "is not a numType")

		NumValidator = NumVal()
		NumValidator.Validate(self)

	def __str__(self):
		if self.Type == "INT":
			return str(int(self.Val))
		if self.Type == "FLOAT":
			return str(float(self.Val))
		if self.Type == "ANGLE":
			return str(self.Val) + "\u00B0"
		if self.Type == "RAD":
			return str(self.Val) + "\u03C0"
		if self.Type == "PI":
			return "\u03C0"
		if self.Type == "E":
			return "e"
		if self.Type == "EPSILON":
			return "\u03B5"
		if self.Type == "OMEGA":
			return "\u03C9"

		raise Exception(self.Type + " can't (yet) be printed")
	def abs(self):
		if self.Type == "INT" or self.Type == "FLOAT" or self.Type == "ANGLE" or self.Type == "RAD":
			return num(self.Type, abs(self.Val))
		return self


expTypes = ["NUMB", "NEG", "ABS", "ADD", "SUB", "MUL", "DIV", "POW", "ROOT"]


class expression:
	def __init__(self, Type, Args):
		self.Type = Type.upper()
		self.Args = Args

		if not self.Type in expTypes:
			raise Exception(self.Type, 'is not an exprType')
		if type(self.Args) != list:
			raise Exception("Args should be a list, got a", type(self.Args))

		# converts possible different inputs to expressions
		ExpValidator = ExpVal()
		ExpValidator.Validate(self)

	def __str__(self):

		if self.Type == "NUMB":
			return f"{self.Args[0]}"

		if self.Type == "NEG":
			if self.Args[0].Type == "NUMB":
				return f"-{self.Args[0]}"
			else:
				return f"-({self.Args[0]})"

		if self.Type == "ABS":
			return f"|{self.Args[0]}|"

		if self.Type == "ADD":
			str = f""
			for exp in self.Args:
				if exp.Type == "NUMB" or exp.Type == "NEG" or exp.Type == "ABS" or exp.Type == "POW" or exp.Type == "ROOT":
					str += f"{exp} + "
				else:
					str += f"({exp}) + "
			return str[:-3]

		if self.Type == "SUB":
			if self.Args[0].Type == "NUMB":
				if self.Args[1].Type == "NUMB":
					return f"{self.Args[0]} - {self.Args[1]}"
				return f"{self.Args[0]} - ({self.Args[1]})"
			if self.Args[1].Type == "NUMB":
				return f"({self.Args[0]}) - {self.Args[1]}"
			return f"({self.Args[0]}) - ({self.Args[1]})"

		if self.Type == "MUL":
			str = f""
			for exp in self.Args:
				if exp.Type == "NUMB" or exp.Type == "NEG" or exp.Type == "ABS" or exp.Type == "POW" or exp.Type == "ROOT":
					str += f"{exp} * "
				else:
					str += f"({exp}) * "
			return str[:-3]

		if self.Type == "DIV":
			if self.Args[0].Type == "NUMB":
				if self.Args[1].Type == "NUMB":
					return f"{self.Args[0]} / {self.Args[1]}"
				return f"{self.Args[0]} / ({self.Args[1]})"
			if self.Args[1].Type == "NUMB":
				return f"({self.Args[0]}) / {self.Args[1]}"
			return f"({self.Args[0]}) / ({self.Args[1]})"

		if self.Type == "POW":
			if self.Args[0].Type == "NUMB":
				if self.Args[1].Type == "NUMB":
					return f"{self.Args[0]} ^ {self.Args[1]}"
				return f"{self.Args[0]} ^ ({self.Args[1]})"
			if self.Args[1].Type == "NUMB":
				return f"({self.Args[0]}) ^ {self.Args[1]}"
			return f"({self.Args[0]}) ^ ({self.Args[1]})"

		if self.Type == "ROOT":
			if self.Args[0].Type == "NUMB":
				if self.Args[1].Type == "NUMB":
					return f"{self.Args[0]} ^ (1/{self.Args[1]})"
				return f"{self.Args[0]} ^ (1/({self.Args[1]}))"
			if self.Args[1].Type == "NUMB":
				return f"({self.Args[0]}) ^ (1/{self.Args[1]})"
			return f"({self.Args[0]}) ^ (1/({self.Args[1]}))"

		raise Exception(self.Type, "has not yet a supported str type")