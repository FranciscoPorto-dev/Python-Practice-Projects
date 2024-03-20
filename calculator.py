def display_menu ():
    print("What operation would you like to procced with(Ex: 1)?")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Multiple Operation (Own Formula or divison of more than two numbers)")

def addition ():
    li_num = input("Write all of the numbers you want to add(Ex:3,4,5,6):")
    split_li = li_num.split(',')
    sum = 0
    for nums in split_li:
        try:
            sum += int(nums)
        except:
            print(f"Unable to convert '{nums}' to an integer")
    print(sum)

def subtraction ():
    li_num = input("Write all of the numbers you want to subtract(Ex:3,4,5,6):")
    split_li = li_num.split(',')
    subtraction = int(split_li[0])
    for nums in split_li[1:]:
        try:
            subtraction -= int(nums)
        except:
            print(f"Unable to convert '{nums}' to an integer")
    print(subtraction)

def multiplication ():
    li_num = input("Write all of the numbers you want to multiply(Ex:3,4,5,6):")
    split_li = li_num.split(',')
    multiplication = 1
    for nums in split_li:
        try:
            multiplication *= int(nums)
        except:
            print(f"Unable to convert '{nums}' to an integer")
    print(multiplication)

def division ():
    li_num = input("Write two numbers you want to have divide(Ex: 5,6):")
    split_li = li_num.split(',')
    full_division = 0
    for nums in split_li:
        try:
            num_1 = int(split_li[0])
            num_2 = int(split_li[1])
            full_division = num_1/num_2
        except:
            print(f"Unable to convert '{nums}' to an integer")
    print(full_division)

def multi_op ():
    li_num = input("Write the full formula that you want to solve(Ex: ((8*9)+(9*8):")
    converted_form = eval(li_num)
    print(converted_form)

def main ():
    while True:
        display_menu()
        operation = input()
        if operation == '1':
            addition()
        elif operation == '2':
            subtraction()
        elif operation == '3':
            multiplication()
        elif operation == '4':
            division()
        elif operation == '5':
            multi_op()
        else:
            print("The number is invalid (make sure its written correctly as stated by the example)")
            break

if __name__ == "__main__":
    main()


