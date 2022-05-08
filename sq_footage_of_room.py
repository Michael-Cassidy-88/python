# this is a basic exercise for inputting the necessary dimensions of a room to calculate the square footage

length = float(input("Length of room: ")) # prompt that requests length of room
width = float(input("Width of room: ")) # prompt that requests width of room
area = length * width # new variable "area" is equal to the product of "length" * "width"
print("Area =", round(area, 2)) # prints the "area" rounding the number to two decimal places