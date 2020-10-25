"""
5.5. Converting an Integer to a String in Any Base

All recursive algorithms must obey three important laws:

A recursive algorithm must have a base case.

A recursive algorithm must change its state and move toward the base case.

A recursive algorithm must call itself, recursively.
https://runestone.academy/runestone/books/published/pythonds
"""
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))


