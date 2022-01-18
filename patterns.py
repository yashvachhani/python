# incrising tringle
n = 5

for i in range(n):
   for j in range(i+1):
      print(j+1,end="")
   print("")


# decrecing tringle
for i in range(n):
   for j in range(n-i,0,-1):
      print(i+1,end="")
   print("")


for i in range(-n,0):
   for j in range(abs(i)):   
      print(abs(i),end="")
   print("")


# final pattarn

for i in range(n):
   for j1 in range(n-i,0,-1):
      print(" ",end="")
   for j2 in range(i):
      print(i,end="")
   for j3 in range(i-1):
      print(i,end="")
   print("")
#print("\033[A",end="")

for i in range(n):
   for j1 in range(i):
      print(" ", end="")
   for j2 in range(n-i,0,-1):
      print(abs(n-i), end="")
   for j3 in range((n-(i)),1,-1):
      print(abs(n-i), end="")
   print("")



# q
no_of_rows = 50
arr = [[0 for i in range(no_of_rows)] for j in range(no_of_rows)]
for i in arr:
   print(i)



