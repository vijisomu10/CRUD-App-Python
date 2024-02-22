from database import *
from create_db_mysql import *
from menu_choice_functions import *
from validation_functions import *


def menu_choice():
    print('Welcome')
    print('--------Menu--------')
    print('1. Register new user')
    print('2. Already registered user, login')
    print('3. Message-search and counts')
    print('4. Exit')

def main_menu():    
    while True:   
        menu_choice()        
        choice = input('Enter your choice: ')  
        if choice == '1':            
            dt1 = create_new_user_reg()
            print('Registration details created')            
            cursor.execute(insert_user, dt1)
            
            dt2 = create_login()
            cursor.execute(insert_user_login, dt2)
            print('Login details registered')
            
            login_entry_csv()
            login_entry_excel()
            
        elif choice == '2':
            #Already registered user, login
            login_user()  
            login_menu()          
                    
        elif choice == '3': 
            message_search_and_counts()

        elif choice == '4':                     
            print('You chose to exit the program, See you another time.')
            delete_old_data(csv_file)
            exit()

        else:
            print('Invalid choice. Please enter a valid number.')      

    
def create_tables(cursor):
    try:
        cursor.execute(create_table_user)
        cursor.execute(create_table_user_login)
        print("Tables created successfully.")
    except Exception as e:
        print('Error creating tables:', e)

def main():
    conn = connect_to_database()
    if conn.is_connected():
        cursor = conn.cursor()
        try:
            create_tables(cursor)
            main_menu()
        finally:
            close_database_connection(conn, cursor)


if __name__ == '__main__':
    main()       

