# Python Algorithm

# Algorithm for finding minimum and maximum numbers


numbers = [12, 23, 100, 53, 34, 76, 86,99, 43, 67, 9,1,56,190,567, -24]

min = None
max = None
for i in numbers:
    # sets initial min max
    if(min == None):
        min = i
    if(max == None):
        max = i
    # min max algorithm
    if( i < min):
        min = i
    if(i > max):
        max = i

print(f"The lowest number in the array is: {min}")
print(f"The largest number in the array is: {max}")


