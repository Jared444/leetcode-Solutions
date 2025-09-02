import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    Cdf = pd.DataFrame(customers)
    Odf = pd.DataFrame(orders)
    
    result = Cdf.merge(Odf, left_on="id",how='left', right_on="customerId", suffixes=("_C,", "_O"))
    result = result[result["customerId"].isna()]
    result = result[["name"]].rename(columns={"name" : "Customers"})
    return result