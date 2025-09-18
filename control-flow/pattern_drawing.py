size=int(input("Enter the  size of the pattern:"))
rows=4
column=4
i=0
while i<=rows + 1:
    j=0
    while j<=column +1:
        for j in range(i):
         print("*" , end="")
        j+=1
        
        print()
        i+=1