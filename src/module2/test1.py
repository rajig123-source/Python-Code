from dataclasses import dataclass

@dataclass
class Employee:

    employee_id: int
    employee_name: str
    department: str

employee=Employee(101, "Raji", "Dev")  

print(employee)
print(employee.employee_name)