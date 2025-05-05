#generate unique name for ec2 instances

# import random
# import string

# ec2_num = int(input("How many EC2 instances do you want to create?: "))
# department_name = input("What is the name of your department?: ").strip().lower()

# for _ in range(ec2_num):
#     random_number = random.randint(0, 100000)
#     special_character = random.choice(string.punctuation)
#     ec2_unique_name = department_name + special_character + str(random_number)
#     print(ec2_unique_name)


#this code can be developed further to ensure that only members of specific 
# departments are allowed to create ec2 instances. 
#To do this, we can create a list of departments and check if the input department
# name is in the list.


import random
import string

allowed_departments = ["hr", "finance", "IT", "marketing", "finops"] #this code defines the list of allowed departments
ec2_num = int(input("How many EC2 instances do you want to create?: "))
department_name = input("What is the name of your department?: ").strip().lower() #.strip() and .lower() ensures that the input is in lowercase and has no spaces

if department_name in allowed_departments: #this checks if department is allowed   
    print("You are allowed to create EC2 instances")
    
    for _ in range(ec2_num):
        random_number = random.randint(0, 100000)
        special_character = random.choice(string.punctuation)
        ec2_unique_name = department_name + special_character + str(random_number)
        print(ec2_unique_name) 
else:
    print("You are not allowed to create EC2 instances")
    exit()



