# Interpreter
python实现python解释器

1.该python解释器是一个模拟堆栈机器的虚拟机

2.基本指令：LOAD_VALUE,将数据压入栈中，STORE_NAME，将栈顶内容存入变量,LOAD_NAME,将变量的内容压入栈中

dis是一个字节码反汇编器

3.LOAD_CONST相当于LOAD_VALUE,STORE_FAST相当于STORE_NAME

4.帧:帧包含了一段代码运行所需要的信息与上下文环境，帧在代码执行时被动态地创建与销毁，每一个帧的创建对应一次函数调用,所以每一个帧都有一个code object与其关联,同时一个code object可以拥有多个帧，因为一个函数可以递归调用自己多次

5.调用栈:每当你在当前函数内调用一次函数就在当前调用栈上压入所调用的函数的帧，在所调用函数返回时再将该帧弹出
  数据栈:执行字节码操作时使用的栈
  块栈:用于特定的控制流，比如循环与异常处理;每一个帧都拥有自己的数据栈与块栈
