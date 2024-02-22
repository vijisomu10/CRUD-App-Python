""" def login_user():    
    cursor.execute(select_table_user_login)
    user_login_data = cursor.fetchall()
    
    username = input('Enter your username: ')
    if any(ulogin_tuple[2] == username for ulogin_tuple in user_login_data):
        password = input('Enter your password: ')
        
        if any (ulogin_tuple[2] == username and ulogin_tuple[3] == password for ulogin_tuple in user_login_data):
            print('Login successful!')
            #records_csv.append((username, datetime.now()))
            records_csv = [datetime.now()]
            df = pd.DataFrame(records_csv)
            df.to_csv('user_login.csv', index = False, mode='a')

            #to be deleted after final call
            time = datetime.now()
            l = f'{time.year}, {time.month}, {time.day}, {time.hour}'
            with open('user_log.txt', 'a', encoding='utf-8') as f:
                    f.write(l + '\n')
            #--------------------------------------------------------      
            
        else:
            print('username or password is incorrect!')
    
    else:
        print('Username is not there! Write the correct username or create a new account!')
    
    conn.commit()
     """




#in choice menu 2
""" file_exists = os.path.isfile('user_login.csv')

            with open('user_login.csv', 'a', encoding='utf-8', newline='') as f:
                one_hour_login_records = csv.writer(f)
                
                if not file_exists:                    
                    header = ['username', 'timestamp']
                    one_hour_login_records.writerow(header)
                
                for records in records_csv:
                    one_hour_login_records.writerow(records)            
             """


""" def csv_to_hourly_excel():
    df = pd.read_csv('user_login.csv')
    # Drop the first column by its positional index
    #df.drop(df.columns[0], axis=1, inplace=True)
       
    df['date_time_column'] = pd.to_datetime(df['timestamp'])
    df['Month'] = pd.to_datetime(df['timestamp']).dt.month
    df['Date'] = pd.to_datetime(df['timestamp']).dt.date
    df['Hour'] = pd.to_datetime(df['timestamp']).dt.hour

    login_counts = df.groupby(['Year', 'Month', 'Date', 'Hour']).size()\
                    .reset_index(name='NumberOfOccurences')
    # Update the login history with the new data
    df = pd.concat([df, login_counts], ignore_index=True)

    excelWriter = pd.ExcelWriter('login_history.xlsx')
    df.to_excel(excelWriter, index=False)
    excelWriter.close() """


import pandas as pd
from datetime import datetime, timedelta
import os
import time

last_write_time = None

def delete_rows_every_hour():
    global last_write_time
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv('your_file.csv')

    # Assuming 'timestamp_column' is the column representing the timestamp
    # Convert the timestamp column to datetime format
    df['timestamp_column'] = pd.to_datetime(df['timestamp_column'])

    # Delete rows for every one hour interval
    df = df[df['timestamp_column'].dt.hour % 2 != 0]

    # Determine the write mode based on elapsed time since last write
    write_mode = 'a' if last_write_time and (datetime.now() - last_write_time) < timedelta(hours=1) else 'w'
    
    # Write the modified DataFrame back to the CSV file
    df.to_csv('your_file.csv', index=False, mode=write_mode)

    # Update the last write time
    last_write_time = datetime.now()

while True:
    # Perform the deletion and writing operation
    delete_rows_every_hour()
    
    # Sleep for a specified duration (e.g., 1 minute)
    time.sleep(60)  # 60 seconds = 1 minute
