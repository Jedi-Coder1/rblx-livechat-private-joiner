import re, os
from getytchat import ytchat

chat = ytchat("")
while True:
    nextC = chat.NextChat()
    if nextC:
        author, msg = nextC
        regex = re.search(r"https:\/\/www.roblox\.com\/share.code=[a-z0-9-]+&type=Server", msg.decode())
        if regex:
            os.startfile(regex.group())
        else:
            print(f"{author} said: {msg}")