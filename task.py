def task_1():
    password = "Password123"

    # Enter your code here
    guess = ""

    while guess 1= password:
        print("Enter password: ")
        guess=input()
    else:
        print("password granted!")


def task_2(): # Times tables
    # Enter your code here
counter = 1
timestables_1 = int(input("Enter a number: "))
timestables_2 = int(input("Enter another number: "))

while counter <= timestables_1:
    print(f"{timestables_1} * {counter} = {timestables_1 * counter}")
    counter += 1



def task_3(): # Count mississippis
import time

counter = 1

while counter <= 5:
    print(f"{counter} Mississippi")
    time.sleep(1)
    counter += 1
   
    
    