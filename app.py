import pandas as pd
import plotly_express as px

df = pd.read_csv("csv/data.csv")

mean = df.groupby("level", as_index=False)["attempt"].mean()
print(mean)

fig = px.scatter(
    df,
    x="student_id",
    y="level",
    size="attempt",
    color="attempt",
)
fig.show()
