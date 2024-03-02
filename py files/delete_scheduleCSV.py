import schedule
import time
from menu_choice_functions import *

csv_file = 'user_login.csv'
def main():
   # Schedule job to run every hour
    schedule.every().hour.do(delete_and_recreate_csv, csv_file)
    print('done')
    
    # Main loop to keep script running
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()