from getytchat import ytchat

chat = ytchat("jfKfPfyJRdk")
while True:
    author, msg = chat.NextChat()
    print(f"{author} said: {msg}")