def pr (string, num):
	print(string, " ", num)
	pass 

def summ(a, b): 
	res = a + b
	return res
def test (*args):
	print(args)
	pass

pr ("Number is", 56)
a = summ (23, 56)
pr("Number is", a)

test("Hi", 23,6.22)

mult = lambda x,y: x*y
print(mult(2,5))
