user_input=int(input("Enter the  size of the pattern: "))
rows=0
while rows<=user_input:
    column=0
    for column in range(user_input):
         print("*" , end="")
         column+=1
        
    print()
    rows+=1