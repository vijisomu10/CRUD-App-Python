Exercise:
CRUD Application
Console/terminal-based CRUD application (CRUD → Create, Read, Update, and Delete).
Ability to create users.
A user has a first name, last name, username (unique), password, address, and phone number [To be stored in a relational database].
Users should be able to log in, and when a user logs in, it should be logged to a CSV file (user_login.csv), which should be read and long-term stored in a relational database every hour (Subsequently cleared so it is empty).
When the CSV file is updated, the number of logins for that hour should also be logged to an Excel file (login_history.xlsx) with information about year, month, day, hour, and count.
Users should also be able to update their first name, last name, (password, address, and phone number).
Users should also be able to post messages to the "wall". (MongoDB)
A message contains a title, a username, and a text message but can also contain an image, a video, or a number of links.
These should be saved in MongoDB (Images, videos, and links are faked in our application as text).
It should also be possible to search for a message title and retrieve it from the database. Similarly, it should be possible to check how many messages a user has posted on the wall!

Solution:
1.	This is a simple user registration with CRUD operations. Execute main.py
2.	CRUD application has database [crup_app] with two tables user and user_login. Login entry stored in csv file and for testing purpose, added user_log.txt. Every hour scheduled to csv file to store the data in login_history.xlsx and deleted from csv file. 
3.	In CRUD app, (main.py)Main menu has register new user, login, mongoDB message search and exit
4.	Register new user - enter user details, login details and created in the database.
5.	Registration has validation functionalities for mobile number, postal code and password. Try to enter wrong format and test it.
6.	Already registered user has Update user details, post message (MongoDb), Delete the user account and logout functionalities.
7.	Message search has MONGODB operations like search for the specific message and number of messages sent by specific user 
8.	csv_file updated every hour by scheduler run
9.	excel file stores the hourly records based on user activity