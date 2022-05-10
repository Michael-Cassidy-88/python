# This project will create a small list of services available on AWS.
# We will add items, take measurements of the list, and delete items using python language. 

aws_list = []  # assigning the variable "aws_list" to be an empty list
print(aws_list) # prints the empty "aws_list".

aws_list = ["Cloud9", "EC2", "VPC", "CloudWatch", "IAM", "S3"]  # Populating the list with a few aws services.
print(aws_list)  # prints "aws_list".

aws_list.append("Lambda")  # appends "Lambda" service to the end of the list.
print(aws_list)  #prints the appended list.

aws_list.insert(2, "ECS") # inserts "ECS" services into the third spot on the list.
print(aws_list)  #prints the new version of the list.

print(len(aws_list))  # prints the length, or number of items in the list.

row_count = len(aws_list) # assign the variable "row_count" to equal the length of the items on the list.
print(row_count) # prints the length of the number of items in the list.

del(aws_list[2]) # deletes the third item on the list.
print(aws_list) # prints the new list.

aws_list[1:3] = ["Kinesis", "CloudFormation"] # slices the second and third item on the list, and replaces them with "Kinesis" and "CloudFormation" services, respectively.
print(aws_list) # prints the new list
print(list(reversed(sorted(aws_list)))) # prints the a reversed sorted version of "my_list". 
