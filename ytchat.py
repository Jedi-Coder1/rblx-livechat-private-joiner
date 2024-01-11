from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchWindowException
from selenium_stealth import stealth

options = ChromeOptions()
options.add_argument("-headless")
video_id = ""

def getDetails(drivwr, id) -> tuple:
    container = drivwr.find_element(By.ID, id)
    # Get Message
    content = container.find_element(By.ID, "content")
    message = content.find_element(By.ID, "message")
    # Get Author
    authorchip = container.find_element(By.CSS_SELECTOR, "yt-live-chat-author-chip")
    author = authorchip.find_element(By.ID, "author-name")
    return (author.text.encode('ascii', 'ignore'), message.text.encode('ascii', 'ignore'))

def mainFunc():
    driver = webdriver.Chrome(options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    url = "https://www.youtube.com/live_chat?v=" + video_id
    driver.get(url)
    latest_id = None
    
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        mydivs = soup.find_all("yt-live-chat-text-message-renderer", {"class": "style-scope yt-live-chat-item-list-renderer"})
        if mydivs[-1]["id"] == latest_id: pass
        else:
            latest_id = mydivs[-1]["id"]
            author, msg = getDetails(driver, mydivs[-1]["id"])
            print(f"{author.decode()} said: {msg.decode()}")


try:
     mainFunc()
except NoSuchWindowException:
    raise SystemExit("Browser Closed")