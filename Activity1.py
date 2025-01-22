print("~~~~Half Pyramid Made Of (*)~~~~\n")

num_of_rows = int(input("Enter The Number Of Rows You'd Like: "))

for x in range(num_of_rows):
    for y in range(x+1):
    
        print ("* ", end=" ")

    print()