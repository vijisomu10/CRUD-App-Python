from pymongo import MongoClient
# Skapa en anslutning till MongoDB
client = MongoClient ("mongodb://localhost:27017/")
# Valj en databas
db = client.crud_app
# Valj en samling
collection = db.postMessaages


def post_message():    
    post_message = input('Would you like to post a message(Y/N)?')
    if post_message.upper() == 'Y':             
        ptitle = input('In which title you want to post the message?')
        pmessage = input('Enter your message:')
        return ptitle, pmessage
    else:
        print('Not interest to post any message now')


def message_search_and_counts():    
    print('1. Enter the title to search a message')
    print('2. No. of posts sent by particular user')
    user_input = input('Choose what do you like to do?')
    if(user_input == '1'):
        input_title = input('Enter the title:')
        message = collection.find_one({"Title": input_title})
        
        if message:
            print(f'Message for this title {message["Title"]} is',message["Message"])  
        else:
            print("Message not found.")
    
    elif(user_input == '2'):
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

