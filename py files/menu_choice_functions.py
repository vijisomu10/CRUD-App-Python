import os
import pandas as pd
import mysql.connector
from openpyxl import load_workbook
from datetime import datetime, timedelta

from create_db_mysql import *
from validation_functions import *
from database import connect_to_database
from mongo_post import *


con = connect_to_database()
cursor = con.cursor()
csv_file = 'user_login.csv'
current_time = datetime.now()
records_csv = {'datetime_column': [datetime.now()]}


def create_new_user_reg():
    firstname = input('Enter your firstname: ')
    lastname = input('Enter your lastname: ')
    street_name = input('Enter your streetname: ')
    city = input('Enter your city: ')
    country = input('Enter your country: ')
    postal_code = postal_code_validation()
    mobile_number = mobile_number_validation()            
    return (firstname, lastname, street_name, city, country, postal_code, mobile_number)

def create_login():    
    username = input('Enter your username: ')        
    while True: 
        passWord = input('Enter your password:')
        password_validate = correctPW(passWord)
        confirm_password = input('confirm your password: ')  
        if password_validate == confirm_password:
            break
        print('Incorrect password! Try again!')
    return username, password_validate


def login_menu_choice():
    print('Welcome to User page')
    print('--------Menu--------')
    print('1. Update the account details')
    print('2. Post a message')
    print('3. Delete the account')
    print('4. Logout')


def login_menu():    
    while True:  
        login_menu_choice()    
            
        choose = input('Enter your choice: ')
        if choose == '1':         
            update_menu()
                        
        elif choose == '2':
            # Call post_message to prompt user for message details
            user_choice = post_message()
            if user_choice:
                ptitle, pmessage = user_choice
                #add_message(username, ptitle, pmessage) 
                collection.insert_one({
                    "Username": username,
                    "Title": ptitle,
                    "Message": pmessage
                })
                print('Message posted')
            client.close()
        
        elif choose == '3':
            delete_user_data()
                    
        elif choose == '4':   
            print('You chose to logout, See you another time.')  
            delete_old_data(csv_file)
            exit()

        else:
            print('Invalid choice. Please enter a valid number.')       

def login_user():    
    cursor.execute(select_table_user_login)
    user_login_data = cursor.fetchall()
    
    global username, password
    username = input('Enter your username: ')
    if any(ulogin_tuple[2] == username for ulogin_tuple in user_login_data):
        password = input('Enter your password: ')     
        if any (ulogin_tuple[2] == username and ulogin_tuple[3] == password for ulogin_tuple in user_login_data):
            print('Login successful!')  
            login_entry_csv()
            login_entry_excel()
            con.commit()        
        else:
            print('username or password is incorrect!')   
    else:
        print('Username is not there! Write the correct username or create a new account!')

def login_entry_csv():    
    #login entry to csv
    records_csv = {'datetime_column': [datetime.now()]}
    df = pd.DataFrame(records_csv)    
    write_header = not os.path.exists(csv_file)
    df.to_csv(csv_file, index=False, mode='a', header=write_header)       
        
    #to be deleted after final call    
    l = f'{current_time.year}, {current_time.month}, {current_time.day}, {current_time.hour}, {current_time.minute}'
    with open('user_log.txt', 'a', encoding='utf-8') as f:
        f.write(l + '\n')
    #--------------------------------------------------------    

def login_entry_excel():      
    df = pd.read_csv('user_login.csv')

    # Extract date and time components
    df['datetime_column'] = pd.to_datetime(df['datetime_column'])
    df['Year'] = df['datetime_column'].dt.year
    df['Month'] = df['datetime_column'].dt.month
    df['Date'] = df['datetime_column'].dt.day
    df['Hour'] = df['datetime_column'].dt.hour

    # Group by hour and count occurrences
    df_counts = df.groupby(['Year', 'Month', 'Date', 'Hour']).size().reset_index(name='NumberOfOccurences')

    # Path to your Excel file
    excel_file = 'C:\\Users\\vijis\\python_ovningar\\CRUD_Submission_2\\login_history.xlsx'

    # Check if the file exists
    if os.path.isfile(excel_file):
        # Load the existing workbook
        book1 = load_workbook(excel_file)
        # Append data to existing worksheet or create a new one if it doesn't exist
        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
            writer.workbook = book1
            writer.sheets.update(dict((ws.title, ws) for ws in book1.worksheets))
    else:
        # Create a new workbook
        writer = pd.ExcelWriter(excel_file, engine='openpyxl')

    # Append the data to the Excel file without including the index
    df_counts.to_excel(excel_file, index=False) 

def update_menu_choice():
    print('Choose options to update your personal details')
    print('--------Menu--------')
    print('1. Firstname')
    print('2. Lastname')
    print('3. Street Name')
    print('4. City')
    print('5. Country')
    print('6. Postal Code')
    print('7. Mobile Number')
    print('8. Login Password')
    print('9. Exit to Main menu')

def update_menu():
    print('confirm your login...')
    login_user()
    while True:        
        update_menu_choice()     
        choice = input('Enter your choice: ')          
        cursor.execute(query_retrieve_user, (username, password))
        result = cursor.fetchone()     
        
        if choice == '1':                     
            if result:
                user_reg_id = result[0]
                new_firstname = input("Enter new firstname: ")        
                cursor.execute(update_FN, (new_firstname, user_reg_id))
                con.commit()
                print("Firstname updated successfully.")                
            else:
                print("Username not found.")
            
        elif choice == '2':  
            if result:
                user_reg_id = result[0]
                new_lastname = input("Enter new lastname: ")        
                cursor.execute(update_LN, (new_lastname, user_reg_id))
                print("Lastname updated successfully.")
                con.commit()
            else:
                print("Username not found.")
        
        elif choice == '3':             
            if result:
                user_reg_id = result[0]
                new_streetname = input("Enter new streetname: ")        
                cursor.execute(update_street, (new_streetname, user_reg_id))
                print("Streetname updated successfully.")
                con.commit()
            else:
                print("Username not found.")    
        
        elif choice == '4':  
            if result:
                user_reg_id = result[0]
                new_city = input("Enter new city: ")        
                cursor.execute(update_city, (new_city, user_reg_id))
                print("City updated successfully.")
                con.commit()
            else:
                print("Username not found.")
        
        elif choice == '5':  
            if result:
                user_reg_id = result[0]
                new_country = input("Enter new country: ")        
                cursor.execute(update_country, (new_country, user_reg_id))
                print("Country updated successfully.")
                con.commit()
            else:
                print("Username not found.")
        
        elif choice == '6':  
            if result:
                user_reg_id = result[0]
                new_postalcode = input("Enter new postalcode: ")        
                cursor.execute(update_postalcode, (new_postalcode, user_reg_id))
                print("Postal Code updated successfully.")
                con.commit()
            else:
                print("Username not found.")
        
        elif choice == '7':  
            if result:
                user_reg_id = result[0]
                new_mobileN = input("Enter new mobile number: ")        
                cursor.execute(update_mobile, (new_mobileN, user_reg_id))
                print("Mobile Number updated successfully.")
                con.commit()
            else:
                print("Username not found.")

        elif choice == '8':
            cursor.execute(query_retrieve_userLogin, (username, password))
            result1 = cursor.fetchone()   
            if result1: 
                user_login_id = result1[0]
                new_password = input('Enter new password:')
                cursor.execute(update_password, (new_password, user_login_id))
                print('Password updated successfully')
                con.commit()
            else:
                print('Username not found')

        elif choice == '9':
            login_menu()
            delete_old_data(csv_file)

def delete_user_data():
    try:
        login_user()
        select_user_id_query = "SELECT id FROM user WHERE username = %s AND password = %s"
        cursor.execute(select_user_id_query, (username, password))
        user_id = cursor.fetchone()

        if user_id:
            user_id = user_id[0]            
            cursor.execute(delete_user_login_query, (user_id,))
                
            delete_user_query = "DELETE FROM user WHERE id = %s"
            cursor.execute(delete_user_query, (user_id,))
            con.commit()

            print("User and associated login data deleted successfully!")
        else:
            print("No user found with the provided username and password.")
    except mysql.connector.Error as error:
        print("Error while deleting user and associated login data:", error)

def delete_old_data(csv_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    # Convert timestamp column to datetime type
    df['datetime_column'] = pd.to_datetime(df['datetime_column'])
    # Determine the current time and the time one hour ago
    hour_ago = current_time - timedelta(hours=1)
    # Filter rows where timestamp is within the last hour
    df = df[df['datetime_column'] >= hour_ago]
    # Write the filtered DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)
        

            

    
        