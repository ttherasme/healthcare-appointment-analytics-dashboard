"""
kpi.py

Functions to calculate Key Performance Indicators (KPIs)
for the Healthcare Appointment Dashboard.
"""

import pandas as pd


def get_total_appointments(df: pd.DataFrame) -> int:
    """
    Return the total number of appointments.
    """
    return len(df)


def get_completed_appointments(df: pd.DataFrame) -> int:
    """
    Return the number of completed appointments.
    """
    return (df["no_show"] == 0).sum()


def get_no_show_appointments(df: pd.DataFrame) -> int:
    """
    Return the number of no-show appointments.
    """
    return (df["no_show"] == 1).sum()


def get_completion_rate(df: pd.DataFrame) -> float:
    """
    Return the completion rate as a percentage.
    """
    return ((df["no_show"] == 0).mean()) * 100


def get_no_show_rate(df: pd.DataFrame) -> float:
    """
    Return the no-show rate as a percentage.
    """
    return ((df["no_show"] == 1).mean()) * 100


def get_average_waiting_days(df: pd.DataFrame) -> float:
    """
    Return the average waiting time in days.
    """
    return round(df["waiting_days"].mean(), 1)


def get_average_age(df: pd.DataFrame) -> float:
    """
    Return the average patient age.
    """
    return round(df["age"].mean(), 1)


def get_kpis(df: pd.DataFrame) -> dict:
    """
    Return all dashboard KPIs as a dictionary.
    """

    return {
        "total_appointments": get_total_appointments(df),
        "completed_appointments": get_completed_appointments(df),
        "no_show_appointments": get_no_show_appointments(df),
        "completion_rate": get_completion_rate(df),
        "no_show_rate": get_no_show_rate(df),
        "average_waiting_days": get_average_waiting_days(df),
        "average_age": get_average_age(df),
    }