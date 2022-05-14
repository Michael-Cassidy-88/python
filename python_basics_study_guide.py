#!/usr/bin/env python3.7  # this line gives you the ability to run a script in a virtual enviornment

# This is a full line comment

# print("Hello World!")  # Hello World example used to provide a trailing comment after a line of code

"""
This is a multiline string
There are no block comments in python
"""

"""
Variables and the Assignment Operator
"""
my_str = "This is a simple string" # Setting the variable my_str
# print(my_str)
my_str = "This is a reassigned string" # Reassigning the variable my_str
# print(my_str)
my_str += " addition"  # adding "addition" to the string
# print(my_str) 
my_str = my_str + " addition"  # adding another "addition" to the string using a different method
# print(my_str)
my_str = 1  # reassigning variable.  Variables in python are not statically typed. The new variable is an integer, rather than a string.
# print(my_str)
"""
Stings and String Operators
"""
# print('single quoted string')  # print a single quoted string, or string literal
# print("double quoted string")  # print a double quoted string
# print('''this is a triple #
# quoted multi-line string''')  # print a multiline string using triple quotes
# print("pass" + "word")  # print "password" by adding two strings together
# print("Ha" * 4) # print "HaHaHaHa" by multiplying a string and an integer
# print("my_string".find('t'))  # using find method to locate the positional index of "t" within the string. "t" is the 4th character. The positional index starts with 0.
# print("my_string".find('in'))  # prints the first location of the characters "in". "in" starts with the 6th character.
# print("UPPERlower".lower()) # prints the lowercase representation of all characters in the string.
# print("Tab\tSpacing") # prints the words with a large space in between.
# print("New\nLine") # prints the words with a new line in between.
# print("'Single' in Double") # prints single quotes around the specified characters within the double quotes.
#print('"Double" in Single') # prints double quotes around the specified characters within the single quotes.
"""
Numeric Operaotors
"""
# print(5e9) # prints the equivalent to 5 * 10 **9.
# print(5e9 == 5 * 10 ** 9) # prints the boolean value of whether or not 5e9 = 5 * 10 ** 9, which is True.

# print(5 // 3) # prints floor division where the output is how many times does 3 go into 5 evenly.
# print(5 % 3) # prints the modulus division where the output is the remainder of 5 / 3.
"""
Unary and Bitwise Operators
"""
a = 0b010 # variable "a" is equal to the binary for 2.
# print(a) # prints the variable "a".
# print(bin(a)) # prints the binary equivalent of the variable "a".
# print(~a) # prints the 2's compliment of our binary representation of the variable "a", which is (-a - 1) or (-1 * a - 1).
# print(bin(~a)) # print the binary equivalent of the 2's complement of the variable "a".

a = 0b1001 # reassigned variable "a".  This will be used as a bitwise operator.
b = 0b1100 # variable "b".  This will be used as a bitwise operator.
# print(bin(a | b)) # prints a "1" when there is a "1" in either bit position to give a new binary (Bitwise OR).
# print(bin(a & b)) # prints a "1" when there is a "1" in both positions, otherwise a "0" will be printed, giving a new binary (Bitwise AND).
# print(bin(a ^ b)) # prints a "1" only when there is only one "1" between both positions of each binary digit (Bitwise XOR).
# print(bin(a >> 2)) # prints the variable "a" but shifts the bit values sideways to the right by 2 decimals.  The rest of the binary values are removed.
# print(bin(a << 4)) # prints the variable "a" but shifts the bit values sideways to the left by 4 decimals.  For each position we shift, a "0" is added.
"""
Boolean Operators
"""
# print(not True) # prints the the opposite of True using the unary operator.
# print(True or False) # prints the equivalent of the bitwise OR operator, but a bit of 1 is equivalent to True, and 0 is equivalent to False.
# print(False or False) # prints the equivalent of the bitwise OR operator, but a bit of 1 is equivalent to True, and 0 is equivalent to False.
# print(True and False) # prints the equivalent of the bitwise AND operator, where both of the operands need to be true, to output the boolean True.
# print(True and True) # prints the equivalent of the bitwise AND operator, where both of the operands need to be true, to output the boolean True.
"""
Comparison Operators
"""
# print(ord('a')) # prints the numeric value that 'a' represents in python.
# print('bb' >= 'ba') # prints boolean value for the statement (greater than or equals to operator).
# print(1 == 1.0) # prints boolean value for the statement (equals operator).
# print(1 != 'a') # prints boolean value for the statement (not equals operator).
# print('a' is 'b') # prints boolean value for the statement (identity operator).
# print(id('a')) # prints the id of the object 'a'.
"""
Operator Priority
"""
# print((14 & 3) * 2 + 4) # prints the answer using operator precedence.
"""
Typecasting
"""
# print(float(1)) # prints the float value of the integer '1' using typecasting.
# print(int(1.3)) # prints the integer value of the float '1.3' using typecasting. Values don't round. They truncate.
# print(str(1)) # prints the string value of the integer '1' using typecasting. 
# print(bool(1)) # prints the boolean value of the integer '1' using typecasting.
# print(bool()) # prints the boolean value of the empty string using typecasting.
# print(1 and 0) # prints the value using the boolean operator on non-boolean operands (returns first falsy value or last truthy value).
# print(1 or 0) # prints the value using the boolean operator on non-boolean operands (returns first truthy value or last falsy value).
# print(not 1) # prints the value using the boolean operator on non-boolean operands (returns the opposite boolean value).
"""
Input Functions
"""
# Favorite = input("Favorite Color: ") # prompts the the user to enter their own answer to "Favorite Color". Your answer will represent the value for "Favorite".
# print(Favorite) # prints the value you typed in for "Favorite Color".
"""
Immutability of Strings
"""
my_str = "testing" # creates a string equal to "testing".
# print(my_str) # prints the value of the variable "my_str".
# print(my_str.capitalize()) # prints the value of the variable "my_str" starting with a capital letter.
# print(id(my_str)) # prints the ID of "my_str".
other_str = "testing" # creates another string, but uses the same variable as "my_str".
# print(id(other_str)) # prints the ID of "other_str" which will be the same ID as "my_str" because strings are immutable.
"""
Indexing and Slicing
"""
# print(len(my_str)) # prints the length of the variable of "my_str".
# print(my_str[0]) # prints the first item in the variable "my_str".
# print(my_str[len(my_str) - 1]) # prints the final item in the variable "my_str".
# print(my_str[-1]) # prints the final item in the variable "my_str".
# print(my_str[0:2]) # prints the first and second item in the variable "my_str".
# print(my_str[2:len(my_str)]) # prints the third through the last item in the variable "my_str".
# print(my_str[2:]) # prints the third through the last item in the variable "my_str".
# print(my_str[1:5:2]) # prints the second and fourth item in the variable "my_str" using a step value to grab every other item, represented by "2", up to the item before the sixth item.
# print(my_str[1::2]) # prints the the second item, then stepwise by 2 for the rest of the items in the variable "my_str".
# print(my_str[::-1]) # prints the variable "my_str" backwards.
"""
Lists
"""
my_list = [1, 2, 3, 4, 5] # creates a list.
# print(my_list) # prints the list "my_list".
# print(my_list[0]) # prints the first item in the list "my_list".
# print(my_list[0::2]) # prints the the first item, then stepwise by 2 for the rest of the items in the list "my_list".
my_list[0] = "a" # modifies the first item in "my_list" to 'a'.
# print(my_list) # prints the redefined list "my_list".
# print(my_list + [6, 7, 8, 9]) # adds items to my_list to make a new list.
# print(my_list) # prints "my_list" without the added items in the line above.
my_list += [6, 7, 8, 9] # adds items to the end of "my_list".
# print(my_list) # prints the new version of "my_list" with added items from line above.
my_list[1:3] = ["b", "c"] # slices items 2 and 3 from the list, and replaces them with 'b' and 'c' respectively.
# print(my_list) # prints the new list.
my_list[3:] = [] # removes the items to the left of the third item in "my_list".
# print(my_list) # prints the modified list.
del my_list[2] # deletes the third item in the list
# print(my_list) # prints the new list.
"""
List Functions and Methods
"""
my_list.append("c") # appends a new item to the end of the list.
# print(my_list) # prints the new list.
my_list.insert(3, "e") # inserts as 'e' to the fourth spot in the list.
my_list.insert(3, "d") # inserts a 'd' to the fourth spot on the list.
# print(my_list) # prints the new list.
# print(my_list.index("d")) # prints the index for the item 'd' in the list. 
# print("f" in my_list) # answers the question "is 'f' in my list?" with a boolean.
# print("f" not in my_list) # answers the question "is 'f' not in my list?" with a boolean.

my_list = [1, 4, 3, 2, 6, 5] # reassigned "my_list".
# print(sorted(my_list)) # prints a sorted "my_list" into a new list. 
# print(reversed(my_list)) # prints a list_reverseiterator object.
# print(list(reversed(my_list))) # prints the reversed version of "my_list".
# print(list(reversed(sorted(my_list)))) # prints the a reversed sorted version of "my_list". 
"""
Matrices
"""
my_matrix = [[1, 2, 3], [4, 5, 6]]  # creates a matrix "my_matrix".
# print(my_matrix) # prints "my_matrix".
row_count = len(my_matrix) # sets the variable "row_count" to how many rows are in "my_matrix".
column_count = len(my_matrix[0]) # sets the variable "column_count" to how many columns are in "my_matrix". 
# print(row_count) # prints the number of rows in "my_matrix".
# print(column_count) # prints the number of columns in "my_matrix".
# print(my_matrix[1][2]) # prints the item in row 2 column 3 in "my_matrix". 
"""
Tuples
"""
point = (2.0, 3.0) # creates a tuple defined as an (x and y) axis.
point_3d = point + (4.0,) # creates a 3-dimensional axis by adding to the original tuple.
# print(point_3d) # prints the tuple "point_3d".
x, y, z = point_3d # unpacks the tuple "point_3d" into three new items according to their place in the axis
# print(x) # prints item from "point_3d" x-axis point.
# print(y) # prints item from "point_3d" y-axis point.
# print(z) # prints item from "point_3d" z-axis point.
# print("My name is: %s %s" % ("Michael", "Cassidy")) # prints the statement and unpacked tuple using the substitution characters "%s".
person = ('Michael Cassidy', 33, '444-444-4444') # assigns items to "person".
person2 = ('Mr. Rogers', 76, '') # assigns items to "person2" while leaving the third item blank.
# print(person[0]) # prints the first item (name) in the tuple "person".
# print(person2[1]) # prints the second item (age) in the tuple "person2".
"""
Lists and Tuples
"""
my_list = [1, 2, 3] # creates a list.
my_tuple = (my_list, 4) # creates a tuple, with a list within the tuple.
# print(my_tuple) # prints "my_tuple".
another_list = [my_tuple, 5, 6] # creates another list with a tuple within.
# print(another_list)  # prints "another_list".
my_list.append(8) # appends an "8" to the end of "my_list".
# print(my_list) # prints "my_list".
# print(my_tuple) # prints "my_tuple" with the modified "my_list" within.
"""
Dictionarys
"""
ages = {"Mike": 33, "Mr. Rogers": 76, "Somebody": 99} # creates a dictionary using keys and values.
# print(ages) # prints the "ages" dictionary.
ages["Bob"] = 22 # adds a new key and value to the end of the "ages" dictionary.
# print(ages) # prints the new "ages" dictionary.
# print(ages["Mike"]) # prints the value for the key "Mike".
del ages["Somebody"] # deletes the dictionary entry for "Somebody".
# print(ages) # prints the revised "ages" dictionary.
ages["Mr. Rogers"] = 75 # changes the value of the key "Mr. Rogers".
# print(ages) # prints the revised "ages" dictionary.
# print("Somebody" in ages) # prints the boolean value for whether or not "Somebody" is a key in the dictionary.
# print(33 in ages) # prints the boolean value for whether or not "33" is a key in the dictionary.
colors = dict(Mike="blue", Somebody="green", Bob="black")  # creates a dictionary for "colors" in an alternate way.
# print(colors) # prints the "colors" disctionary. 
# print(ages.keys()) # prints the keys of the dictionary "ages".
# print(list(ages.keys())) # prints the keys of the dictionary "ages" in list format.
# print(ages.values()) # prints the values of the dictionary "ages".
# print(list(ages.values())) # prints the values of the dictionary "ages" in list format.
# print(ages.items()) # prints the items of the dictionary "ages".
# print(list(ages.items())) # prints the items of the dictionary "ages" in list format. 
"""
Sting Encodings and Functions
"""
# print(ord("a")) # prints the code point for "a".
# print(ord('\u2122')) # prints the the code point for the hexidecimal number "2122".
# print('\u2122') # prints the ™ string symbol, from the hexidecimal notation.
# print(chr(8482)) # prints the string from the code point.
"""
String Methods
"""
# print("This".lower()) # prints the string in lowercase letters.
my_str = "tEsTinG" # setting variable.
# print(my_str.lower()) # prints the string in lowercase letters.
# print(my_str.upper()) # prints the string in uppercase letters.
# print(my_str.capitalize()) # prints the string with the first character capitalized, and the rest lowercase.
# print("This is a multiword string".title()) # prints each work with the first letter capitalized. 
# print("Mike@example.com" == "mike@example.com") # prints boolean value for the statement.
# print("Mike@example.com".lower() == "mike@example.com") # prints boolean value for the statement.

# print(my_str.isascii()) # prints boolean for whether or not all characters in string are ASCII.
# print(my_str.islower()) # prints boolean for whether or not all characters in string are lowercase.
# print(my_str.isalpha()) # prints boolean for whether or not all characters in string are alphabetical characters.
# print(my_str.title().istitle()) # changes "my_str" to a title string and prints boolean for whether or not all characters in string are in title format.

url = "https://example.com/users/mike" # sets the variable.
user = url.split("/")[-1] # sets "user" variable to be the "url" variable, but splitting by the slash, and only selecting the last item in the list.
# print(user) # prints the variable "user".
# print(url.split("/")) # prints the "url" variable split up by slashes. 
lines = ["First Line", "Second Line", "Last Line"] # Setting the variable "lines" to the list.
output = "\n".join(lines) # sets the variable "output" to create a single string with a new line in between each item.
# print(output) # prints the variable "output". 
words = ["Hello", "My", "Name", "Is", "Mike"] # assigns a list to the variable "words".
output = " ".join(words) # reassigns the variable "output" to create a single string with a space in between each item.
# print(output) # prints the variable "output".
template = "Hello, my name is {}, and I enjoy {}. Have a nice time." # sets the variabel "template"
# print(template.format("Mike", "Python")) # prints the formatted version with the values described into "template".
template = "Hello, my name is {0}, and I enjoy {1}. Have a nice time. - {0}" # reassigns the variable "template" with item indices.
# print(template.format("Mike", "Python")) # prints the formatted version with the values described into "template".
"""
'If' and 'Else'
"""
# if "a" < "b": # makes a conditional statement with "if".
    # print("Condition was True") # prints the value if the above condition is true.
# if "a" > "b": # makes a conditional statement with "if".
    # print("Condition was True") # prints the value if the above condition is true.
# if False: # makes a conditional statement.
    # print("Was True") # prints "Was True" if the conditional statement is false, but since the statement is explicitly passing in "False", nothing will be printed.
# else:
    # print("Was False") # prints "Was False".
"""
elif
"""
# if "b" < "a": # makes a conditional statement
    # print("This is true") # prints the value if the above condition is true.
# elif "c" < "d": # makes a second conditional statement if no value is printed.
    # print("Second condition is true") # prints the value if the above condition is true.
# else: # if nothing has been printed yet, move to the next line.
    # print("no condition was true") # print the value.

# name = input("What is your name? ") # assigns the value of "name" to the input of the question.
# if len(name) >= 6: # makes a conditional statement
    # print("Your name is long") # prints the value if the above condition is true.
# elif len(name) >= 4: # makes a second conditional statement if no value is printed.
    # print("Your name is 4 or more letters long") # prints the value if the above condition is true.
# elif len(name) == 5: # makes a third conditional statement if no value is printed.
    # print("Your name is 5 letters long") # prints the value if the above condition is true.
# else: # if nothing has been printed yet, move to the next line.
    # print("Your name is short") # print the value.
"""
Pass
"""
# name = "Mike" # assigns variable "name".
# if name == "Bob": # makes a conditional statement
    # print("Hello Bob") # prints the value if the above condition is true.
# else: # if nothing has been printed yet, move to the next line.
    # pass # non operational statement.  Good for coming back to code later.
"""
While Loop
"""
# count = 1 # sets the variable "count".
# while count <= 4: # makes a while loop statement.
    # print("looping") # prints the value.
    # count += 1 # adds 1 to the count and repeat the loop
"""
For Loops
"""
# colors = ["blue", "green", "red", "purple"] # makes a list of colors.
# for color in colors: # makes a for loop statement with variables in a sequence.
    # print(color) # prints the values in sequential order.
# point = (1.2, 3.4, 5.6) # creates a tuple of values
# for value in point: # makes a for loop statement with variables in a sequence.
    # print(value) # prints the values in sequential order.
    
# ages = {"Mike": 33, "Mr. Rogers": 76, "Somebody": 99} # creates a dictionary using keys and values.
# for key in ages: # makes a for loop statement with variables in a sequence.
    # print(key) # prints the keys in sequential order.
# for key, value in ages.items(): # makes a for loop statement that is able to unpach to tuple.
    # print(key, value) # prints the key and value, in sequential order.

# for letter in "my_string": # makes a loop statement for a string.
    # print(letter) # prints the values in the string sequentially.
"""
Nesting Loops and Conditionals
"""
# counter = 1 # sets value for the variable.
# while counter <= 25: # makes a while loop statement.
    # if counter % 4 == 0: # makes a conditional statement.
        # print(counter) # prints the value.
    # counter += 1 # adds 1 to the counter and repeat the loop.
"""
Loop Execution
"""
# count = 0 # sets the variable
# while count < 10: # makes a while loop statement.
    # if count % 2 == 0: # makes a conditional statement.
        # count += 1 # adds 1 to the count.
        # continue # lines after this will not be executed for the current iteration.
    # print(f"We're counting odd numbers: {count}") # prints the format string with an expression.
    # count += 1 # adds 1 to the count and repeat the loop.
# count = 1 # sets the variable
# while count < 10: # makes a while loop statement.
    # if count % 2 == 0: # makes a conditional statement.
        # count += 1 # adds 1 to the count.
        # break # lines after this will not be executed after the above condition is false, and the execution stops entirely.
    # print(f"We're counting odd numbers: {count}") # prints the format string with an expression.
    # count += 1 # adds 1 to the count and repeat the loop.
"""
'else' with Loops
"""
# count = 1 # sets the variable
# while count <= 4:  # makes a while loop statement.
    # print(count) # prints the value.
    # count += 1 # adds 1 to the count and repeat the loop.
# else: # else clause
    # print("While loop completed") # prints the statement.
    
# for i in [1, 2, 3, 4, 5]: # makes a for loop staetment with variables in a sequence.
    # print(i) # prints the values in sequential order.
# else:  # else clause
    # print("For loop completed") # prints the statement.

# colors = ['red', 'yellow', 'green', 'blue', 'purple'] # # makes a list of colors.
# for color in colors: # makes a for loop statement with variables in a sequence.
    # if color == 'purple': # makes a conditional statement.
        # print("Purple is in the list") # prints the statement
        # break # lines after this will not be executed after the above condition is false, and the execution stops entirely.
# else: # else clause
    # print("Purple is not in the list") # prints the statement.
"""
'range'
"""
# my_range = range(10) # assigns the variable to a range of numbers with the specified stop value.
# print(my_range) # prints the variable.
# print(list(my_range)) # prints a list of all values in the range.

# print(list(range(1, 14, 2))) # prints a list using a start value, stop value, and step value.

# for number in range(1, 5): # makes a for loop statement with variables in a range.
    # print("looping") # prints the item "looping".
"""
List Comprehensions
"""
# colors = ["blue", "green", "orange", "red", "purple"] # makes a list of colors.
# uppercase_colors = [] # creates empty list.
# for color in colors: # makes a for loop statement with variables in a sequence.
    # uppercase_colors.append(color.upper()) # appends uppercase colors to the "uppercase_colors" list.
# print(uppercase_colors) # prints the list.

# uppercase_colors = [color.upper() for color in colors] # creates a list that contains an uppercase color for each iteration of the value in the list of colors.
# print(uppercase_colors) # prints the list.

# warm_colors = [] # creates empty list.
# for color in colors: # makes a for loop statement with variables in a sequence.
    # if color in ["red", "orange"]: # filters the colors "red" and "orange".
        # warm_colors.append(color.upper()) # appends uppercase colors to the "warm_colors" list.
# print(warm_colors) # prints the list.

# warm_colors = [color.upper() for color in colors if color in ["red", "orange"]] # creates a list that contains an uppercase color for each iteration of the value...
# ...in the list of colors if the values are true in the condition.
# print(warm_colors) # prints the list.
"""
Functions
"""
# def print_name(name): # defines a parameter in a function.
    # print(f"Name is {name}") # calls print to the function.
# print_name("Mike") # calls "print_name" and adds "Mike" to the print_name value.

# def add_two(num): # defines a parameter in a function.
    # return num + 2 # creates a return statement that adds 2 to "num".
# result = add_two(2) # adds an argument to the "result".
# print(result) # prints the result.

# def add(num1, num2): # defines parameters in a function.
    # return num1 + num2 # creates a return statement that adds both parameters together.
# result = add(1, 5) # adds arguments to passed into the parameters of the function.
# print(result) # prints the result.
"""
Parameters Vs Arguments
"""
# def contact_card(name, age, car_model): # defines parameters in a function.
    # return f"{name} is {age} and drives a {car_model}" # creates a return statement.
# print(contact_card("Mike", 33, "Ford F150")) # prints the function using positional arguments.

# print(contact_card(age=33, car_model="Ford F150", name="Mike")) # prints the function using keyword arguments.

# print(contact_card("Mike", car_model="Ford F150", age="33")) # prints the function using mixed arguments. Positional arguments cannot follow keyword arguments.

# def can_drive(age, driving_age=16): # defines parameters in a function.
    # return age >= driving_age # creates a return statement.
# print(can_drive(16)) # prints the function.
# print(can_drive(16, driving_age=18)) # prints the function with a change in the default argument.
"""
Recursion
"""
# def fib(n): # defines parameters in a function.
    # if n == 0: # makes a conditional statement.
        # return 0 # creates a return statement.
    # elif n == 1: # makes a second conditional statement if no value is printed.
        # return 1 # creates a return statement.

    # return fib(n - 2) + fib(n - 1) # creates a return statement by calling the fib function.

# item_to_calculate = int(input("What Fibonnaci item would you like to calculate? ")) # creates a script.

# print(fib(item_to_calculate)) # prints the fib value using the script input.
# The number of recursive function calls that happen when we try to calculate an excessively high number may cause no return (i.e. 50).
"""
Generators
"""
# def gen_range(stop, start=1, step=1): # defines parameters in a function.
    # num = start # sets the variable "num".
    # while num <= stop: # makes a while loop statement.
        # yield num # makes a yield statement that returns a generator object.
        # num += step # sets the variable to add a step.
# print(gen_range(10)) # prints the generator function.
# generator = gen_range(10) # assigns the varible "generator" 
# print(next(generator)) # prints the generator function until it hits the next yield.
# print(next(generator)) # prints the next generator function until it hits the next yield.
# once you print the generator function 10 times, the 11th time will return an error, because the range is 10.
"""
Generators to Lists
"""
# def gen_fib(): # defines parameters in a function.
    # a, b = 0, 1 # makes "a" = 0, and "b" = 1.
    # while True: # makes a infinite while loop statement.
        # a, b = b, a + b # reassigns the variables to create the next step in the Fibonnaci sequence.
        # yield a # makes a yield statement.
# fib = gen_fib() # assigns the varible "fib".
# print(next(fib)) # prints the generator function until it hits the next yield.
"""
Python Scopes
"""
# if 1 < 2:# makes a conditional statement.
    # x = 5 # assigns a value to the variable "x".

# while x < 6: # makes a while loop statement.
    # print(x) # print the variable "x".
    # x += 1 # add 1 to the variable.
# print(x) # print the new value of "x".
"""
Name Hiding
"""
# y = 5 # assigns the variable "y".

# def set_x(y): # defines parameters in a function to set "x", to take a "y".
    # print("Inner y:", y) # prints the quoted value, then the variable "y".
    # x = y # sets "x" equal to "y".
    # y = x # sets "y" equal to "x".

# set_x(10) # calls set "x" with 10.
# print("Outer y:", y) # prints the quoted value, then the variable "y".
# parameters are of higher priority than variables of the same name that are at a higher context.
"""
'global' keyword
"""
# y = 5 # assigns the variable "y".

# def set_x(z): # defines parameters in a function to set "x", to take a "z".
    # x = z # sets "x" equal to "z".
    # global y # sets the variable "y" outside the current scope.
    # global a # sets the variable "a" outside the current scope.
    # y = x # sets "y" equal to "x".
    # a = 7 # sets "a" equal to "7".

# print("y Before set_x:", y)  # prints the quoted value, then the variable "y".
# set_x(10) # calls set "x" with 10.
# print("y After set_x:", y)  # prints the quoted value, then the variable "y".
# print("a After set_x:", a)  # prints the quoted value, then the variable "a".

