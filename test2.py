employees = {}

for i in range(1, 4):
    emp_no = input(f"Enter employee {i} number: ")
    emp_name = input(f"Enter employee {i} name: ")
    employees[emp_no] = emp_name

print("\nAll Employee Numbers:")
for emp_no in employees.keys():
    print(emp_no)


second_emp_no = list(employees.keys())[1]
new_name = input("\nEnter new name for 2nd employee: ")
employees[second_emp_no] = new_name


print("\nEmployee Numbers with Names:")
for emp_no, emp_name in employees.items():
    print(emp_no, ":", emp_name)

