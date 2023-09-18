from selenium import webdriver

from bs4 import BeautifulSoup
from selenium_stealth import stealth

video_id = ""

def mainFunc():
    driver = webdriver.Chrome()
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    url = f"https://www.youtube.com/live_chat?v={video_id}"
    driver.get(url)
    latest_id = None
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        mydivs = soup.find_all("yt-live-chat-text-message-renderer", {"class": "style-scope yt-live-chat-item-list-renderer"})
        if mydivs[-1]["id"] == latest_id: pass
        else:
            print(mydivs[-1]["id"])
            latest_id = mydivs[-1]["id"]
        
        
        

mainFunc()
