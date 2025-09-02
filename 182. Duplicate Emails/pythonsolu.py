import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(person)
    result = df.groupby("email")["email"].count().reset_index(name="count")
    result = result.rename(columns={"email":"Email"})
    result = result.query("count > 1")
    result = result.drop(columns=["count"])
    return result