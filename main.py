from spy_details import spy
from steganography.steganography import Steganography
from datetime import datetime

import sys

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

friends = []


###### ADD STATUS MODULE

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



###### ADD A FRIEND MODULE

def add_friend():


    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    # using dictionary data type, there is need to use "" again and again when we use input so to avoid it i preferred here using raw input..
    new_friend['name'] = raw_input("Please add your friend's name: ")

    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = raw_input("Age?")

    new_friend['rating'] = raw_input("Spy rating?")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:

        friends.append(new_friend)

        print 'Friend Added Successfully!'

    else:

        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)



###### SELECT A FRIEND MODULE

def select_a_friend():


    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend['name'],
                                                                 friend['age'],
                                                                 friend['rating'])
        item_number = item_number + 1

    friend_choice = input("Choose from your friends")

    friend_choice_position = friend_choice - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()

    original_image = input("What is the name of the image?")

    output_path = "output.jpg"

    text = input("What do you want to say? ")

    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)

    print "Your secret message image is ready!"


def read_message():

    sender = select_a_friend()

    output_path = input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)

    print "Your secret message has been saved!"

###### START CHAT METHOD

def start_chat(spy):

    show_menu = True

    current_status_message = None

    while show_menu == True:

        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3. Send a secret message\n 4. Read a personal message\n 5. Read chats from a user\n 6. Close Application\n"

        menu_choice = input(menu_choices)


        if menu_choice == 1:

            print "Dear %s add a status update that will disapper automatically after 24 hours" % (spy['name'])
            current_status_message = add_status(current_status_message)

        elif menu_choice == 2:

            print "%s you can add a friend" % (spy['name'])
            number_of_friends = add_friend()
            print 'You have %d friends' % (number_of_friends)

        elif menu_choice == 3:

            print "%s you should have secrecy let\'s send secret messages to your friends" % (spy['name'])
            send_message()

        elif menu_choice == 4:

            print "Hey %s let\'s read personal messages" % (spy['name'])
            read_message()

        elif menu_choice == 5:

            print "Oh Yea!!\n %s now let\'s read chats from other users" % (spy['name'])

        elif menu_choice == 6:

             show_menu = False

        else:

            print "%s kindly choose a valid menu option" % (spy['name'])


    #while menu_choice != 6:

        #start_chat(spy)

    print("Good bye")


print "Hello!"

print 'Let\'s get started'

question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y\N)? "
existing = raw_input(question)

if existing.upper() == "Y" :
  print "Welcome %s to spychat having age %d with rating %.2f" % (spy['name'],spy['age'],spy['rating'])


  start_chat(spy)


else:

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    print "Dear Spy Firstly Create A New Account So Enter Your Details Carefully."

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")


    # spy_name cannot be empty and can have only alphabets.
    if len(spy['name']) > 0 and spy['name'].isalpha():

        print 'Welcome ' + spy['name'] + '. Glad to have you back with us.'

        spy['salutation'] = raw_input("Should I call you Mister or Miss?: ")

        spy['name'] = spy['salutation'] + " " + spy['name']

        print "Alright " + spy['name'] + ". I'd like to know a little bit more about you before we proceed..."



        # spy_age = input("What is your age?")
        spy['age'] = int(raw_input("What is your age?")) # {for age to have only integer value}

        # age restriction.
        if spy['age'] > 12 and spy['age'] < 50:

            spy['rating'] = input("What is your spy rating?")

            if spy['rating'] > 4.5:
                print 'Great ace!'
            elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
                print 'You are one of the good ones.'
            elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            spy['is_online'] = True

            # String integer objects typecasting using str(), repr() or backtick
            # print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
            # print "Authentication complete. Welcome " + spy_name + " age: " + repr(spy_age) + " and rating of: " + repr(spy_rating) + " Proud to have you onboard"
            # print "Authentication complete. Welcome " + spy_name + " age: " + `spy_age` + " and rating of: " + `spy_rating` + " Proud to have you onboard"

            # using placeholders
            print "Authentication complete. Welcome %s age: %d and rating of: %.2f Proud to have you onboard" % (spy['name'],spy['age'],spy['rating'])

            start_chat(spy)


        else:

            print 'Sorry you are not of the correct age to be a spy'


    else:

        print "A spy needs to have a valid name and name of spy can only have alphabets. Try again please."
