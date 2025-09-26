pattern = int(input("Enter the  size of the pattern:"))
rows=0
while rows<=pattern:
    column=0
    for column in range(pattern):
         print("*" , end="")
         column+=1
        
    print()
    rows+=1
