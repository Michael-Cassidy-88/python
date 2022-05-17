import random

def ec2_id(id_size = 4):
    letters = [chr(i) for i in (range(ord("a"),ord("z")+1))]
    numbers = [str(i) for i in range(0,10)]
    characters = letters + numbers
    return ''.join(random.choice(characters) for i in range(id_size))
    
while True:
    try:
        dept_name = input("For which department are you creating an instance name?: ")
        list = ["Accounting", "Marketing", "FinOps"]
        if dept_name not in list:
            raise ValueError
        break
    except ValueError:
            print("This department does not have access to the ID generator")
            exit ()
    else:
        break

id_name = input("What is your name:? ")

num = input("How many EC2 Instance names would you like?: ")
x = num
x = int(x)
for _ in range(x):
    print('\n')
    print("Unique EC2 Name:")
    print('{}-{}-{}'.format(dept_name, id_name, ec2_id(id_size = 4)))  