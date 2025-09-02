import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employee)
    
    result = df.merge(df, left_on="managerId", right_on="id", suffixes=("_emp","_mgr"))
    result = result.query("salary_emp > salary_mgr")
    result = result[["name_emp"]].rename(columns={"name_emp" : "Employee"})

    return result