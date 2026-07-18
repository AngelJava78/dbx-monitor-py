import pandas as pd
import plotly.express as px


def create_empty_chart():
    fig = px.line(title="Sin datos")
    fig.update_layout(template="plotly_white", height=400, title_x=0.5)
    return fig


def create_cluster_chart(cluster_stack: pd.DataFrame):
    if cluster_stack.empty:
        return create_empty_chart()

    fig = px.bar(
        cluster_stack,
        x="start_time_cdmx",
        y="cantidad",
        color="tipo",
        barmode="stack",
        title="Cluster metrics",
        color_discrete_map={
            "drivers": "#2563eb",
            "workers": "#22c55e",
        },
    )

    max_instances = (
        cluster_stack
        .groupby("start_time_cdmx")["cantidad"]
        .sum()
        .max()
    )

    fig.add_hline(
        y=max_instances,
        line_dash="dash",
        line_width=1,
        line_color="#f97316",
        annotation_text=f"Max: {max_instances}",
        annotation_position="top left",
    )

    start_time = pd.to_datetime(cluster_stack["start_time_cdmx"]).min().floor("2h")
    end_time = pd.to_datetime(cluster_stack["start_time_cdmx"]).max().ceil("2h")

    for dt in pd.date_range(start=start_time, end=end_time, freq="2h"):
        fig.add_vline(
            x=dt,
            line_width=1,
            line_dash="dot",
            opacity=0.5,
        )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_white",
        height=400,
        hovermode="x unified",
        title_x=0.5,
        legend_title_text="",
        xaxis_title="Date",
        yaxis_title="Instances",
    )

    fig.update_yaxes(dtick=1)

    return fig
