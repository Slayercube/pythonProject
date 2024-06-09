# exception = event that interrupts the normal flow of the program's execution
# exception handling = process of responding to exceptions

try:
    numberator = int(input("Enter a number: "))
    denominator = int(input("Enter a number: "))
    result = numberator / denominator

except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter a valid number")
except Exception:
    print("something went wrong")
else:
    print(result)
finally:
    print("this will always run")