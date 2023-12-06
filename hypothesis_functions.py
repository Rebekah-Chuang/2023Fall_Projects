"""
This hypothesis_functions.py file includes all functions I used for hypothesis or research questions
"""
import pandas as pd


def create_time_column(df: pd.DataFrame, intake_date: str, outcome_date: str) -> pd.DataFrame:
    """
    Create new columns to specify a row's year-month, year, month for further analysis
    :param df: the DataFrame containing intake and outcome data
    :param intake_date: the column include intake datetime
    :param outcome_date: the column include outcome datetime
    :return: the updated DataFrame including new columns for year-month, year, and month for each row

    This function converts intake and outcome date columns into datetime format. It then creates several new columns:
    - `intake_y_m`: Year-month of intake in string format (YYYY-MM).
    - `outcome_y_m`: Year-month of outcome in string format (YYYY-MM).
    - `intake_yr`: Year of intake in string format (YYYY).
    - `outcome_yr`: Year of outcome in string format (YYYY).
    - `intake_m`: Month name of intake (e.g., January, February) based on the intake date.
    - `outcome_m`: Month name of outcome (e.g., January, February) based on the outcome date.

    Examples:
    >>> test_data = pd.read_csv("test_data/no_kill_test_data.csv")
    >>> result = create_time_column(test_data, "intake_datetime", "outcome_datetime")
    >>> print(result.loc[0, "intake_y_m"])
    2013-11
    >>> print(result.loc[1, "outcome_m"])
    March
    >>> print(result.loc[4, "intake_yr"])
    2023
    """
    df["intake_datetime"] = pd.to_datetime(df[intake_date])
    df["outcome_datetime"] = pd.to_datetime(df[outcome_date])

    df["intake_y_m"] = df[intake_date].dt.to_period("M").astype(str)
    df["outcome_y_m"] = df[outcome_date].dt.to_period("M").astype(str)

    df["intake_yr"] = df[intake_date].dt.to_period("Y").astype(str)
    df["outcome_yr"] = df[outcome_date].dt.to_period("Y").astype(str)

    df["intake_m"] = pd.to_datetime(df[intake_date], format='%m').dt.month_name()
    df["outcome_m"] = pd.to_datetime(df[outcome_date], format='%m').dt.month_name()

    return df


def no_kill_rate(df: pd.DataFrame, intake_col: str, outcome_col: str) -> pd.DataFrame:
    """
    Calculate the no-kill(save) rates based on intake and outcome data
    :param df: the DataFrame containing intake and outcome data
    :param intake_col: the column include intake datetime
    :param outcome_col: the column include outcome datetime
    :return: the updated DataFrame including new columns for save_rate(total death) and save_rate(euthanasia)

    Examples:
    >>> test_data = pd.read_csv("test_data/no_kill_test_data.csv")
    >>> result = create_time_column(test_data, "intake_datetime", "outcome_datetime")
    >>> save_rate_df = no_kill_rate(result, "intake_yr", "outcome_yr").set_index("time")
    >>> save_rate_df.loc["2015", "euthanasia_cases"]
    2
    >>> int(save_rate_df.loc["2014", "save_rate(euthanasia)"])
    75
    >>> save_rate_df2 = no_kill_rate(result, "intake_m", "outcome_m").set_index("time")
    >>> int(save_rate_df2.loc["March", "save_rate(total death)"])
    80
    """
    died_list = ["Euthanasia", "Died", "Disposal", "Missing", "Stolen"]

    total_intake = df.groupby(intake_col).size().rename("total_intake")
    total_outcome = df.groupby(outcome_col).size().rename("total_outcome")
    total_death_cases = df.groupby(outcome_col)["outcome_type"].apply(lambda x: (x.isin(died_list)).sum()).rename("total_death_cases")
    euthanasia_cases = df.groupby(outcome_col)["outcome_type"].apply(lambda x: (x == "Euthanasia").sum()).rename("euthanasia_cases")

    cases = pd.concat([total_intake, total_outcome, euthanasia_cases, total_death_cases], axis=1).reset_index()
    cases = cases.rename(columns={"index": "time"})
    cases = cases.dropna(subset=["total_intake"])
    cases["save_rate(total death)"] = (1 - (cases["total_death_cases"]/cases["total_intake"]))*100.0
    cases["save_rate(euthanasia)"] = (1 - (cases["euthanasia_cases"]/cases["total_intake"]))*100.0

    return cases

