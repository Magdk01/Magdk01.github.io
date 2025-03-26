import plotly.express as px
import pandas as pd
import numpy as np

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

# Create the visualization
fig = px.scatter(
    df,
    x="x",
    y="y",
    color="category",
    title="Interactive Scatter Plot",
    labels={"x": "X Axis", "y": "Y Axis", "category": "Category"},
)

# Customize the layout
fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    showlegend=True,
    margin=dict(l=40, r=40, t=40, b=40),
    height=500,  # Set a reasonable default height
    autosize=True,
)

# Save as HTML
fig.write_html(
    "assets/plotly/example.html",
    config={
        "responsive": True,
        "displayModeBar": True,
        "scrollZoom": True,
        "displaylogo": False,
    },
    full_html=True,
    include_plotlyjs=True,
)
print("Plotly visualization has been generated and saved to assets/plotly/example.html")
