"""
The python file to check the functions in this repo/project.
"""
import datetime
import sys
sys.path.append('C:/Users/sawan/Projects/QuantBinary')
import Base.utilities.utils as utils
import Satin_Bower.indicators as sb

api_key = "PKDX1ONV8MASSY7TKAAG"
secret_key = "hvSF9OV0X9IXR6140I6nZcxEgVVOMaQKQoq7hWBo"

data = utils.get_historical_stock_data(api_key, secret_key, "AAPL", start_date=datetime.datetime(2023, 1, 1))
print(data.head())
print("Output")

# Trying out the functions in the Repo/Project
print(sb.moving_average(data, 2))
print(sb.mcginley_dynamic_average(data, 20, 'close', True))
print(sb.exponential_moving_average(data))
print(sb.supertrend(data))
print(data.reset_index().index.values)
