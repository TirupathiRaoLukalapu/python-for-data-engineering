
# Two sources of data
source1 = {
    "emp_id": 101,
    "name": "John",
    "age": 30,
    "ssn": "123-45-6789",
    "department": {
        "name": "IT",
        "manager": "Alice"
    }
}

source2 = {
    "emp_id": 101,
    "city": "New York",
    "salary": 80000,
    "skills": ["Python", "SQL", "Spark"]
}

# 1. Merge source1 and source2
# 2. Add a new field "manager" (from department info)
# 3. Remove ssn and salary fields
# 4. Print final dictionary
""""
source1.update(source2)

source1["manager"]=source1["department"]["manager"]

source1={k:v for k,v in source1.items() if k not in ["ssn", "salary"]}

print(source1)
"""

source1.update(source2)

# Add a new key for manager
source1["manager"] = source1["department"]["manager"]

# Remove sensitive info
source1 = {k: v for k, v in source1.items() if k not in ["ssn", "salary"]}

print(source1)
