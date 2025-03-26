import pandas as pd
import plotly.express as px
from bokeh.plotting import figure
from bokeh.models import HoverTool, Legend, ColumnDataSource
from bokeh.palettes import Category10
from bokeh.resources import CDN
from bokeh.embed import file_html
import json

df = pd.read_csv("SF_crimeDF_cleaned.csv", index_col=0)
df["DateTime"] = pd.to_datetime(df["DateTime"])
drug_offenses = df[
    df["Crime_Category"].str.lower().str.contains("drug|narcotic", regex=True)
]


########################
#  Plot 1
def generate_yearly_bar():
    drug_counts_yearly = drug_offenses.groupby("Year").size().reset_index(name="Count")

    fig = px.bar(
        drug_counts_yearly,
        x="Year",
        y="Count",
        title="Annual Drug Offenses in San Francisco",
        labels={"Count": "Number of Drug Offenses", "Year": "Year"},
        color="Count",
        color_continuous_scale="YlOrRd",
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40),
        height=500,
        autosize=True,
    )

    fig.write_html(
        "assets/plotly/yearly_drug_offenses.html",
        config={
            "responsive": True,
            "displayModeBar": True,
            "scrollZoom": True,
            "displaylogo": False,
        },
        full_html=True,
        include_plotlyjs=True,
    )
    print("Generated yearly drug offenses bar chart")


########################
#  Plot 2
def generate_district_lines():
    drug_district_yearly = (
        drug_offenses.groupby(["Year", "District"]).size().reset_index(name="Count")
    )
    drug_pivot = drug_district_yearly.pivot(
        index="Year", columns="District", values="Count"
    ).fillna(0)

    p = figure(
        title="Drug Offenses by District (2003–2024)",
        x_axis_label="Year",
        y_axis_label="Number of Offenses",
        sizing_mode="stretch_width",
        height=500,
        tools="pan,box_zoom,reset,save",
    )

    colors = Category10[10]
    legend_items = []

    for i, district in enumerate(drug_pivot.columns):
        source = ColumnDataSource(
            data={
                "x": drug_pivot.index,
                "y": drug_pivot[district],
                "district": [district] * len(drug_pivot),
            }
        )
        line = p.line(
            "x",
            "y",
            source=source,
            line_width=2,
            color=colors[i % len(colors)],
            alpha=0.8,
        )
        legend_items.append((district, [line]))

    hover = HoverTool(
        tooltips=[("Year", "@x"), ("District", "@district"), ("Count", "@y")]
    )
    p.add_tools(hover)

    legend = Legend(items=legend_items, location="top_right", click_policy="hide")
    p.add_layout(legend)

    html = file_html(p, CDN, "Drug Offenses by District")
    with open("assets/bokeh/district_trends.html", "w") as f:
        f.write(html)
    print("Generated district trends line chart")


########################
#  Plot 3
def generate_choropleth():
    df_agg = (
        drug_offenses.groupby(["Year", "District"]).size().reset_index(name="count")
    )
    df_agg["District"] = df_agg["District"].str.upper()

    with open("sfpd.geojson", "r") as f:
        geo_data = json.load(f)

    fig = px.choropleth_mapbox(
        df_agg,
        geojson=geo_data,
        locations="District",
        color="count",
        featureidkey="properties.DISTRICT",
        color_continuous_scale="YlOrRd",
        range_color=(0, df_agg["count"].max()),
        center={"lat": 37.76, "lon": -122.45},
        animation_frame="Year",
        hover_name="District",
        hover_data=["count"],
        opacity=0.8,
        zoom=10,
        mapbox_style="carto-positron",
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        height=600,
        autosize=True,
    )

    # Configure animation settings to disable autoplay
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 500
    fig.layout.sliders[0].active = 0

    # Add a play button but start paused
    fig.layout.updatemenus[0].buttons[0].args[1]["mode"] = "immediate"
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["redraw"] = True
    fig.layout.updatemenus[0].showactive = True

    fig.write_html(
        "assets/plotly/district_map.html",
        config={
            "responsive": True,
            "displayModeBar": True,
            "scrollZoom": True,
            "displaylogo": False,
        },
        full_html=True,
        include_plotlyjs=True,
        auto_play=False,  # Disable auto play
    )
    print("Generated district choropleth map")


if __name__ == "__main__":
    generate_yearly_bar()
    generate_district_lines()
    generate_choropleth()
    print("All visualizations have been generated successfully")
