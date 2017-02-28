import dis
def cond():
	x=3
	if x<5:
		return 'yes'
	else:
		return 'no'

print(cond.__code__.co_code)
print(list(bytearray(cond.__code__.co_code)))
dis.dis(cond)
print(dis.opname[100])
print(dis.opname[125])

def loop():
		x=1
		while x<5:
			if x==3:
				break
			x=x+1
			print x
		return x
loop()