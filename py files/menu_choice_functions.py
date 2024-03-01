import os
import pandas as pd
from datetime import datetime, timedelta

from create_db_mysql import *
from validation_functions import *
from data_entry_transfer import *
from database_connect import connect_to_database
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
    print('3. Logout')

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
                collection.insert_one({
                    "Username": username,
                    "Title": ptitle,
                    "Message": pmessage
                })
                print('Message posted')
            client.close()
        
        elif choose == '3':
            print('You chose to logout, See you another time.')  
            #delete_old_data(csv_file)
            exit()

        else:
            print('Invalid choice. Please enter a valid number.')       

def login_user():    
    cursor.execute(select_table_user_login)
    user_login_data = cursor.fetchall()
    while True:
        global username, password
        username = input('Enter your username: ')
        if any(ulogin_tuple[2] == username for ulogin_tuple in user_login_data):
            password = input('Enter your password: ')     
            if any (ulogin_tuple[2] == username and ulogin_tuple[3] == password for ulogin_tuple in user_login_data):
                print('Login successful!')  
                login_entry_csv()
                login_entry_excel()
                con.commit()       
                break 
            else:
                print('username or password is incorrect!')   
        else:
            print('Username is not there! Write the correct username or create a new account!')


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
                while True:
                    new_password = input('Enter new password:')
                    pwd_validate = correctPW(new_password)
                    confirm_new_password = input('Confirm new password:')
                    if pwd_validate == confirm_new_password:
                        cursor.execute(update_password, (confirm_new_password, user_login_id))
                        print('New password updated successfully')
                    else:
                        print('Incorrect password! Try again!')
                    con.commit()
            else:
                print('Username not found')

        elif choice == '9':
            login_menu()
            #delete_old_data(csv_file)


def delete_old_data(csv_file):
    df = pd.read_csv(csv_file)
    df['datetime_column'] = pd.to_datetime(df['datetime_column'])
    hour_ago = current_time - timedelta(hours=1)
    df = df[df['datetime_column'] >= hour_ago]  # Check if the file exists before attempting to delete it
    if os.path.exists(csv_file):
        os.remove(csv_file)
        print("CSV file deleted successfully.")
    
    df = pd.DataFrame(records_csv)
    df.to_csv(csv_file, index=False)
    print("CSV file recreated successfully.")

# Function to delete and recreate the CSV file with new data
def delete_and_recreate_csv():
    # Check if the file exists before attempting to delete it
    if os.path.exists(csv_file):
        os.remove(csv_file)
        print("CSV file deleted successfully.")
    
    df = pd.DataFrame(records_csv)
    
    # Write data to CSV file
    df.to_csv(csv_file, index=False)
    print("CSV file recreated successfully.")