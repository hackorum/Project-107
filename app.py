import pandas as pd
import plotly_express as px

student_ids = [
    "TRL_987",
    "TRL_abc",
    "TRL_imb",
    "TRL_mda",
    "TRL_mno",
    "TRL_rst",
    "TRL_xsl",
    "TRL_xyz",
    "TRL_zet",
    "TRL_zny",
]


df = pd.read_csv("csv/data.csv")

student_dfs = []
for i in range(len(student_ids)):
    student_dfs.append(df.loc[df["student_id"] == student_ids[i]])

answers = []
for student_df in student_dfs:
    answers.append(student_df.groupby("level")["attempt"].mean())

for j in range(len(student_dfs)):
    fig = px.scatter(
        student_dfs[j], x=["Level 1", "Level 2", "Level 3", "Level 4"], y=answers[j]
    )
    fig.show()
