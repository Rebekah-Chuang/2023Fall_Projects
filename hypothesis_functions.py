import pandas as pd


def no_kill_rate(df, intake_col, outcome_col):
    died_list = ["Euthanasia", "Died", "Disposal", "Missing", "Stolen"]

    total_intake = df.groupby(intake_col).size().rename("total_intake")
    total_outcome = df.groupby(outcome_col).size().rename("total_outcome")
    total_died_cases = df.groupby(outcome_col)["outcome_type"].apply(lambda x: (x.isin(died_list)).sum()).rename("total_died_cases")
    euthanasia_cases = df.groupby(outcome_col)["outcome_type"].apply(lambda x: (x == "Euthanasia").sum()).rename("euthanasia_cases")

    cases = pd.concat([total_intake, total_outcome, euthanasia_cases, total_died_cases], axis=1).reset_index()
    cases = cases.rename(columns={"index":"time"})
    cases = cases.dropna(subset=["total_intake"])
    cases["save_rate(total died)"] = (1 - (cases["total_died_cases"]/cases["total_intake"]))*100.0
    cases["save_rate(euthanasia)"] = (1 - (cases["euthanasia_cases"]/cases["total_intake"]))*100.0

    return cases