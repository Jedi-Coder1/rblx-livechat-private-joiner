import re
from getytchat import ytchat

chat = ytchat("")
while True:
    nextC = chat.NextChat()
    if nextC:
        author, msg = nextC
        URL = re.search(r"https:\/\/www.roblox\.com\/share.code=[a-z0-9-]+&type=Server", msg)
        if URL:
            print(URL.group())
        else:
            print(f"{author} said: {msg}")