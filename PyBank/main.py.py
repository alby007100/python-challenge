import datetime

end_date = datetime.datetime(2010,1,1)
start_date = datetime.datetime(2017, 2, 1)

num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

print("Total Month:", num_months)
