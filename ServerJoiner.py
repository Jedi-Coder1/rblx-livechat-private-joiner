from getytchat import ytchat

chat = ytchat("")
while True:
    nextC = chat.NextChat()
    if nextC:
        author, msg = nextC
        print(f"{author} said: {msg}")