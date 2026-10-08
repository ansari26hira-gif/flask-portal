import pandas as pd
import os
os.makedirs("uploads", exist_ok=True)

data = [
    ["NX-001","John Smith","Finance","CFO",95000],
    ["NX-002","Sophia Turner","Finance","CFO",92000],
    ["NX-003","Martha Hayes","Technology","CTO",105000],
    ["NX-004","Olivia Hughes","HR","HR Manager",68000],
    ["NX-005","Ethan Brooks","Sales","Sales Manager",72000],
]
df = pd.DataFrame(data, columns=["ID","Name","Dept","Post","Salary"])
df.to_excel("uploads/01_Employee_Database.xlsx", index=False)
print("CIT: 01_Employee_Database.xlsx ban gaya!")