def employee_details(name, empid, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {empid}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return result

if __name__ == "__main__":
    name = "Alice"
    empid = "E1001"
    department = "IT"
    salary = 55000
    print(employee_details(name, empid, department, salary))