from textwrap import indent
import pandas as pd
from datetime import datetime
import schedule




""" def delete_rows_every_hour():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('your_file.csv')

    # Assuming 'timestamp_column' is the column representing the timestamp
    # Convert the timestamp column to datetime format
    df['timestamp_column'] = pd.to_datetime(df['timestamp_column'])

    # Delete rows for every one hour interval
    df = df[df['timestamp_column'].dt.hour % 2 != 0]

    # Write the modified DataFrame back to the CSV file in 'w' mode to overwrite
    df.to_csv('your_file.csv', index=False)

# Schedule the task to run every hour
schedule.every().hour.do(delete_rows_every_hour)

# Run the scheduler continuously
while True:
    schedule.run_pending() """


""" next_hour = df[hour]+1
if(df[hour] == next_hour):
    df.to_csv(csv_file, mode = 'w', index = False)

else:
     df.to_csv(csv_file, mode = 'a', index = False)
 """