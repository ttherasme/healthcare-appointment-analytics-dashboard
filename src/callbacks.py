"""
callbacks.py

Contains all Dash callbacks that update
KPIs and charts based on user interaction.
"""


from dash import Input, Output, no_update


from src.kpi import get_kpis


from src.charts import (

    # Patient Profile
    create_gender_distribution,
    create_age_histogram,
    create_age_group_chart,
    create_neighbourhood_distribution,


    # Appointment Analysis
    create_weekday_chart,
    create_month_chart,
    create_waiting_histogram,
    create_waiting_boxplot,


    # No-Show Analysis
    create_noshow_gender_donut,
    create_noshow_binary_factors_chart,
    create_noshow_neighbourhood_chart,


    # Correlation
    create_correlation_heatmap,

)



# ============================================================
# Register Callbacks
# ============================================================

def register_callbacks(app, df):

    """
    Register dashboard callbacks.
    """



    # ========================================================
    # Main Dashboard Callback
    # ========================================================


    @app.callback(

        [

            # -------------------------
            # KPI Cards
            # -------------------------

            Output(
                "total-appointments",
                "children"
            ),

            Output(
                "completed-appointments",
                "children"
            ),

            Output(
                "no-show-appointments",
                "children"
            ),

            Output(
                "no-show-rate",
                "children"
            ),

            Output(
                "average-waiting-days",
                "children"
            ),

            Output(
                "average-age",
                "children"
            ),



            # -------------------------
            # Patient Profile
            # -------------------------

            Output(
                "gender-chart",
                "figure"
            ),

            Output(
                "age-chart",
                "figure"
            ),

            Output(
                "age-group-chart",
                "figure"
            ),

            Output(
                "neighbourhood-chart",
                "figure"
            ),



            # -------------------------
            # Appointment Analysis
            # -------------------------

            Output(
                "weekday-chart",
                "figure"
            ),

            Output(
                "month-chart",
                "figure"
            ),

            Output(
                "waiting-histogram",
                "figure"
            ),

            Output(
                "waiting-boxplot",
                "figure"
            ),



            # -------------------------
            # No-Show Analysis
            # -------------------------

            Output(
                "noshow-gender-chart",
                "figure"
            ),

            Output(
                "noshow-factor-chart",
                "figure"
            ),

            Output(
                "noshow-neighbourhood-chart",
                "figure"
            ),



            # -------------------------
            # Correlation
            # -------------------------

            Output(
                "correlation-heatmap",
                "figure"
            ),

        ],



        [

            # -------------------------
            # Filters
            # -------------------------

            Input(
                "gender-filter",
                "value"
            ),

            Input(
                "age-filter",
                "value"
            ),

            Input(
                "neighbourhood-filter",
                "value"
            ),

            Input(
                "scholarship-filter",
                "value"
            ),

        ]

    )


    def update_dashboard(
        selected_gender,
        selected_age,
        selected_neighbourhood,
        selected_scholarship
    ):

        """
        Update dashboard based on filters.
        """



        # ====================================================
        # Apply Filters
        # ====================================================


        filtered_df = df.copy()



        if selected_gender:

            filtered_df = filtered_df[
                filtered_df["gender"]
                == selected_gender
            ]



        if selected_age:

            filtered_df = filtered_df[
                filtered_df["age_group"]
                == selected_age
            ]



        if selected_neighbourhood:

            filtered_df = filtered_df[
                filtered_df["neighbourhood"]
                == selected_neighbourhood
            ]



        if selected_scholarship is not None:

            filtered_df = filtered_df[
                filtered_df["scholarship"]
                == selected_scholarship
            ]




        # ====================================================
        # KPIs
        # ====================================================


        kpis = get_kpis(filtered_df)



        # ====================================================
        # Return Components
        # ====================================================


        return (

            # -------------------------
            # KPI Values
            # -------------------------

            f"{kpis['total_appointments']:,}",

            f"{kpis['completed_appointments']:,}",

            f"{kpis['no_show_appointments']:,}",

            f"{kpis['no_show_rate']:.2f}%",

            kpis["average_waiting_days"],

            kpis["average_age"],



            # -------------------------
            # Patient Profile
            # -------------------------

            create_gender_distribution(
                filtered_df
            ),

            create_age_histogram(
                filtered_df
            ),

            create_age_group_chart(
                filtered_df
            ),

            create_neighbourhood_distribution(
                filtered_df
            ),



            # -------------------------
            # Appointment Analysis
            # -------------------------

            create_weekday_chart(
                filtered_df
            ),

            create_month_chart(
                filtered_df
            ),

            create_waiting_histogram(
                filtered_df
            ),

            create_waiting_boxplot(
                filtered_df
            ),



            # -------------------------
            # No-Show Analysis
            # -------------------------

            create_noshow_gender_donut(
                filtered_df
            ),

            create_noshow_binary_factors_chart(
                filtered_df
            ),

            create_noshow_neighbourhood_chart(
                filtered_df
            ),



            # -------------------------
            # Correlation
            # -------------------------

            create_correlation_heatmap(
                filtered_df
            ),

        )




    # ========================================================
    # Reset Filters Callback
    # ========================================================


    @app.callback(

        [

            Output(
                "gender-filter",
                "value"
            ),

            Output(
                "age-filter",
                "value"
            ),

            Output(
                "neighbourhood-filter",
                "value"
            ),

            Output(
                "scholarship-filter",
                "value"
            ),

        ],

        Input(
            "reset-filters",
            "n_clicks"
        ),

        prevent_initial_call=True

    )


    def reset_filters(n_clicks):

        """
        Reset all dashboard filters.
        """

        if n_clicks:

            return (

                None,

                None,

                None,

                None

            )


        return (

            no_update,

            no_update,

            no_update,

            no_update

        )