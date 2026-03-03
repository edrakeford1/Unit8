"""
8-9
Make a list containing a series of short text messages. Pass the list to a function called show_messages() which prints each
text message
"""

def show_messages(messages):
    if not messages:
        print('no messages to show')
        return
    for message in messages:
        print(message)

def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"Sending:\n{message}")
        print()
        sent_messages.append(message)

messages = ['hello', 'how are you', 'good to see you']
sent_messages = []

send_messages(messages, sent_messages)
show_messages(messages)
show_messages(sent_messages)

"""
8-10
Sending message
Building on exercise 8-9, write a function called send_messages() that prints each text message and moves each message to a new list
called sent_messages as it's printed. After calling the function, print both of your lists to make sure the messages
were moved correctly
"""

