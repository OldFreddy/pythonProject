prompt = '\nTell me something'
prompt += '\nEnter quit to leave '
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)