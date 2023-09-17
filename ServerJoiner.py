import pytchat, re, requests
channel_url = 'Enter Channel Url Here'

def GetLastestStreamId():
    try:
        html = requests.get(channel_url+'/streams').text
        id = int(re.search('(?<="videoId":").*?(?=")',html).group())
        return id
    except:
        return None

def check():
    request = requests.get(channel_url)
    TEXT = request.text.encode("ascii", "ignore").decode()
    if 'hqdefault_live.jpg' in TEXT:
        return True
    else: 
        return False


def start():
    Vid_Id = GetLastestStreamId()
    Is_Live = check()
    if Is_Live == True:
        if Vid_Id == None:
            print('No Video Id')
        else:
            chat = pytchat.create(Vid_Id)
            while chat.is_alive():
                    for c in chat.get().sync_items():
                        author= c.author.name.encode("ascii", "ignore").decode()
                        msg = c.message.encode("ascii", "ignore").decode()
                        print("Given text contains some URL")
                        URL = re.search("(?P<url>https?://[^\s]+)", msg).group("url")
                        if 'https://www.roblox.com/' in URL:
                            print('Joining Game')
                        else:
                            print(f'{author}: {msg}')
    else:
        print('Channel Is Not Live')
        start()

start()
