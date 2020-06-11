def test(x):
	a = x
	if a == 0:
		return a
	else:
		return "b"

var = test(2)

try:
	assert var == 'io' 
except AssertionError as e:
	raise e
else:
	print(var)