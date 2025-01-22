print("Floyd's Triangle\n")

num_of_rows = int(input("Enter The Number Of Rows You'd Like: "))

z = 0

for x in range(num_of_rows):
    for y in range(x+1):
        z += 1
    
        print (z, end=" ")

    print()