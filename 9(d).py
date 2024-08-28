s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
  print(i)
counts1=0
counts2=0
letters=set.intersection(set(s1),set(s2))
for letter1 in set(s1):
    counts1+=s2.count(letter1)
for letter2 in set(s2):
    counts2+=s1.count(letter2)
counts=min(counts1,counts2)
print("count of common letters are:",counts)
