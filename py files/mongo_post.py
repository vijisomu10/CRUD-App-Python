from pymongo import MongoClient

client = MongoClient ("mongodb://localhost:27017/")
db = client.crud_app
collection = db.postMessaages


def post_message():    
    post_message = input('Would you like to post a message(Y/N)?')
    if post_message.upper() == 'Y':             
        ptitle = input('In which title you want to post the message?')
        pmessage = input('Enter your message:')
        choice = input("Choose what to add (image/video/link): ").lower()
        if choice == 'image':
            image_data = input("Enter image data (base64 encoded): ")
            video_data = None
            link = None
        elif choice == 'video':
            image_data = None
            video_data = input("Enter video data (base64 encoded): ")
            link = None
        elif choice == 'link':
            image_data = None
            video_data = None
            link = input("Enter link: ")
        else:
            print("Invalid choice. No additional data will be added.")
            image_data = None
            video_data = None
            link = None

    return ptitle, pmessage, image_data, video_data, link


def message_search_and_counts():    
    print('1. Enter the title to search a message')
    print('2. No. of posts sent by particular user')
    user_input = input('Choose what do you like to do?')
    
    if user_input == '1':
        input_title = input('Enter the title:')
        message = collection.find_one({"Title": input_title})
        
        if message:
            print(f'Message for this title {message["Title"]} is',message["Message"])  
        else:
            print("Message not found.")
    
    elif user_input == '2':
        field_entries = "Username"
        value_to_check = input("Enter the username you want to check: ")
        pipeline = [{"$match":{field_entries: value_to_check}}, 
                               {"$count":"count"}
                               ]
        result = list(collection.aggregate(pipeline))
        if result:
            print(f" '{value_to_check}' has sent {result[0]['count']} messages ")
        else:
            print(f" '{value_to_check}' does not post messages ")

    else:
        print("You didn't choose the right option")

