# try:
#     a = int(input("Enter a number:"))
#     b = int(input("Enter a number:"))
#     c = a/b
# except ZeroDivisionError:
#     print("cannot divide by zero")
# else:
#     print("division succesfull")
# finally:
#     print("Program succesfull")




# user_input = int(input("enter a number:"))
# try:
#     number = int("enter a number: ")



# a = input("enter a value: ")
# b = 7
# try:
#     result = a+b
#     print(result)
# except TypeError:
#     print("please enter a valid value")
# finally:
#     print("program execution successfull")


# my_dict = {"name": "aryan","age":20}
# key = input("Enter a key")
# try:
#     print(my_dict[key])
# except KeyError:
#     print("Key not found enter another key!")
# finally:
#     print("Program exceuted succesfully")


# a = 1
# b = 0
# try:
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("Can not devide by zero!")
# finally:
#     print("Program executed")


# a = int(input("Enter a number:"))
# b = int(input("enter a number"))

# try:
#     result = a / b
#     print(result)
# except ArithmeticError:
#     print("Cannot divide by zero! please enter a valid number")
# except ValueError as e:
#     print(f"Please enter a valid value. (Error {e})")
# except Exception as e:
#     print(f"( Error: {e})")
# else:
#     print("Program Exceuted Succesfully")



# def celsius_to_fahrenheit(celsius):

#     if celsius < -271.15:
#         raise ValueError("Temperature can not be below absolute temperature")
#     fahrenheit = (celsius *(9/5)) + 32
#     return fahrenheit
# try:
#     celsius = float(input("Please enter the value"))
#     celsius_to_fahrenheit(celsius)
#     fahrenheit = (celsius *(9/5)) + 32
#     print(celsius)
#     print(fahrenheit)
# except ValueError:
#     print("Please enter the correct value")
# except Exception as e:
#     print(e)
# finally:
    # print("Program excecuted successful")


# def celsius_to_fahrenheit(celsius):
#     if celsius < -271.15:
#         raise ValueError("Temperature can not be below absolute temperature")
#     fahrenheit = (celsius *(9/5)) + 32
#     print(fahrenheit)
# try:
#     celsius = float(input("Please enter the value"))
#     celsius_to_fahrenheit(celsius)
#     print(celsius)
    
# except ValueError as e:
#     print("Please enter the correct value",e)
# except Exception as e:
#     print(e)
# finally:
#     print("Program excecuted successful")    


# def celsius_to_fahrenheit(celsius):
#     if celsius < -271.15:
#         raise ValueError("Temperature can not be below absolute temperature")

# try:
#     celsius = float(input("Please enter the value"))
#     celsius_to_fahrenheit(celsius)
#     fahrenheit = (celsius *(9/5)) + 32
#     print("Celsius: ",celsius)
#     print("fahrenheit: ",fahrenheit)
    
# except ValueError as e:
#     print("Please enter the correct value",e)
# except Exception as e:
#     print(e)
# finally:
#     print("Program excecuted successful")  