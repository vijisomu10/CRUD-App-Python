import schedule
import time
from menu_choice_functions import delete_old_data, csv_file

def main():
   # Schedule job to run every hour
    schedule.every().hour.do(delete_old_data, csv_file)
    print('done')
    
    # Main loop to keep script running
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()