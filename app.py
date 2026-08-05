"""
Healthcare Appointment Dashboard

Main entry point for the Dash application.
"""

import dash
import dash_bootstrap_components as dbc

from src.data_loader import load_data
from src.layout import create_layout
from src.callbacks import register_callbacks


# -----------------------------------------------------
# Load and prepare data
# -----------------------------------------------------
df = load_data()


# -----------------------------------------------------
# Initialize Dash app
# -----------------------------------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

app.title = "Healthcare Appointment Dashboard"


# -----------------------------------------------------
# Create dashboard layout
# -----------------------------------------------------
app.layout = create_layout(df)


# -----------------------------------------------------
# Register callbacks
# -----------------------------------------------------
register_callbacks(app, df)
#print(app.callback_map.keys())

# -----------------------------------------------------
# Run application
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)