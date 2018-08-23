import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import *


df = pd.read_csv("../data/CETRAD_rainfall.csv")  # Read in the raw csv data.

# Step 1. Convert text strings into datetime objects.
format = '%m/%d/%y'  # Column RDate has data in M/D/YY
df['Datetime'] = pd.to_datetime(df['RDate'], format=format)  # Create a new column of datetime objects using RDate.  # NOQA

# 2. Step 2. Convert future dates inferred during the conversion back into
# 20th century dates. Python is a future-looking programming language, and
# assumes that 1/1/34 is Jan 1, 2034. We can fix this by finding all the dates
# in the future (dt > datetime.now()) and removing 100 years from
# their value. This requires using the relativedelta function, which handles
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

rainfall_data = df
