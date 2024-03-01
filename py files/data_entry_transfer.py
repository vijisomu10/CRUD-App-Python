#login entry to csv and excel
import os
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook

csv_file = 'user_login.csv'

# Function to add login entry to CSV
def login_entry_csv():    
    current_time = datetime.now()
    records_csv = {'datetime_column': [current_time]}
    df = pd.DataFrame(records_csv)    
    write_header = not os.path.exists(csv_file)
    df.to_csv(csv_file, index=False, mode='a', header=write_header)       

def login_entry_excel():      
    df = pd.read_csv('user_login.csv')
    df['datetime_column'] = pd.to_datetime(df['datetime_column'])
    df['Year'] = df['datetime_column'].dt.year
    df['Month'] = df['datetime_column'].dt.month
    df['Date'] = df['datetime_column'].dt.day
    df['Hour'] = df['datetime_column'].dt.hour
    # Group by hour and count occurrences
    df_counts = df.groupby(['Year', 'Month', 'Date', 'Hour']).  \
                size().reset_index(name='NumberOfOccurences')

    excel_file = 'C:\\Users\\vijis\\python_ovningar\\CRUD_Submission_2\\login_history.xlsx'

    if os.path.isfile(excel_file):
        # Load the existing workbook
        book1 = load_workbook(excel_file)
        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
            writer.workbook = book1
            writer.sheets.update(dict((ws.title, ws) for ws in book1.worksheets))
    else:
        writer = pd.ExcelWriter(excel_file, engine='openpyxl')

    df_counts.to_excel(excel_file, index=False) 
