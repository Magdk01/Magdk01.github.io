import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

# Create sample data
np.random.seed(42)
n_points = 100
df = pd.DataFrame(
    {
        "x": np.random.normal(0, 1, n_points),
        "y": np.random.normal(0, 1, n_points),
        "category": np.random.choice(["A", "B", "C"], n_points),
    }
)

# Create Bokeh visualization
p = figure(
    title="Interactive Scatter Plot (Bokeh)",
    sizing_mode="stretch_width",
    height=500,
    tools="pan,box_zoom,reset,save",
)

# Add scatter points with different colors for each category
colors = {"A": "red", "B": "blue", "C": "green"}
for category in df["category"].unique():
    category_data = df[df["category"] == category]
    p.scatter(
        category_data["x"],
        category_data["y"],
        color=colors[category],
        legend_label=category,
        size=8,
        alpha=0.6,
    )

# Customize the plot
p.title.align = "center"
p.grid.grid_line_color = "white"
p.background_fill_color = "#f8f9fa"
p.border_fill_color = "white"
p.legend.click_policy = "hide"

# Save the plot
html = file_html(p, CDN, "Bokeh Plot")
with open("assets/bokeh/example.html", "w") as f:
    f.write(html)

print("Bokeh visualization has been generated and saved to assets/bokeh/example.html")
