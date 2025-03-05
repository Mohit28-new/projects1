def subtract(numbers):
    result = 0
    for num in numbers:
            result -= num
    return result

def multiply(numbers):
        result = 1
        for num in numbers:
                result *= num
        return int(result)
        
def divide(numbers):
        result = numbers[0]
        for num in numbers[1:]:
                result /= num
        return int(result)
        

print("-------------------Welcome to python calculator---------------------")

choice = (input("Enter choise\n 1-'+'\n 2- '-'\n 3- '*'\n 4-'/' \n"))
numbers = (input("Enter the values of the number given by the space: ")).split()

numbers = [int(num) for num in numbers]

       
if choice == '1' :
           result  = (sum(numbers))
           print(result)
elif choice == '2':
        result = (subtract(numbers))
        print(result)
elif choice == '3':
        result = (multiply(numbers))
        print(result)
elif choice == '4':
        result = round(divide(numbers),2)
        print(result)
else:
        print("You entered the wrong choice, GAME FINISH!!!")