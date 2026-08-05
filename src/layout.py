"""
layout.py

Defines the Dash dashboard layout.
"""

from dash import html, dcc
import dash_bootstrap_components as dbc

from src.kpi import get_kpis



# ============================================================
# KPI CARD
# ============================================================

def create_kpi_card(title, value, component_id, icon):

    return dbc.Card(

        dbc.CardBody(

            [

                html.Div(

                    [

                        html.Div(

                            icon,

                            className="kpi-icon"

                        ),

                        html.Div(

                            [

                                html.Div(

                                    title,

                                    className="kpi-title"

                                ),

                                html.H2(

                                    value,

                                    id=component_id,

                                    className="kpi-value"

                                ),

                            ],

                            className="kpi-text"

                        ),

                    ],

                    className="kpi-content"

                )

            ]

        ),

        className="kpi-card"

    )



# ============================================================
# CHART CARD
# ============================================================

def create_chart_card(chart_id, title):

    return dbc.Card(

        dbc.CardBody(

            [

                html.H5(

                    title,

                    className="chart-title"

                ),

                dcc.Graph(

                    id=chart_id,

                    config={
                        "displayModeBar": False
                    }

                )

            ]

        ),

        className="chart-card"

    )



# ============================================================
# DASHBOARD LAYOUT
# ============================================================

def create_layout(df):

    """
    Create complete dashboard layout.
    """

    kpis = get_kpis(df)



    return dbc.Container(

        [

            # ==================================================
            # HEADER
            # ==================================================

            dbc.Card(

                dbc.CardBody(

                    [

                        html.Div(

                            [

                                html.H1(

                                    "🏥 Healthcare Appointment Dashboard",

                                    className="dashboard-title"

                                ),


                                html.P(

                                    "Interactive analytics for patient demographics, appointment trends, no-show behavior and healthcare performance.",

                                    className="dashboard-subtitle"

                                ),

                            ],

                            className="header-content"

                        )

                    ]

                ),

                className="header-card mb-4"

            ),



            # ==================================================
            # FILTER SECTION
            # ==================================================

            dbc.Card(

                dbc.CardBody(

                    [

                        html.Div(

                            [

                                html.Div(

                                    [

                                        html.H4(

                                            "🔍 Dashboard Filters",

                                            className="filter-title"

                                        ),

                                        html.P(

                                            "Filter the dashboard to analyze specific patient populations.",

                                            className="filter-subtitle"

                                        ),

                                    ]

                                ),


                                dbc.Button(

                                    "Reset Filters",

                                    id="reset-filters",

                                    color="success",

                                    className="reset-btn"

                                )

                            ],

                            className="filter-header"

                        ),


                        html.Hr(),



                        dbc.Row(

                            [

                                dbc.Col(

                                    [

                                        html.Label(

                                            "Gender",

                                            className="filter-label"

                                        ),

                                        dcc.Dropdown(

                                            id="gender-filter",

                                            options=[

                                                {
                                                    "label":x,
                                                    "value":x
                                                }

                                                for x in sorted(
                                                    df["gender"]
                                                    .dropna()
                                                    .unique()
                                                )

                                            ],

                                            placeholder="All Genders",

                                            clearable=True

                                        )

                                    ],

                                    xs=12,
                                    md=6,
                                    lg=3

                                ),



                                dbc.Col(

                                    [

                                        html.Label(

                                            "Age Group",

                                            className="filter-label"

                                        ),

                                        dcc.Dropdown(

                                            id="age-filter",

                                            options=[

                                                {
                                                    "label":str(x),
                                                    "value":x
                                                }

                                                for x in df["age_group"]
                                                .dropna()
                                                .unique()

                                            ],

                                            placeholder="All Ages",

                                            clearable=True

                                        )

                                    ],

                                    xs=12,
                                    md=6,
                                    lg=3

                                ),



                                dbc.Col(

                                    [

                                        html.Label(

                                            "Neighbourhood",

                                            className="filter-label"

                                        ),

                                        dcc.Dropdown(

                                            id="neighbourhood-filter",

                                            options=[

                                                {
                                                    "label":x,
                                                    "value":x
                                                }

                                                for x in sorted(
                                                    df["neighbourhood"]
                                                    .dropna()
                                                    .unique()
                                                )

                                            ],

                                            placeholder="All Areas",

                                            clearable=True

                                        )

                                    ],

                                    xs=12,
                                    md=6,
                                    lg=3

                                ),



                                dbc.Col(

                                    [

                                        html.Label(

                                            "Scholarship",

                                            className="filter-label"

                                        ),


                                        dcc.Dropdown(

                                            id="scholarship-filter",

                                            options=[

                                                {
                                                    "label":"No",
                                                    "value":0
                                                },

                                                {
                                                    "label":"Yes",
                                                    "value":1
                                                }

                                            ],

                                            placeholder="All Patients",

                                            clearable=True

                                        )

                                    ],

                                    xs=12,
                                    md=6,
                                    lg=3

                                )

                            ],

                            className="g-3"

                        )

                    ]

                ),

                className="filter-card mb-4"

            ),



            # ==================================================
            # KPI SECTION
            # ==================================================

            html.H2(

                "Key Performance Indicators",

                className="section-title"

            ),



            dbc.Row(

                [

                    dbc.Col(

                        create_kpi_card(

                            "Total Appointments",

                            f"{kpis['total_appointments']:,}",

                            "total-appointments",

                            "📅"

                        ),

                        xs=12,
                        sm=6,
                        md=4,
                        lg=2

                    ),


                    dbc.Col(

                        create_kpi_card(

                            "Completed Appointments",

                            f"{kpis['completed_appointments']:,}",

                            "completed-appointments",

                            "✅"

                        ),

                        xs=12,
                        sm=6,
                        md=4,
                        lg=2

                    ),


                    dbc.Col(

                        create_kpi_card(

                            "No-Shows Appointments",

                            f"{kpis['no_show_appointments']:,}",

                            "no-show-appointments",

                            "❌"

                        ),

                        xs=12,
                        sm=6,
                        md=4,
                        lg=2

                    ),


                    dbc.Col(

                        create_kpi_card(

                            "No-Show Percentage",

                            f"{kpis['no_show_rate']:.2f}%",

                            "no-show-rate",

                            "📉"

                        ),

                        xs=12,
                        sm=6,
                        md=4,
                        lg=2

                    ),


                    dbc.Col(

                        create_kpi_card(

                            "Avg Waiting Days",

                            kpis["average_waiting_days"],

                            "average-waiting-days",

                            "⏳"

                        ),

                        xs=12,
                        sm=6,
                        md=4,
                        lg=2

                    ),


                    dbc.Col(

                        create_kpi_card(

                            "Patients Average Age",

                            kpis["average_age"],

                            "average-age",

                            "👥"

                        ),

                        xs=12,
                        sm=6,
                        md=4,
                        lg=2

                    )

                ],

                className="g-4 mb-4"

            ),



            # ==================================================
            # BUSINESS INSIGHTS
            # ==================================================

            html.H2(

                "Business Insights",

                className="section-title"

            ),



            dbc.Card(

                dbc.CardBody(

                    [

                        html.Ul(

                            [

                                html.Li(
                                    "No-show behavior can be analyzed through demographic and appointment characteristics."
                                ),

                                html.Li(
                                    "Longer waiting periods may increase the probability of missed appointments."
                                ),

                                html.Li(
                                    "SMS reminders should be evaluated as a patient engagement strategy."
                                )

                            ]

                        )

                    ]

                ),

                className="insight-card mb-4"

            ),



            # ==================================================
            # DASHBOARD TABS
            # ==================================================

            dcc.Tabs(

                id="dashboard-tabs",

                value="patient-profile",

                className="custom-tabs",

                children=[


                    dcc.Tab(

                        label="Patient Profile",

                        value="patient-profile",

                        className="custom-tab",

                        selected_className="custom-tab--selected",

                        children=[

                            dbc.Row(

                                [

                                    dbc.Col(

                                        create_chart_card(
                                            "gender-chart",
                                            "Gender Distribution"
                                        ),

                                        xs=12,
                                        lg=6

                                    ),


                                    dbc.Col(

                                        create_chart_card(
                                            "age-chart",
                                            "Age Distribution"
                                        ),

                                        xs=12,
                                        lg=6

                                    )

                                ],

                                className="g-4"

                            ),


                            dbc.Row(

                                [

                                    dbc.Col(

                                        create_chart_card(
                                            "age-group-chart",
                                            "Patients by Age Group"
                                        ),

                                        xs=12,
                                        lg=6

                                    ),


                                    dbc.Col(

                                        create_chart_card(
                                            "neighbourhood-chart",
                                            "Top 10 Neighbourhoods"
                                        ),

                                        xs=12,
                                        lg=6

                                    )

                                ],

                                className="g-4"

                            )

                        ]

                    ),



                    dcc.Tab(

                        label="Appointment Analysis",

                        value="appointment-analysis",

                        className="custom-tab",

                        selected_className="custom-tab--selected",

                        children=[

                            dbc.Row(

                                [

                                    dbc.Col(

                                        create_chart_card(
                                            "weekday-chart",
                                            "Appointments by Weekday"
                                        ),

                                        xs=12,
                                        lg=6

                                    ),


                                    dbc.Col(

                                        create_chart_card(
                                            "month-chart",
                                            "Appointments by Month"
                                        ),

                                        xs=12,
                                        lg=6

                                    )

                                ],

                                className="g-4"

                            ),



                            dbc.Row(

                                [

                                    dbc.Col(

                                        create_chart_card(
                                            "waiting-histogram",
                                            "Waiting Days Distribution"
                                        ),

                                        xs=12,
                                        lg=6

                                    ),


                                    dbc.Col(

                                        create_chart_card(
                                            "waiting-boxplot",
                                            "Waiting Days by Status"
                                        ),

                                        xs=12,
                                        lg=6

                                    )

                                ],

                                className="g-4"

                            )

                        ]

                    ),



                    dcc.Tab(

                        label="No-Show Analysis",

                        value="noshow-analysis",

                        className="custom-tab",

                        selected_className="custom-tab--selected",

                        children=[


                            dbc.Row(

                                [

                                    dbc.Col(

                                        create_chart_card(
                                            "noshow-gender-chart",
                                            "No-Show Rate by Gender"
                                        ),

                                        xs=12,
                                        lg=4

                                    ),


                                    dbc.Col(

                                        create_chart_card(
                                            "noshow-factor-chart",
                                            "No-Show Rate by Health & Appointment Factors"
                                        ),

                                        xs=12,
                                        lg=4

                                    ),


                                    dbc.Col(

                                        create_chart_card(
                                            "noshow-neighbourhood-chart",
                                            "Top 10 Neighborhoods by No-Show Rate"
                                        ),

                                        xs=12,
                                        lg=4

                                    )

                                ],

                                className="g-4"

                            )

                        ]

                    ),



                    dcc.Tab(

                        label="Correlation Analysis",

                        value="correlation-analysis",

                        className="custom-tab",

                        selected_className="custom-tab--selected",

                        children=[

                            create_chart_card(

                                "correlation-heatmap",

                                "Correlation Between Patient and Appointment Factors"

                            )

                        ]

                    )

                ]

            ),



            # ==================================================
            # FOOTER
            # ==================================================

            dbc.Card(

                dbc.CardBody(

                    [

                        html.H5(

                            "Healthcare Analytics",

                            className="footer-title"

                        ),

                        html.P(

                            "Powered by Dash + Plotly",

                            className="footer-text"

                        )

                    ]

                ),

                className="dashboard-footer mt-5"

            )


        ],

        fluid=True,

        className="dashboard-container"

    )