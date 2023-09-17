from selenium import webdriver
from selenium_stealth import stealth
import time

driver = webdriver.Chrome()

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://www.youtube.com/live_chat?is_popout=1&v=9lhUIEs6HiM"
driver.get(url)
time.sleep(5)
driver.quit()
