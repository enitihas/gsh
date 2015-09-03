from pyparsing import Word, alphas, alphanums, printables, ZeroOrMore, \
nums, Literal, Suppress, Group, QuotedString, removeQuotes, OneOrMore, \
oneOf, Optional
from sys import argv

class parser:
	def __init__(self):
		self.varLiteral = Word(alphas, alphanums + '_').setResultsName("#literal:")
		self.exprTokens = Word(printables, excludeChars="\n ;")
		self.expr = Group(OneOrMore(self.exprTokens) + oneOf("\n ;"))
		self.List = OneOrMore(self.expr).setResultsName("#ListOfExpressions")
		self.semicolon = Literal(";")
		self.newLine = Literal('\n')

	def variableDeclaration(self, stringArg):
		# Grammar for basic atoms
		quotString = Word(printables).setResultsName("#string:")

		# Grammar for other descriptor
		assignment = quotString
		equalTo = Suppress(Literal("="))

		# Assignment Expression
		assignmentExpression = (self.varLiteral + equalTo + assignment).setResultsName("#Assignment_Expression:")

		# Reading and parsing from Standard arguments
		assignmentToken = assignmentExpression.parseString(stringArg)

		dictData = assignmentToken.asDict()

		return dictData

	def for_loop(self, stringArg):

		# Grammar Defination
		name = (self.varLiteral).setResultsName("#name:")
		words = Group(OneOrMore(Word(printables, excludeChars=";"))).setResultsName("#list")
		For = Literal("for")
		In = Literal("in")
		Do = Literal("do")
		Done = Literal("done")

		for_expr = (For + name + In + words + self.semicolon + Do + Optional(self.newLine) + self.List + Optional(self.newLine) + Done).setResultsName("#for_expression")

		for_exprTokens = for_expr.parseString(stringArg)

		dictData = for_exprTokens.asDict()

		for x in dictData:
			print x, dictData[x]

		return dictData

	def if_cond(self, stringArg):
		If = Literal("if")
		Then = Literal("then")
		Else = Literal("else")
		Fi = Literal("fi")

		if_expr = (If + self.List + self.semicolon + Then + self.List + self.semicolon + \
			Else + self.List + self.semicolon + Fi).setResultsName("#if_expression")

		if_exprTokens = if_expr.parseString(stringArg)

		dictData = if_exprTokens.asDict()

		for x in dictData:
			print x, dictData[x]

a = parser()
s = "asdsad_=3234"
a.variableDeclaration(s)
q = "for i in 232 324 45 4 7 ^; do\necho $i;\necho \"sd\";\ndone"
a.for_loop(q)
