from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")
    mydivs = soup.find_all("div", {"class": "style-scope yt-live-chat-item-list-renderer"})
    print(mydivs)

mainFunc()
