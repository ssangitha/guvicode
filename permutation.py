import itertools
s=input()
a=itertools.permutations(s)
for i in list(a):
	print (''.join(i))
#.......permutation,,,......
