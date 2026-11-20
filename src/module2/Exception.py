class InvalidSalaryError(Exception):
    pass

def calculate(salary):
    if salary<=0:
        raise InvalidSalaryError("salary nust be grater than zero")
    print("Employee Salary",salary)
try:
    calculate(-5000)

except InvalidSalaryError as error:
    print("Error",error)