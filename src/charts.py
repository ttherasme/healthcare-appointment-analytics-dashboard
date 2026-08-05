"""
charts.py

Plotly visualizations for the Healthcare Appointment Dashboard.
"""

import pandas as pd
import plotly.express as px



# ============================================================
# Common Chart Layout
# ============================================================

def apply_layout(fig, title):

    """
    Apply common dashboard styling.
    """

    fig.update_layout(

        template="plotly_white",

        height=380,

        autosize=True,

        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        ),

        font=dict(
            size=12
        ),

        legend=dict(
            orientation="v",
            x=1.02,
            y=0.5,
            xanchor="left",
            yanchor="middle"
        )

    )


    return fig



# ============================================================
# Empty Chart
# ============================================================

def empty_chart(message):

    fig = px.scatter(
        x=[],
        y=[]
    )


    fig.update_layout(

        title=message,

        template="plotly_white",

        height=350

    )


    return fig



# ============================================================
# Patient Profile
# ============================================================


def create_gender_distribution(df):

    if df.empty:
        return empty_chart("No Gender Data")


    data = (
        df["gender"]
        .value_counts()
        .reset_index()
    )


    data.columns = [
        "Gender",
        "Count"
    ]


    fig = px.pie(

        data,

        names="Gender",

        values="Count",

        hole=0.55

    )


    fig.update_traces(

        textposition="inside",

        textinfo="percent+label"

    )


    return apply_layout(
        fig,
        "Gender Distribution"
    )



def create_age_histogram(df):

    if df.empty:
        return empty_chart("No Age Data")


    fig = px.histogram(

        df,

        x="age",

        nbins=25

    )


    fig.update_layout(

        xaxis_title="Age",

        yaxis_title="Patients"

    )


    return apply_layout(
        fig,
        "Age Distribution"
    )



def create_age_group_chart(df):

    if df.empty:
        return empty_chart("No Age Group Data")


    data = (

        df["age_group"]

        .value_counts()

        .reset_index()

    )


    data.columns = [

        "Age Group",

        "Count"

    ]


    fig = px.bar(

        data,

        x="Age Group",

        y="Count"

    )


    return apply_layout(

        fig,

        "Patients by Age Group"

    )



def create_neighbourhood_distribution(df):

    if df.empty:
        return empty_chart("No Neighborhood Data")


    data = (

        df["neighbourhood"]

        .value_counts()

        .head(10)

        .reset_index()

    )


    data.columns = [

        "Neighbourhood",

        "Appointments"

    ]


    fig = px.bar(

        data,

        x="Appointments",

        y="Neighbourhood",

        orientation="h"

    )


    return apply_layout(

        fig,

        "Top 10 Neighbourhoods"

    )



# ============================================================
# Appointment Analysis
# ============================================================


def create_weekday_chart(df):

    if df.empty:
        return empty_chart("No Weekday Data")


    order = [

        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"

    ]


    data = (

        df["appointment_weekday"]

        .value_counts()

        .reindex(order)

        .fillna(0)

        .reset_index()

    )


    data.columns = [

        "Weekday",

        "Appointments"

    ]


    fig = px.bar(

        data,

        x="Weekday",

        y="Appointments"

    )


    return apply_layout(

        fig,

        "Appointments by Weekday"

    )



def create_month_chart(df):

    if df.empty:
        return empty_chart("No Month Data")


    order = [

        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"

    ]


    data = (

        df["appointment_month"]

        .value_counts()

        .reindex(order)

        .dropna()

        .reset_index()

    )


    data.columns = [

        "Month",

        "Appointments"

    ]


    fig = px.line(

        data,

        x="Month",

        y="Appointments",

        markers=True

    )


    return apply_layout(

        fig,

        "Appointments by Month"

    )



def create_waiting_histogram(df):

    if df.empty:
        return empty_chart("No Waiting Data")


    fig = px.histogram(

        df,

        x="waiting_days",

        nbins=30

    )


    return apply_layout(

        fig,

        "Waiting Days Distribution"

    )



def create_waiting_boxplot(df):

    if df.empty:
        return empty_chart("No Waiting Data")


    fig = px.box(

        df,

        x="show_status",

        y="waiting_days"

    )


    return apply_layout(

        fig,

        "Waiting Days by Appointment Status"

    )



# ============================================================
# No-Show Analysis
# ============================================================


def create_noshow_gender_donut(df):

    if df.empty:
        return empty_chart("No Gender Data")


    data = (

        df.groupby("gender")["no_show"]

        .mean()

        .reset_index()

    )


    data["No-Show Rate"] = (

        data["no_show"] * 100

    )


    fig = px.pie(

        data,

        names="gender",

        values="No-Show Rate",

        hole=0.55

    )


    fig.update_traces(

        textinfo="label+percent"

    )


    return apply_layout(

        fig,

        "No-Show Rate by Gender"

    )



def create_noshow_age_group_chart(df):

    if df.empty:
        return empty_chart("No Age Group Data")


    data = (

        df.groupby(
            "age_group",
            observed=True
        )["no_show"]

        .mean()

        .reset_index()

    )


    data["No-Show Rate"] = (

        data["no_show"] * 100

    )


    fig = px.bar(

        data,

        x="No-Show Rate",

        y="age_group",

        orientation="h"

    )


    fig.update_layout(

        xaxis_title="No-Show Rate (%)",

        yaxis_title="Age Group"

    )


    return apply_layout(

        fig,

        "No-Show Rate by Age Group"

    )



def create_noshow_binary_factors_chart(df):

    if df.empty:
        return empty_chart("No Factor Data")


    factors = [

        "scholarship",

        "hypertension",

        "diabetes",

        "alcoholism",

        "sms_received"

    ]


    results = []


    for factor in factors:


        temp = (

            df.groupby(factor)["no_show"]

            .mean()

            .reset_index()

        )


        for _, row in temp.iterrows():


            results.append(

                {

                    "Factor":
                    factor.replace(
                        "_",
                        " "
                    ).title(),


                    "Category":
                    "Yes"
                    if row[factor] == 1
                    else "No",


                    "No-Show Rate":
                    row["no_show"] * 100

                }

            )



    data = pd.DataFrame(results)



    fig = px.bar(

        data,

        x="Factor",

        y="No-Show Rate",

        color="Category",

        barmode="group"

    )


    return apply_layout(

        fig,

        "No-Show Rate by Health & Engagement Factors"

    )



def create_noshow_handicap_chart(df):

    if df.empty:
        return empty_chart("No Handicap Data")


    data = (

        df.groupby("handicap")["no_show"]

        .mean()

        .reset_index()

    )


    data["No-Show Rate"] = (

        data["no_show"] * 100

    )


    fig = px.bar(

        data,

        x="handicap",

        y="No-Show Rate"

    )


    return apply_layout(

        fig,

        "No-Show Rate by Handicap Level"

    )



def create_noshow_neighbourhood_chart(df):

    if df.empty:
        return empty_chart("No Neighborhood Data")


    data = (

        df.groupby("neighbourhood")["no_show"]

        .mean()

        .reset_index()

    )


    data["No-Show Rate"] = (

        data["no_show"] * 100

    )


    data = (

        data.sort_values(

            "No-Show Rate",

            ascending=False

        )

        .head(10)

    )


    fig = px.bar(

        data,

        x="No-Show Rate",

        y="neighbourhood",

        orientation="h"

    )


    return apply_layout(

        fig,

        "Top 10 Neighborhoods by No-Show Rate"

    )



# ============================================================
# Correlation Analysis
# ============================================================


def create_correlation_heatmap(df):

    if df.empty:
        return empty_chart("No Correlation Data")


    columns = [

        "age",

        "scholarship",

        "hypertension",

        "diabetes",

        "alcoholism",

        "handicap",

        "sms_received",

        "waiting_days",

        "no_show"

    ]


    corr = (

        df[columns]

        .corr()

    )


    fig = px.imshow(

        corr,

        text_auto=True,

        aspect="auto",

        color_continuous_scale="RdBu_r"

    )


    return apply_layout(

        fig,

        "Correlation Heatmap"

    )