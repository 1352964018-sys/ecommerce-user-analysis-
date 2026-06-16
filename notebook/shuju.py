import pandas as pd

df = pd.read_csv(
    "../dwd/dwd_user_behavior.csv",
    nrows=5
)

print(df)