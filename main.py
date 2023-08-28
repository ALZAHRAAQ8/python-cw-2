my_name = input("enter your name")
my_age = input("enter your age")

print(f"my_name is {my_name} and I am {my_age} years old")

first_number=int(input("enter first number"))
second_number=int(input("enyer second number"))
operation=input("what is the operation (+-*/)")

if operation == '+' :
    print(first_number + second_number)

elif operation == "-" :
    print(first_number - second_number)
elif operation == "*" :
    print(first_number * second_number)
elif operation == "/" :
    print(first_number / second_number)
else :
    print("the operation is not avalid")


bus_capacity=25
people_inbus = int(input("the people in the bus"))
people_outbus = int(input("the people want to enter the bus"))

empty_seats = bus_capacity - people_inbus

if empty_seats > people_outbus :        
   print("the empty seats is"+ empty_seats)
elif empty_seats <= people_outbus:
    print("there is no empty seats")
    