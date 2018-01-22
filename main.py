# **+@ To Use CSV Functionality @+**
import csv

#** +@ To Import Elements Of Other Class @+**
from spy_details import spy, friends, Spy, ChatMessage, chatmessage

#** +@ To Check Image Extension @+**
import imghdr

#** +@ To Implement Hiding Text In Image @+**
from steganography.steganography import Steganography

#** +@ To Use Different Colors In Texts @+**
from colorama import init
from colorama import Fore, Style, Back

from termcolor import colored


from datetime import datetime
import os
import sys

# |+@pre stored status message list @+|
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

chats = []

#*********************** +@ ADD STATUS MODULE @+ ***************************************************************************

def add_status(current_status_message):

    updated_status_message = None

    if current_status_message != None:

        print 'Your current status message is %s \n' % (current_status_message)

    else:

        print 'You don\'t have any status message currently \n'


    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":

        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:

            updated_status_message = new_status_message

            STATUS_MESSAGES.append(updated_status_message)


    elif default.upper() == "Y":

        item_position = 1

        for message in STATUS_MESSAGES:

            print '%d. %s' % (item_position, message)

            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:

            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:

        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:

        print 'Your updated status message is: %s' % (updated_status_message)

        print"Status Successfully updated \n Spy select other activity from menu to move further in this application"

    else:

        print 'You did not update your status message'

    return updated_status_message


#*********************** +@ MODULE TOREAD CHATS OF OTHERS @+ ***************************************************************************

def read_chat_of_a_friend():

    if len(friends) > 0:

        print "Select the friend whose chat you wanna have ur eye on.."

        friend_choice = select_a_friend()

        sent_to = friends[friend_choice].name

        with open('chats.csv', 'rU') as chat:

            reader = csv.reader(chat)

            for row in reader:
                if row[1] == sent_to:
                    '''
                    print 'Message is :' + (Fore.BLACK + row[2])
                    print "Time       : " + (Fore.BLUE+ row[3])
                    print "Sent_by    : " + (Fore.CYAN + row[0])
                    print 'Sent to    :' + (Fore.RED + row[1])
                    '''
                    print 'Message is :',colored(row[2], 'red')#,attrs=['bold','concealed'])
                    print "Time       : ",colored(row[3], 'blue')#,attrs=['blink'])
                    print "Sent_by    : ",colored(row[0], 'cyan')#,attrs=['underline','blink'])
                    print 'Sent to    :',colored(row[1], 'red')#,attrs=['dark','bold'])


    else:

        print"Hey Spy! You don't have friends yet..... Add friends soon... GOOD LUCK.."


#*********************** +@ LOAD FRIENDS MODULE @+ ***************************************************************************

def load_friends():

    with open('friends.csv', 'rb') as friends_data:
      reader = csv.reader(friends_data)


      for row in reader:
           #print row[2]
           spy = Spy(name=row[0], salutation=row[1], age=`row[2]`, rating=`row[3]`)
           friends.append(spy)



#*********************** +@ MODULE TO LOAD CHATS @+ ***************************************************************************

def load_chat():

    with open('chats.csv', 'rU') as message:
        reader = csv.reader(message)

        for row in reader:
            read = ChatMessage(sent_by=row[0], sent_to=row[1], text=row[2],sent_by_me=True)
            chats.append(read)

    for chat in chats:
        print "%s has sent message %s to %s" % (chat.sent_by, chat.text, chat.sent_to)


#******************* +@ ADD A FRIEND MODULE @+ *****************************************************************************

def add_friend():

    name = input("Please add your friend's name: ")

    salutation = input("Are they Mr. or Ms.?: ")

    name = salutation + " " + name

    age = input("Age?")

    rating = input("Spy rating?")

    load_friends()

    if len(name) > 0 and age > 12 and rating >= spy.rating:
        new_friend = Spy(name=name,salutation=salutation,age=age,rating=rating)
        friends.append(new_friend)


        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.salutation,new_friend.age,new_friend.rating,new_friend.is_online])

        print 'Friend Added Successfully!'

    else:

        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    load_friends()
    return len(friends)


#***************** +@ SELECT A FRIEND MODULE @+ ****************************************************************************

def select_a_friend():

    load_friends()
    item_number = 0

    for friend in friends:

        print "%d. %s is online" % (item_number+1 , friend.name)

        item_number = item_number + 1

    friend_choice = input("Choose from your friends")

    friend_choice_position = friend_choice - 1

    return friend_choice_position


#*********************** +@ MODULE TO TACKLE SPECIAL MESSAGES @+ ***************************************************************************

def special_message(original_image,output_path,text):

    if (text == "SOS"):
        text = "Ballu Crazy"
        Steganography.encode(original_image, output_path, text)

    elif(text == "SAVE ME"):
        text = "Kiran Don Save Me"
        Steganography.encode(original_image, output_path, text)

    elif(text == "EMERGENCY"):
        text = "O... Saini Emergency, Call Pazim!!"
        Steganography.encode(original_image, output_path, text)

    elif(text == "SECRECY"):
        text = "Have Secrecy, It's Needed"
        Steganography.encode(original_image, output_path, text)


#**************** +@ SEND A SECRET MESSAGE MODULE @+ ***********************************************************************

def send_message():

    if len(friends) > 0:

        friend_choice = select_a_friend()

        original_image = input("What is the name of the image?")

        im = imghdr.what('input.jpg') # To Check Type Of File Entered.....
        print 'The type of file entered is %s' %(im)

        output_path = "output.jpg"

        text = input("What do you want to say? ")
        if (text == "SOS" or text == "SAVE ME" or text == "EMERGENCY" or text == "SECRECY"):

            special_message(original_image,output_path,text)

        else:

            Steganography.encode(original_image, output_path, text)

        print(Fore.LIGHTMAGENTA_EX + 'Message Sent Successfully')

        new_chat = ChatMessage('','','',sent_by_me = True)

        friends[friend_choice].chats.append(new_chat)

        with open('chats.csv', 'a' ) as chat_data:
            writer = csv.writer(chat_data)
            writer.writerow([spy.name,friends[friend_choice].name, text,new_chat.time,new_chat.sent_by_me])

        print "Your secret message image is ready!"

    else:
        print "Add Friends Soon.........!"


#**************** +@ READ AND SAVE SECRET MESSAGE MODULE @+ ***********************************************************************

def read_message():

    sender = select_a_friend()

    output_path = input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    friends[sender].chats.append(chatmessage)

    print (Fore.BLUE + "Your secret message has been saved!")


#******************** +@ START CHAT MODULE @+ ***************************************************************************************

def start_chat(spy):

    load_chat()

    show_menu = True

    current_status_message = None

    while show_menu == True:

        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3. Send a secret message\n 4. Read a personal message\n 5. Read chats from a user\n 6. Close Application\n"

        menu_choice = input(menu_choices)


        if menu_choice == 1:

            print "Dear %s add a status update that will disapper automatically after 24 hours" % (spy.name)
            current_status_message = add_status(current_status_message)

        elif menu_choice == 2:

            print "%s you can add a friend" % (spy.name)
            number_of_friends = add_friend()
            print 'You have %d friends' % (number_of_friends)

        elif menu_choice == 3:

            print "%s you should have secrecy let\'s send secret messages to your friends" % (spy.name)
            send_message()

        elif menu_choice == 4:

            print "Hey %s let\'s read personal messages" % (spy.name)
            read_message()

        elif menu_choice == 5:

            print "Oh Yea!!\n %s now let\'s read chats from other users" % (spy.name)
            read_chat_of_a_friend()

        elif menu_choice == 6:

             show_menu = False

        else:

            print "%s kindly choose a valid menu option" % (spy.name)


    #while menu_choice != 6:

        #start_chat(spy)

    print("Good bye")


print "Hello!"

print 'Let\'s get started'

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y\N)? "
existing = raw_input(question)

if (existing.upper() == "Y"):

  print "Welcome %s to spychat having age %d with rating %.2f" % (spy.name,spy.age,spy.rating)
  load_friends()
  start_chat(spy)


else:

    print "Dear Spy Firstly Create A New Account So Enter Your Details Carefully."

    spy.name = input("Welcome to spy chat, you must tell me your spy name first: ")


    # spy_name cannot be empty and can have only alphabets.
    if len(spy.name) > 0 and spy.name.isalpha():

        print 'Welcome ' + spy.name + '. Glad to have you back with us.'

        spy.salutation = input("Should I call you Mister or Miss?: ")

        spy.name = spy.salutation + " " + spy.name

        print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed..."



        spy_age = input("What is your age?")
        #spy.age = int(raw_input("What is your age?")) # {for age to have only integer value}

        # age restriction.
        if spy.age > 12 and spy.age < 50:

            spy.rating = input("What is your spy rating?")

            if spy.rating > 4.5:
                print 'Great ace!'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            #spy['is_online'] = True

            # String integer objects typecasting using str(), repr() or backtick
            # print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
            # print "Authentication complete. Welcome " + spy_name + " age: " + repr(spy_age) + " and rating of: " + repr(spy_rating) + " Proud to have you onboard"
            # print "Authentication complete. Welcome " + spy_name + " age: " + `spy_age` + " and rating of: " + `spy_rating` + " Proud to have you onboard"

            # using placeholders
            print "Authentication complete. Welcome %s age: %d and rating of: %.2f Proud to have you onboard" % (spy.name,spy.age,spy.rating)

            start_chat(spy)


        else:

            print 'Sorry you are not of the correct age to be a spy'


    else:

        print "A spy needs to have a valid name and name of spy can only have alphabets. Try again please."
