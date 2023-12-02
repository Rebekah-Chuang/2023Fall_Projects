import plotly.express as px


def freq_bar_plot(df, col, freq):
    """
    create frequency bar chart
    :param df:
    :param col:
    :param freq:
    :return:
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
                      marker_color="#13294B")
    fig.update_layout(title_x=0.5,
                      height=600,
                      width=1000)
    fig.show()