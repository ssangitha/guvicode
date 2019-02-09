s=input()
if all(i is"a" or i is"b" or i in ["a","b"] for i in s):
	print("yes")
else:
	print("no")
