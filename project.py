def check_age():
    try:
        age = input("Please enter your age: ")
        age = int(age)  
        if age < 0:
            print("The age cannot be negative number.")
        else:
            if age % 2 == 0:
                print("The age entered is even.")
            else:
                print("The age entered is odd.")
    except ValueError:
        print("Value error: Please check")

check_age()
