from datetime import datetime, time


class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None


class ChatMessage:

  def __init__(self,sent_by,sent_to,text,sent_by_me):

    self.sent_by = sent_by
    self.sent_to = sent_to
    self.text = text
    self.time = datetime.now()
    self.sent_by_me = sent_by_me


spy = Spy('Samar', 'Miss.', 19, 4.0)


friend_one = Spy('Pawan', 'Mr.', 20, 4.9)
friend_two = Spy('Pine', 'Ms.', 21, 3.0)
friend_three = Spy('Mashook', 'Dr.', 37, 4.95)
friends = [friend_one, friend_two, friend_three]
#friends = []
chatmessage = Spy
msg = ChatMessage('','','','')



