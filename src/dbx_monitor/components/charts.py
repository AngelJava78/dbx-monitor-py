import pandas as pd
import plotly.express as px


def create_empty_chart():
    fig = px.line(title="Sin datos")
    fig.update_layout(template="plotly_white", height=500, title_x=0.5)
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

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        hovermode="x unified",
        title_x=0.5,
        legend_title_text="",
        xaxis_title="Date",
        yaxis_title="Instances",
    )

    fig.update_yaxes(dtick=1)

    return fig
