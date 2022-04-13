def show_messages(messages):
    for message in messages:
        print(message.title())

def send_messages(messages):
    sent_messages = []

    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
    print(messages)
    print(sent_messages)

messages_massive = ['messag1', 'messag2', 'message3']

#show_messages(messages_massive)

send_messages(messages_massive)