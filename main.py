from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online

import sys

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']


friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []


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



def add_friend():

    new_name = raw_input("Please add your friend's name: ")

    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    new_name = new_name + " " + new_salutation

    new_age = input("Age?")

    new_rating = input("Spy rating?")

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:

        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print 'Friend Added Successfully'
        print "Spy let\'s do something further,select from menu your preferable option"

    else:

        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)

def start_chat(spy_name, spy_age, spy_rating):

    show_menu = True

    current_status_message = None

    while show_menu == True:

        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3. Send a secret message\n 4. Read a personal message\n 5. Read chats from a user\n 6. Close Application\n"

        menu_choice = input(menu_choices)


        if menu_choice == 1:

            print "Dear %s add a status update that will disapper automatically after 24 hours" % (spy_name)
            current_status_message = add_status(current_status_message)

        elif menu_choice == 2:

            print "%s you can add a friend" % (spy_name)
            number_of_friends = add_friend()
            print 'You have %d friends' % (number_of_friends)

        elif menu_choice == 3:

            print "%s you should have secrecy let\'s send secret messages to your friends" % (spy_name)

        elif menu_choice == 4:

            print "Hey %s let\'s read personal messages" % (spy_name)

        elif menu_choice == 5:

            print "Oh Yea!!\n %s now let\'s read chats from other users" % (spy_name)

        elif menu_choice == 6:

             show_menu = False

        else:

            print "%s kindly choose a valid menu option" % (spy_name)


    #while menu_choice != 6:

        #start_chat(spy_name,spy_age,spy_rating)

    print("Good bye")


print "Hello!"

print 'Let\'s get started'

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y\N)? "
existing = raw_input(question)

if existing.upper() == "Y" :
  print "Welcome %s to spychat having age %d with rating %.2f" % (spy_name,spy_age,spy_rating)


  start_chat(spy_name,spy_age,spy_rating)


else:

  print "Dear Spy Firstly Create A New Account So Enter Your Details Carefully."

  spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")


  # spy_name cannot be empty and can have only alphabets.
  if len(spy_name) > 0 and spy_name.isalpha():

      print 'Welcome ' + spy_name + '. Glad to have you back with us.'

      spy_salutation = raw_input("Should I call you Mister or Miss?: ")

      spy_name = spy_salutation + " " + spy_name

      print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

      # duck-typing.
      spy_age = 0

      spy_rating = 0.0

      spy_is_online = False

      # spy_age = input("What is your age?")
      spy_age = int(raw_input("What is your age?")) # {for age to have only integer value}

      # age restriction.
      if spy_age > 12 and spy_age < 50:

          spy_rating = input("What is your spy rating?")

          if spy_rating > 4.5:
              print 'Great ace!'
          elif spy_rating > 3.5 and spy_rating <= 4.5:
              print 'You are one of the good ones.'
          elif spy_rating >= 2.5 and spy_rating <= 3.5:
              print 'You can always do better'
          else:
              print 'We can always use somebody to help in the office.'

          spy_is_online = True

          # String integer objects typecasting using str(), repr() or backtick
          # print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
          # print "Authentication complete. Welcome " + spy_name + " age: " + repr(spy_age) + " and rating of: " + repr(spy_rating) + " Proud to have you onboard"
          # print "Authentication complete. Welcome " + spy_name + " age: " + `spy_age` + " and rating of: " + `spy_rating` + " Proud to have you onboard"

          # using placeholders
          print "Authentication complete. Welcome %s age: %d and rating of: %.2f Proud to have you onboard" % (spy_name,spy_age,spy_rating)

          start_chat(spy_name,spy_age,spy_rating)


      else:
          print 'Sorry you are not of the correct age to be a spy'


  else:

      print "A spy needs to have a valid name and name of spy can only have alphabets. Try again please."
