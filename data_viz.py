import pandas as pd
import plotly.express as px


def freq_bar_plot(df: pd.DataFrame, col: str, freq: str):
    """
    Create a frequency bar chart based on the provided DataFrame.
    :param df: the DataFrame containing the data
    :param col: the column in the DataFrame to be used for plotting
    :param freq: the frequency/count column associated with the `col` parameter.
    :return: None
    """
    title_text = " ".join(col.split("_")).title()
    fig = px.bar(df,
                 x=col,
                 y=freq,
                 labels={col: f"{title_text}",
                         freq: "Counts"},
                 title=f"Frequency of {title_text}")
    fig.update_traces(text=df[freq],
                      textposition="outside",
                      marker_color="#13294B",
                      hovertemplate=f"{title_text}: %{{x}}<br>Counts: %{{y}}")
    fig.update_layout(title_x=0.5,
                      height=600,
                      width=1000)
    fig.show()


def save_rate_line_plot(df: pd.DataFrame, title_text: str):
    """
    Create a save rate line plot based on the dataframe(overtime, by year, by month)
    :param df: the DataFrame containing the data
    :param title_text: the text to appear on the plot title
    :return: None
    """

    # create line plot
    fig = px.line(df,
                  x="time",
                  y=["save_rate(total death)", "save_rate(euthanasia)"],
                  title=f"Save Rate {title_text}")

    # update overall layout
    fig.update_layout(title_x=0.5,
                      legend=dict(title=""),
                      height=600,
                      width=1000)

    # update legend position
    fig.update_layout(legend=dict(orientation="v",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1))

    # update hover template
    fig.update_traces(mode="markers+lines",
                      hovertemplate=None)

    fig.update_layout(hovermode="x unified")

    # update x, y, title
    fig.update_xaxes(title_text="Time")
    fig.update_yaxes(title_text="Save Rate(%)")

    # add y=90 line as threshold
    fig.add_hline(y=90,
                  line_dash="dot",
                  line_color="black")
    fig.show()
