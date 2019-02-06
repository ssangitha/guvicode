s=input()
l1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l=s.lower()
if all(i in l for i in l1):
	print("yes")
else:
	print("no")
 #...panagram.....
