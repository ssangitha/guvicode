s=input()
lx=['a','e','i','o','u']
if s in lx:
  print("Vowel")
elif s.isalpha():
  print("Consonant")
else:
  print("Invalid")
