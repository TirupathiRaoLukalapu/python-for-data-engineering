"""
Remove sensitive data (ssn, salary).

Add a field department_manager from the nested dictionary.

Keep only employees who have "Python" in their skill set.

"""

employees = [
    {
        "emp_id": 101,
        "name": "John",
        "age": 30,
        "ssn": "123-45-6789",
        "salary": 80000,
        "department": {"name": "IT", "manager": "Alice"},
        "skills": ["Python", "SQL", "Spark"]
    },
    {
        "emp_id": 102,
        "name": "Emma",
        "age": 28,
        "ssn": "987-65-4321",
        "salary": 75000,
        "department": {"name": "HR", "manager": "Robert"},
        "skills": ["Excel", "Communication"]
    },
    {
        "emp_id": 103,
        "name": "Mike",
        "age": 35,
        "ssn": "555-11-2222",
        "salary": 95000,
        "department": {"name": "Finance", "manager": "Sara"},
        "skills": ["Python", "SQL"]
    }
]

cleaned_employees=[]

for emp in employees:
    cleaned_emp= {k: v for k,v in emp.items() if k not in ["ssn", "salary"] }
    #print("after removing ssn and salary\n",cleaned_emp)
    cleaned_emp["department_manager"]=emp["department"]["manager"]
   # print("after adding department manager \n", cleaned_emp)

    if "Python" in emp["skills"]:
        cleaned_employees.append(cleaned_emp)
       # print("printing if python in skills\m",cleaned_emp)

print(cleaned_employees)        
         