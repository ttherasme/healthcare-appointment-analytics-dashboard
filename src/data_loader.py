"""
data_loader.py

Loads and prepares the Healthcare Appointment dataset
for use throughout the Dash application.
"""

from pathlib import Path

import pandas as pd


def load_data():
    """
    Load, clean, and prepare the healthcare appointment dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataframe ready for analysis.
    """

    # --------------------------------------------------
    # Load data
    # --------------------------------------------------
    data_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "healthcare_appointments.csv"
    )

    df = pd.read_csv(data_path)

    # --------------------------------------------------
    # Rename columns
    # --------------------------------------------------
    df.columns = [
        "patient_id",
        "appointment_id",
        "gender",
        "scheduled_day",
        "appointment_day",
        "age",
        "neighbourhood",
        "scholarship",
        "hypertension",
        "diabetes",
        "alcoholism",
        "handicap",
        "sms_received",
        "no_show",
    ]

    # --------------------------------------------------
    # Data types
    # --------------------------------------------------
    df["scheduled_day"] = pd.to_datetime(df["scheduled_day"])
    df["appointment_day"] = pd.to_datetime(df["appointment_day"])

    # Remove time portion (keep datetime type)
    df["scheduled_day"] = df["scheduled_day"].dt.normalize()
    df["appointment_day"] = df["appointment_day"].dt.normalize()

    df["patient_id"] = df["patient_id"].astype(str)
    df["appointment_id"] = df["appointment_id"].astype(str)
    df["age"] = df["age"].astype(int)

    # --------------------------------------------------
    # Standardize text
    # --------------------------------------------------
    df["gender"] = df["gender"].str.upper()

    df["neighbourhood"] = (
        df["neighbourhood"]
        .str.strip()
        .str.title()
    )

    # --------------------------------------------------
    # Convert No Show
    # --------------------------------------------------
    df["no_show"] = (
        df["no_show"]
        .str.strip()
        .str.upper()
        .map(
            {
                "NO": 0,
                "YES": 1
            }
        )
        .astype(int)
    )

    # --------------------------------------------------
    # Remove duplicate rows
    # --------------------------------------------------
    df = df.drop_duplicates()

    # --------------------------------------------------
    # Remove missing values
    # --------------------------------------------------
    df = df.dropna(subset=["appointment_id"])

    # --------------------------------------------------
    # Feature Engineering
    # --------------------------------------------------

    # Waiting Days
    df["waiting_days"] = (
        df["appointment_day"]
        - df["scheduled_day"]
    ).dt.days

    # Remove negative waiting days
    df = df[df["waiting_days"] >= 0]

    # Age Groups
    df["age_group"] = pd.cut(
        df["age"],
        bins=[-1, 17, 34, 49, 64, 120],
        labels=[
            "0-17",
            "18-34",
            "35-49",
            "50-64",
            "65+"
        ]
    )

    # Show Status
    df["show_status"] = df["no_show"].map(
        {
            0: "Show",
            1: "No Show"
        }
    )

    # Weekday
    df["appointment_weekday"] = (
        df["appointment_day"]
        .dt.day_name()
    )

    # Month
    df["appointment_month"] = (
        df["appointment_day"]
        .dt.month_name()
    )

    return df