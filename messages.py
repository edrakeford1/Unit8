"""
8-9
Make a list containing a series of short text messages. Pass the list to a function called show_messages() which prints each
text message
"""

def show_messages(messages):
    for message in messages:
        print(message)

messages = ['hello', 'how are you', 'good to see you']
show_messages(messages)
