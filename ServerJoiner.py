import re, requests
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
            print()
    else:
        print('Channel Is Not Live')
        start()

start()