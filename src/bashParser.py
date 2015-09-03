import pyparsing
from sys import argv

class parser:
	def __init__(self):
		self.varLiteral = pyparsing.Word(pyparsing.alphas, pyparsing.alphanums + '_').setResultsName("#literal:")
		self.exprTokens = pyparsing.Word(pyparsing.printables, excludeChars="\n ;")
		self.expr = pyparsing.Group(pyparsing.OneOrMore(self.exprTokens) + pyparsing.oneOf("\n ;"))
		self.List = pyparsing.OneOrMore(self.expr).setResultsName("#ListOfExpressions")
		self.semicolon = pyparsing.Literal(";")
		self.newLine = pyparsing.Literal('\n')

	# Takes stringArg and returns parsed dictionary
	def variableDeclaration(self, stringArg):
		# Grammar for basic atoms
		quotString = pyparsing.Word(pyparsing.printables).setResultsName("#string:")

		# Grammar for other descriptor
		assignment = quotString
		equalTo = pyparsing.Suppress(pyparsing.Literal("="))

		# Assignment Expression
		assignmentExpression = (self.varLiteral + equalTo + assignment).setResultsName("#Assignment_Expression:")

		# Reading and parsing from Standard arguments
		assignmentToken = assignmentExpression.parseString(stringArg)

		dictData = assignmentToken.asDict()

		return dictData

	# Takes stringArg as argument and returns dictionary
	def for_loop(self, stringArg):

		# Grammar Defination
		name = (self.varLiteral).setResultsName("#name:")
		words = pyparsing.Group(pyparsing.OneOrMore(pyparsing.Word(pyparsing.printables, excludeChars=";"))).setResultsName("#list")
		For = pyparsing.Literal("for")
		In = pyparsing.Literal("in")
		Do = pyparsing.Literal("do")
		Done = pyparsing.Literal("done")

		for_expr = (For + name + In + words + self.semicolon + Do + pyparsing.Optional(self.newLine) + self.List + pyparsing.Optional(self.newLine) + Done).setResultsName("#for_expression")

		for_exprTokens = for_expr.parseString(stringArg)

		dictData = for_exprTokens.asDict()

		return dictData

	# Don't read it is buggy
	def if_cond(self, stringArg):

		# Grammar Definition
		If = pyparsing.Literal("if")
		Then = pyparsing.Literal("then")
		Fi = pyparsing.Literal("fi")
		Predicate = pyparsing.OneOrMore(self.expr).setResultsName("#predicate")
		consqCommands = pyparsing.OneOrMore(self.expr).setResultsName("#consequent")

		Elif = pyparsing.Literal("elif")
		morePredicate = pyparsing.OneOrMore(self.expr).setResultsName("#morePredicate")
		moreConsequent = pyparsing.OneOrMore(self.expr).setResultsName("#moreConsequent")
		optElif = Elif + morePredicate + Then + pyparsing.Optional(self.newLine) + moreConsequent

		Else = pyparsing.Literal("else")
		altConsequent = pyparsing.OneOrMore(self.expr).setResultsName("#alternateConsequent")
		optElse = Else + altConsequent + pyparsing.Optional(self.newLine)

		if_expr = (If + Predicate + pyparsing.Optional(self.newLine) + Then + \
			pyparsing.Optional(self.newLine) + consqCommands + \
			pyparsing.Optional(optElif) + pyparsing.Optional(optElse) + \
			pyparsing.Optional(self.newLine) + Fi).setResultsName("#if_expression")

		if_exprTokens = if_expr.parseString(stringArg)

		dictData = if_exprTokens.asDict()

		for x in dictData:
			print x, dictData[x]

a = parser()
s = "asdsad_=3234"
a.variableDeclaration(s)
q = "for i in 232 324 45 4 7 ^; do\necho $i;\necho \"sd\";\ndone"
a.for_loop(q)
a.fn()
l = "if [ $count -eq 100 ];\nthen\n  echo \"Count is 100\";\nfi"
print l
a.if_cond(l)