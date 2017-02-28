#-*- coding:utf-8 -*-
#源代码
def s():
	a=1
	b=2
	print(a+b)

#编译后的字节码
what_to_execute={
	#指令列表
	"instructions":[("LOAD_VALUE",0),
					("STORE_NAME",0),
					("LOAD_VALUE",1),
					("STORE_NAME",1),
					("LOAD_NAME",0),
					("LOAD_NAME",1),
					("ADD_TWO_VALUES",None),
					("PRINT_ANSWER",None),],
	#常量列表，变量列表
	"numbers":[1,21],
	"names":["a","b"]}

class Interpreter:
	def __init__(self):
		self.stack=[]
		#存储变量映射关系的字典变量
		self.environment={}

	def STORE_NAME(self,name):
		val=self.stack.pop()
		self.environment[name]=val

	def LOAD_NAME(self,name):
		val=self.environment[name]
		self.stack.append(val)

	def LOAD_VALUE(self,number):
		self.stack.append(number)

	def PRINT_ANSWER(self):
		answer=self.stack.pop()
		print(answer)

	def ADD_TWO_VALUES(self):
		first_num=self.stack.pop()
		second_num=self.stack.pop()
		total=first_num+second_num
		self.stack.append(total)

	#解析指令
	def parse_argument(self,instruction,argument,what_to_execute):
		#使用常量列表的方法
		numbers=["LOAD_VALUE"]
		#使用变量列表的方法
		names=["LOAD_NAME","STORE_NAME"]

		if instruction in numbers:
			argument=what_to_execute["numbers"][argument]
		elif instruction in names:
			argument=what_to_execute["names"][argument]

		return argument

	#执行代码
	def run_code(self,what_to_execute):
		instructions=what_to_execute["instructions"]
		for each_step in instructions:
			instruction,argument=each_step
			argument=self.parse_argument(instruction,argument,what_to_execute)

			if instruction=="LOAD_VALUE":
				self.LOAD_VALUE(argument)
			elif instruction=="ADD_TWO_VALUES":
				self.ADD_TWO_VALUES()
			elif instruction=="PRINT_ANSWER":
				self.PRINT_ANSWER()
			elif instruction=="STORE_NAME":
				self.STORE_NAME(argument)
			elif instruction=="LOAD_NAME":
				self.LOAD_NAME(argument)

	#对run_code()进行的改进
	def execute(self,what_to_execute):
		instructions=what_to_execute["instructions"]
		for each_step in instructions:
			instruction,argument=each_step
			argument=self.parse_argument(instruction,argument,what_to_execute)
			bytecode_method=getattr(self,instruction)
			if argument is None:
				bytecode_method()
			else:
				bytecode_method(argument)

interpreter=Interpreter()
interpreter.execute(what_to_execute)
