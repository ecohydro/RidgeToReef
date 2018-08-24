import numpy as np
from datetime import datetime, timedelta
from dateutil.relativedelta import *
import pandas as pd


def read_data():

    # Read in the raw csv data.
    df = pd.read_csv("../data/CETRAD_rainfall.csv")

    # Step 1. Convert text strings into datetime objects.
    format = '%m/%d/%y'  # Column RDate has data in M/D/YY
    df['Datetime'] = pd.to_datetime(df['RDate'], format=format)  # Create a new column of datetime objects using RDate.  # NOQA

    # 2. Step 2. Convert future dates inferred during the conversion back into
    # 20th century dates. Python is a future-looking programming language, and
    # assumes that 1/1/34 is Jan 1, 2034. We fix this by finding all the dates
    # in the future (dt > datetime.now()) and removing 100 years from
    # their value. This requires using a relativedelta function, which handles
    # weird stuff like leap years.
    df['Datetime'] = df['Datetime'].map(
        lambda dt: dt+relativedelta(years=-100) if dt > datetime.now() else dt)

    # Step 3. Extract the Year and Month from the Datetime to make
    # aggregation easier.
    df['Year'] = [dt.year for dt in df['Datetime']]
    df['Month'] = [dt.month for dt in df['Datetime']]

    # Step 4. Use the Datetime values as the index for this dataframe.
    df = df.set_index(pd.DatetimeIndex(df['Datetime']))  # Set the Datetime column as the dataframe index # NOQA

    # Step 5.  Delete the old RDate column, which we no longer need.
    # We will keep the Datetime column, in case we need it later.
    df = df.drop(['RDate'], axis=1)

    return df


def analyze_rainfall(station='JACOBSON FARM', start_year=None, end_year=None):
    rainfall_data = read_data()
    data = rainfall_data[[station, 'Month', 'Year', 'Datetime']]
    if not start_year:
        start_year = min(data['Year'])
    if not end_year:
        end_year = max(data['Year'])
    if start_year < min(data['Year']):
        start_year = min(data['Year'])
    if end_year > max(data['Year']):
        end_year = max(data['Year'])
    data = data.loc[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

    # First, find all the rows in the data where it rained and group by month.
    rain_days = data.loc[data[station] > 0]

    # Find all locations in the data where an observation was made.
    all_days = data.loc[data[station] >= 0]

    lambda_by_month = (
        rain_days.groupby('Month')[station].count() /
        all_days.groupby('Month')[station].count()
    )

    alpha = rain_days[station].mean()

    return alpha, lambda_by_month, data


def simulate_rainfall(
        planting_date=datetime.today(),
        days_to_maturity=150,
        lambda_values,
        alpha_value):
    """ Simulates a season of rainfall.

    Usage:

    simulate_rainfall(
        planting_date=datetime, days_to_maturity,
        lambda_values, alpha_values
    )

    Arguments:
        - planting_date = datetime object specifying month/day of planting.
        - days_to_maturity - integer number of days until crop is mature
        - lambda_values - array of 12 lambda values; one for each month
        - alpha value - a constant average storm depth

    """
    start_date = planting_date
    end_date = planting_date + timedelta(days=days_to_maturity)
    datetimes = np.arange(
        start_date, end_date, timedelta(days=1)).astype(datetime)
    month_value_by_day = np.array([datetime.month for datetime in datetimes])
    lambda_values = np.array([lambda_by_month[i] for i in month_value_by_day])
