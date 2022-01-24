# q

l = [8,10,5]
no_of_rows = 25

arr = [[0 for i in range(no_of_rows)] for j in range(no_of_rows)]
for i in arr:
   print(i)

print("------------------------------------------------------------------------------")
arr[l[0]][l[1]]=l[2]
for i in arr:
   print(i)

f=1
for i in range (l[0]-l[2],l[0],1):
   for j in range(l[1],f,1):
      arr[i][l[1]+f]=2
      print(arr[i][l[1]+f])
      print("j is "+ j )
   f= f+1
   arr[i][10]=1 
   print(arr[i][10])

for i in arr:
   print(i)
