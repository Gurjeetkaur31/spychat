from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online
import sys


def start_chat(spy_name, spy_age, spy_rating):

    menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3. Send a secret message\n 4. Read a personal message\n 5. Read chats from a user\n 6. Exit application or Logout"

    menu_choice = input(menu_choices)

    if menu_choice == 1:

        print "Dear %s add a status update that will disapper automatically after 24 hours" % (spy_name)

    elif menu_choice == 2:

        print "%s you might either accept friend request or send a friend request to your friends" % (spy_name)

    elif menu_choice == 3:

        print "%s you should have secrecy let\'s send secret messages to your friends" % (spy_name)

    elif menu_choice == 4:

        print "Hey %s let\'s read personal messages" % (spy_name)

    elif menu_choice == 5:

        print "Oh Yea!!\n %s now let\'s read chats from other users" % (spy_name)

    elif menu_choice == 6:

        sys.exit(0)

    else:

        print "%s kindly choose a valid menu option" % (spy_name)


    while menu_choice != 6:

        start_chat(spy_name,spy_age,spy_rating)

    print("Good bye")

print "Hello!"

print 'Let\'s get started'

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Yes/No)? "
existing = raw_input(question)

if existing == "Y" :
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

      spy_age = input("What is your age?")

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
